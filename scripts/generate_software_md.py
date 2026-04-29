#!/usr/bin/env python3
"""Generate a MkDocs page listing available UCT HPC software modules.

Expected repo layout, based on the current workflow:

    eresearch_docs/
      scripts/
        generate_software_md.py
        hpc-software-json.txt
        hpc-software-lookup-sorted.yml
        available-software.md

The input JSON is expected to come from the Tcl Environment Modules metadata output,
with module entries such as `software/abaqus-2024` and optional top-level wrapping by
modulefile directory.

Output format:
    A single searchable Markdown table, grouped by logical software name, with:
      - category
      - clean software name, linked to a website where available from the YAML lookup file
      - description, where available from the YAML lookup file
      - installed versions
      - exact module names to use with `module load`
"""

import json
import re
from datetime import date
from pathlib import Path

try:
    import yaml
except ImportError:
    yaml = None


BASE_DIR = Path(__file__).resolve().parent
PROJECT_DIR = BASE_DIR.parent

INPUT_JSON = PROJECT_DIR / "scripts" / "hpc-software-json.txt"
METADATA_YAML = PROJECT_DIR / "scripts" / "hpc-software-lookup-sorted.yml"
OUTPUT_MD = PROJECT_DIR / "scripts" / "available-software.md"

TITLE = "Available software on HPC"
SOURCE = "ICTS HPC Environment Modules"
LAST_UPDATED = date.today().strftime("%d %B %Y")

EXCLUDE_MODULES = {
    "use.own",
    "module-info",
    "modules",
    "module-git",
    "null",
    "dot",
}

CATEGORY_ORDER = [
    "Programming languages & environments",
    "Compilers & toolchains",
    "Parallel computing",
    "Workflow, reproducibility & publishing",
    "Bioinformatics & genomics",
    "Proteomics & metabolomics",
    "Neuroimaging & medical imaging",
    "Climate, earth observation & geospatial",
    "Engineering, physics & materials simulation",
    "Mathematics, statistics & scientific computing",
    "Visualisation & interactive tools",
    "Cloud, data & system utilities",
    "Other software",
]

# Description-led category rules. These use YAML descriptions first, with the
# cleaned module base name included as extra context. Order matters.
DESCRIPTION_CATEGORY_RULES = [
    (
        r"\b(proteomics?|mass spectrometry|ms data|dia-?nn|maxquant|peptide|protein data search)\b",
        "Proteomics & metabolomics",
    ),
    (
        r"\b(neuroimaging|brain imaging|fmri|mri|diffusion mri|freesurfer|fsl|tortoise)\b",
        "Neuroimaging & medical imaging",
    ),
    (
        r"\b(climate|earth observation|nwp|insar|remote sensing|snap|cdo|gmtsar|geospatial)\b",
        "Climate, earth observation & geospatial",
    ),
    (
        r"\b(single[- ]cell|rna[- ]?seq|sequencing|genom(?:e|ic|ics)|variant|vcf|bcf|bam|sam|"
        r"alignment|aligner|assembler|assembly|metagenom|microbiome|phylogenom|phylogen|"
        r"transcriptome|transcript|k[- ]?mer|basecaller|nanopore|bioinformatics|haplotype)\b",
        "Bioinformatics & genomics",
    ),
    (
        r"\b(workflow|pipeline|reproducible|publishing|technical publishing|notebook|quarto|nextflow|snakemake)\b",
        "Workflow, reproducibility & publishing",
    ),
    (
        r"\b(finite element|simulation|molecular dynamics|materials?|engineering simulation|"
        r"electronic structure|fluid dynamics|hydrodynamics|monte carlo|qcd|collision|numerical simulations?)\b",
        "Engineering, physics & materials simulation",
    ),
    (
        r"\b(statistical computing|bayesian|mathematics|symbolic mathematics|numerical analysis|"
        r"scientific computing|linear algebra|jags|mathematica|matlab)\b",
        "Mathematics, statistics & scientific computing",
    ),
    (
        r"\b(visuali[sz]ation|visuali[sz]e|post processor|pre[- ]?processor|ide|integrated development environment|paraview|vscode|rstudio)\b",
        "Visualisation & interactive tools",
    ),
    (
        r"\b(message passing interface|mpi standard|parallel computing|parallel software|openmpi|mpich)\b",
        "Parallel computing",
    ),
    (
        r"\b(compiler|fortran|c\+\+|c language|programming language|runtime environment|python distribution|environment manager|julia compiler)\b",
        "Programming languages & environments",
    ),
    (
        r"\b(cloud|google cloud|file format|hdf5|shell tool|unix[- ]like|macro|template metaprogramming|system|utilities|toolkit)\b",
        "Cloud, data & system utilities",
    ),
]

# Name/prefix fallbacks for entries with sparse or missing YAML descriptions.
NAME_CATEGORY_RULES = [
    (r"^(python|r|julia|java|miniconda3)$", "Programming languages & environments"),
    (r"(gcc|intel|clang|compiler)", "Compilers & toolchains"),
    (r"(openmpi|mpich|mpi)", "Parallel computing"),
    (r"(nextflow|snakemake|quarto)", "Workflow, reproducibility & publishing"),
    (r"(diann|maxquant|mzmine|trinotate)", "Proteomics & metabolomics"),
    (r"(freesurfer|fsl|tortoise)", "Neuroimaging & medical imaging"),
    (r"(snap|cdo|gmstar|gmtsar)", "Climate, earth observation & geospatial"),
    (
        r"(bwa|bowtie|bowtie2|samtools|bcftools|bedtools|gatk|qiime|fastqc|"
        r"trimgalore|trimmomatic|hisat2|star|salmon|kallisto|cellranger|"
        r"kraken|kraken2|mothur|spades|quast|vep|minimap2|freebayes|snpeff|"
        r"sratoolkit|plink|subread|rsem|picard|mafft|iqtree|diamond|dorado|"
        r"bamtools|bbmap|breakdancer|delly|geva|gffread|jellyfish|metabat|"
        r"motifbinner|mummer|racon|skesa|trimal|trinity|vsearch)",
        "Bioinformatics & genomics",
    ),
    (
        r"(gromacs|lammps|namd|amber|jewel|vasp|castep|abaqus|ansys|dyna|"
        r"dualsphysics|dealii|gid-simulation|pythia)",
        "Engineering, physics & materials simulation",
    ),
    (r"(matlab|mathematica|jags)", "Mathematics, statistics & scientific computing"),
    (r"(paraview|vmd|vtk|vscode|rstudio)", "Visualisation & interactive tools"),
    (r"(parallel|hdf5|boost|autoconf|google-cloud-utils|load-test)", "Cloud, data & system utilities"),
]

FALLBACK_CATEGORY = "Other software"


def metadata_key(value: str) -> str:
    """Normalise metadata keys and parsed module bases for matching."""
    return str(value or "").strip().lower()


def compact_metadata_key(value: str) -> str:
    """A looser key for matching variants such as cellrangerarc/cellranger-arc."""
    return re.sub(r"[^a-z0-9]+", "", metadata_key(value))


def load_metadata(path: Path) -> dict:
    if not path.exists():
        return {}

    if yaml is None:
        raise RuntimeError(
            "PyYAML is required to load metadata. Install it with: pip install pyyaml"
        )

    with path.open("r", encoding="utf-8") as f:
        raw = yaml.safe_load(f) or {}

    # Normalise exact keys, while preserving metadata values.
    return {metadata_key(key): value for key, value in raw.items()}


def unwrap_modules(raw: dict) -> dict:
    """
    Handles files shaped like:
    {
      "/opt/.../modulefiles": {
        "software/x": {...}
      }
    }

    Also works if the file is already flat.
    """
    if len(raw) == 1:
        only_value = next(iter(raw.values()))
        if isinstance(only_value, dict):
            if any(
                isinstance(v, dict) and v.get("type") == "modulefile"
                for v in only_value.values()
            ):
                return only_value

    return raw


def clean_name(raw_name: str):
    """
    Convert a module name into namespace, clean software base name, and version.

    This avoids "split on the last dash" behaviour, which produced incorrect
    groupings such as:
      software/ansys-2025R2-v252 -> ansys-2025R2 / v252

    Instead, it treats the first dash/underscore segment that looks like a
    version as the start of the version string:
      software/ansys-2025R2-v252 -> ansys / 2025R2-v252
      software/cellranger-arc-2.1.0 -> cellranger-arc / 2.1.0
      python/miniconda3-py3.12 -> miniconda3 / py3.12
      software/load-test -> load-test / ""
    """
    if "/" in raw_name:
        prefix, module_name = raw_name.split("/", 1)
    else:
        prefix, module_name = "", raw_name

    module_name = module_name.strip()

    # Version segments usually start with a number, R+number, v+number, or py+number.
    # Prefer dash/underscore-separated versions so names such as
    # "cellranger-arc-2.1.0" keep "cellranger-arc" as the base.
    match = re.match(r"^(.+?)[-_]((?:[RrVv]|py)?\d.*)$", module_name)

    if match:
        base, version = match.group(1), match.group(2)
    else:
        # Some module names attach the version directly to the software name,
        # e.g. "MUMmer3.23". Treat a trailing digit-dot-version as a version
        # only when the name has at least one letter before it. This avoids
        # damaging names that naturally contain digits but are not versioned.
        compact_match = re.match(r"^([A-Za-z][A-Za-z0-9_.+-]*?[A-Za-z])([0-9]+(?:\.[0-9A-Za-z]+)+.*)$", module_name)
        if compact_match:
            base, version = compact_match.group(1), compact_match.group(2)
        else:
            base, version = module_name, ""

    return prefix, base.strip(), version.strip()


def display_name(base: str) -> str:
    """Return a clean user-facing software name without version or module path."""
    known_upper = {
        "r", "gcc", "mpi", "openmpi", "mpich", "hdf5",
        "bwa", "gatk", "fastqc", "star", "rsem", "spades",
        "namd", "vasp", "vmd", "cdo", "fsl",
    }

    known_title = {
        "matlab": "MATLAB",
        "rstudio": "RStudio",
        "vscode": "VS Code",
        "paraview": "ParaView",
        "trimgalore": "Trim Galore",
        "maxquant": "MaxQuant",
        "cellranger": "Cell Ranger",
        "cellranger-arc": "Cell Ranger ARC",
        "cellranger-atac": "Cell Ranger ATAC",
        "nextflow": "Nextflow",
        "samtools": "SAMtools",
        "bcftools": "BCFtools",
        "bedtools": "BEDTools",
        "bowtie2": "Bowtie 2",
        "minimap2": "Minimap2",
    }

    key = base.lower()

    if key in known_title:
        return known_title[key]
    if key in known_upper:
        return base.upper()
    return base


def metadata_for(base: str, metadata: dict) -> dict:
    """Return metadata for a parsed software base name.

    The exact key is preferred, but a compact fallback catches harmless YAML
    spelling differences such as ``cellrangerarc`` vs ``cellranger-arc``.
    """
    exact_key = metadata_key(base)
    if exact_key in metadata:
        return metadata[exact_key] or {}

    compact_key = compact_metadata_key(base)
    for key, value in metadata.items():
        if compact_metadata_key(key) == compact_key:
            return value or {}

    return {}


def description_for(base: str, metadata: dict) -> str:
    return metadata_for(base, metadata).get("description", "")


def url_for(base: str, metadata: dict) -> str:
    return metadata_for(base, metadata).get("url", "")


def categorise(prefix: str, base: str, metadata: dict) -> str:
    meta = metadata_for(base, metadata)
    meta_category = meta.get("category")
    if meta_category:
        return meta_category

    prefix_key = metadata_key(prefix)
    base_key = metadata_key(base)
    description = metadata_key(meta.get("description", ""))
    text = f"{base_key} {description}"

    # Prefixes are authoritative for infrastructure-level categories.
    if prefix_key == "compilers":
        return "Compilers & toolchains"
    if prefix_key == "mpi":
        return "Parallel computing"
    if prefix_key in {"python", "r", "java"}:
        return "Programming languages & environments"

    # Prefer category inference from the YAML description.
    for pattern, category in DESCRIPTION_CATEGORY_RULES:
        if re.search(pattern, text):
            return category

    # Fall back to the cleaned module base name for entries without descriptions.
    for pattern, category in NAME_CATEGORY_RULES:
        if re.search(pattern, base_key):
            return category

    if prefix_key == "tools":
        return "Cloud, data & system utilities"

    return FALLBACK_CATEGORY


def category_sort_key(category: str):
    if category in CATEGORY_ORDER:
        return CATEGORY_ORDER.index(category)
    return len(CATEGORY_ORDER)


def version_sort_key(version: str):
    """Best-effort sort for mixed versions like 6.14, 2024R1, 4.0.5a, default."""
    if not version or version == "default":
        return (1, "")

    parts = re.split(r"(\d+)", version.lower())
    normalised = [int(part) if part.isdigit() else part for part in parts]
    return (0, normalised)


def build_software_items(data: dict, metadata: dict) -> list[dict]:
    """Collapse module entries into one item per software package."""
    software_map = {}

    for key, value in data.items():
        if not isinstance(value, dict):
            continue

        if value.get("type") != "modulefile":
            continue

        raw_name = value.get("name", key)
        prefix, base, version = clean_name(raw_name)

        if raw_name.lower() in EXCLUDE_MODULES or base.lower() in EXCLUDE_MODULES:
            continue

        base_key = base.lower()

        if base_key not in software_map:
            software_map[base_key] = {
                "name": display_name(base),
                "base": base,
                "category": categorise(prefix, base, metadata),
                "description": description_for(base, metadata),
                "url": url_for(base, metadata),
                "versions": [],
            }

        software_map[base_key]["versions"].append(
            {
                "version": version or "default",
                "module": raw_name,
            }
        )

    items = []
    for item in software_map.values():
        # De-duplicate versions by module name, then sort by version.
        unique_versions = {v["module"]: v for v in item["versions"]}
        item["versions"] = sorted(
            unique_versions.values(),
            key=lambda x: version_sort_key(x["version"]),
        )
        items.append(item)

    return items


def html_escape(value: str) -> str:
    """Escape text for safe use in generated HTML."""
    if not value:
        return "—"
    import html
    return html.escape(str(value), quote=True)


def format_software_name_html(item: dict) -> str:
    """Return linked software name if a URL is available."""
    name = html_escape(item["name"])
    url = item.get("url", "")

    if url:
        return f'<a href="{html_escape(url)}"><strong>{name}</strong></a>'

    return f"<strong>{name}</strong>"


def format_versions_html(item: dict) -> str:
    if not item["versions"]:
        return "—"
    return "<br>".join(
        f"<code>{html_escape(v['version'])}</code>" for v in item["versions"]
    )


def format_modules_html(item: dict) -> str:
    if not item["versions"]:
        return "—"
    return "<br>".join(
        f"<code>{html_escape(v['module'])}</code>" for v in item["versions"]
    )


def item_sort_key(item: dict):
    return (category_sort_key(item["category"]), item["name"].lower())


def write_table_styles(out) -> None:
    """Write page-scoped CSS for the software table.

    This can be moved to docs/stylesheets/extra.css later if preferred.
    """
    out.write("""
<style>
  .software-table-controls {
    margin: 1rem 0;
  }

  .software-table-controls label {
    display: block;
    font-weight: 600;
    margin-bottom: 0.35rem;
  }

  .software-table-search {
    box-sizing: border-box;
    max-width: 32rem;
    width: 100%;
    padding: 0.45rem 0.6rem;
    border: 1px solid var(--md-default-fg-color--lighter);
    border-radius: 0.2rem;
    background: var(--md-default-bg-color);
    color: var(--md-default-fg-color);
  }

  .software-table-wrapper {
    overflow-x: auto;
    margin-top: 1rem;
  }

  table.software-table {
    width: 100%;
    border-collapse: collapse;
    font-size: 0.82rem;
  }

  .software-table caption {
    text-align: left;
    font-weight: 600;
    margin-bottom: 0.5rem;
  }

  .software-table th,
  .software-table td {
    border: 1px solid var(--md-default-fg-color--lightest);
    padding: 0.45rem 0.55rem;
    vertical-align: top;
  }

  .software-table thead th {
    background: var(--md-default-fg-color--lightest);
    font-weight: 700;
  }

  .software-table tbody tr:nth-child(even) {
    background: var(--md-code-bg-color);
  }

  .software-table tbody tr:hover {
    background: var(--md-accent-fg-color--transparent);
  }

  .software-table th button {
    all: unset;
    cursor: pointer;
    font: inherit;
    font-weight: 700;
    color: inherit;
  }

  .software-table th button:focus-visible {
    outline: 2px solid var(--md-accent-fg-color);
    outline-offset: 2px;
  }

  .software-table th[data-sortable="true"]::after {
    content: " ↕";
    font-size: 0.75em;
    opacity: 0.65;
  }

  .software-table th[aria-sort="ascending"]::after {
    content: " ↑";
  }

  .software-table th[aria-sort="descending"]::after {
    content: " ↓";
  }
</style>
""")


def write_table_script(out) -> None:
    """Write unobtrusive JavaScript for client-side search and selected-column sorting."""
    out.write("""
<script>
  document.addEventListener("DOMContentLoaded", function () {
    const table = document.getElementById("software-table");
    const searchInput = document.getElementById("software-table-search");
    const countOutput = document.getElementById("software-table-count");

    if (!table || !searchInput) return;

    const tbody = table.querySelector("tbody");
    const rows = Array.from(tbody.querySelectorAll("tr"));
    const sortableHeaders = table.querySelectorAll("th[data-sortable='true'] button");

    function updateCount() {
      const visibleRows = rows.filter(row => row.style.display !== "none").length;
      if (countOutput) {
        countOutput.textContent = visibleRows + " software entr" + (visibleRows === 1 ? "y" : "ies") + " shown";
      }
    }

    function filterRows() {
      const query = searchInput.value.trim().toLowerCase();

      rows.forEach(row => {
        const rowText = row.textContent.toLowerCase();
        row.style.display = rowText.includes(query) ? "" : "none";
      });

      updateCount();
    }

    function clearSortState() {
      table.querySelectorAll("th[aria-sort]").forEach(th => {
        th.setAttribute("aria-sort", "none");
      });
    }

    sortableHeaders.forEach(button => {
      button.addEventListener("click", () => {
        const th = button.closest("th");
        const columnIndex = Number(th.dataset.columnIndex);
        const currentSort = th.getAttribute("aria-sort");
        const nextSort = currentSort === "ascending" ? "descending" : "ascending";
        const direction = nextSort === "ascending" ? 1 : -1;

        const sortedRows = rows.slice().sort((a, b) => {
          const aValue = a.children[columnIndex].dataset.sortValue || a.children[columnIndex].textContent;
          const bValue = b.children[columnIndex].dataset.sortValue || b.children[columnIndex].textContent;
          return aValue.localeCompare(bValue, undefined, { numeric: true, sensitivity: "base" }) * direction;
        });

        sortedRows.forEach(row => tbody.appendChild(row));
        clearSortState();
        th.setAttribute("aria-sort", nextSort);
      });
    });

    searchInput.addEventListener("input", filterRows);
    updateCount();
  });
</script>
""")
    
def item_sort_key(item):
    return (
        item.get('category', '').lower(),
        item.get('name', '').lower()
    )


def main():
    metadata = load_metadata(METADATA_YAML)


    print(f"Metadata file: {METADATA_YAML}")
    print(f"Metadata entries loaded: {len(metadata)}")
    print("Example metadata for gromacs:", metadata.get("gromacs"))

    with INPUT_JSON.open("r", encoding="utf-8") as f:
        raw = json.load(f)

    data = unwrap_modules(raw)
    items = build_software_items(data, metadata)

    OUTPUT_MD.parent.mkdir(parents=True, exist_ok=True)

    with OUTPUT_MD.open("w", encoding="utf-8") as out:
        out.write(f"# {TITLE}\n\n")
        out.write(f"**Source:** {SOURCE}  \n")
        out.write(f"**Last updated:** {LAST_UPDATED}  \n\n")

        out.write(
            "Software on the UCT HPC system is provided through environment modules. "
            "This page helps you check what is currently available.\n\n"
        )

        out.write(
            "To use a specific version, copy the module name and load it on the HPC. "
            "See [How to load software modules](../../how-to/hpc/use-software-modules.md).\n\n"
        )

        out.write("## Available software\n\n")
        out.write(
            "Use the search box to filter the table. Select **Category** or **Software** "
            "to sort by that column.\n\n"
        )

        write_table_styles(out)

        out.write('<div class="software-table-controls">\n')
        out.write('  <label for="software-table-search">Search available software</label>\n')
        out.write(
            '  <input id="software-table-search" class="software-table-search" '
            'type="search" placeholder="Search by software, category, version, or module name" '
            'aria-describedby="software-table-count">\n'
        )
        out.write('  <p id="software-table-count" aria-live="polite"></p>\n')
        out.write('</div>\n\n')

        out.write('<div class="software-table-wrapper">\n')
        out.write('<table id="software-table" class="software-table">\n')
        out.write('  <caption>Available UCT HPC software modules</caption>\n')
        out.write('  <thead>\n')
        out.write('    <tr>\n')
        out.write(
            '      <th scope="col" data-sortable="true" data-column-index="0" aria-sort="none">'
            '<button type="button">Category</button></th>\n'
        )
        out.write(
            '      <th scope="col" data-sortable="true" data-column-index="1" aria-sort="none">'
            '<button type="button">Software</button></th>\n'
        )
        out.write('      <th scope="col">Description</th>\n')
        out.write('      <th scope="col">Versions installed</th>\n')
        out.write('      <th scope="col">Module names</th>\n')
        out.write('    </tr>\n')
        out.write('  </thead>\n')
        out.write('  <tbody>\n')

        for item in sorted(items, key=item_sort_key):
            out.write('    <tr>\n')
            out.write(
                f'      <td data-sort-value="{html_escape(item["category"].lower())}">'
                f'{html_escape(item["category"])}</td>\n'
            )
            out.write(
                f'      <td data-sort-value="{html_escape(item["name"].lower())}">'
                f'{format_software_name_html(item)}</td>\n'
            )
            out.write(f'      <td>{html_escape(item["description"])}</td>\n')
            out.write(f'      <td>{format_versions_html(item)}</td>\n')
            out.write(f'      <td>{format_modules_html(item)}</td>\n')
            out.write('    </tr>\n')

        out.write('  </tbody>\n')
        out.write('</table>\n')
        out.write('</div>\n\n')

        write_table_script(out)

    print(f"Written: {OUTPUT_MD}")


if __name__ == "__main__":
    main()