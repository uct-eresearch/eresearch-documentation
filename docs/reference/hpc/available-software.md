# Available software on HPC

**Source:** ICTS HPC Environment Modules  
**Last updated:** 29 April 2026  

Software on the UCT HPC system is provided through environment modules. This page helps you check what is currently available.

To use a specific version, copy the module name and load it on the HPC. See [How to load software modules](../../how-to/hpc/use-software-modules.md).

## Available software

Use the search box to filter the table. Select **Category** or **Software** to sort by that column.


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
<div class="software-table-controls">
  <label for="software-table-search">Search available software</label>
  <input id="software-table-search" class="software-table-search" type="search" placeholder="Search by software, category, version, or module name" aria-describedby="software-table-count">
  <p id="software-table-count" aria-live="polite"></p>
</div>

<div class="software-table-wrapper">
<table id="software-table" class="software-table">
  <caption>Available UCT HPC software modules</caption>
  <thead>
    <tr>
      <th scope="col" data-sortable="true" data-column-index="0" aria-sort="none"><button type="button">Category</button></th>
      <th scope="col" data-sortable="true" data-column-index="1" aria-sort="none"><button type="button">Software</button></th>
      <th scope="col">Description</th>
      <th scope="col">Versions installed</th>
      <th scope="col">Module names</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bamtools"><a href="https://bio.tools/bamtools"><strong>bamtools</strong></a></td>
      <td>BamTools provides a fast, flexible C++ API &amp; toolkit for reading, writing, and managing BAM files.</td>
      <td><code>2.5.2</code></td>
      <td><code>software/bamtools-2.5.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bbmap"><a href="https://jgi.doe.gov/data-and-tools/software-tools/bbtools/bb-tools-user-guide/bbmap-guide/"><strong>bbmap</strong></a></td>
      <td>Splice-aware global aligner for DNA and RNA sequencing reads.</td>
      <td><code>39.08</code></td>
      <td><code>software/bbmap-39.08</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bcftools"><a href="https://sourceforge.net/projects/samtools/"><strong>BCFtools</strong></a></td>
      <td>Variant calling and VCF/BCF file processing.</td>
      <td><code>1.20</code></td>
      <td><code>software/bcftools-1.20</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bedtools"><a href="https://github.com/arq5x/bedtools2"><strong>BEDTools</strong></a></td>
      <td>Tools for genomic interval manipulation.</td>
      <td><code>2.31.0</code></td>
      <td><code>software/bedtools-2.31.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bowtie"><a href="https://sourceforge.net/projects/bowtie-bio/files/bowtie/0.12.9/"><strong>bowtie</strong></a></td>
      <td>Short read aligner.</td>
      <td><code>0.12.9</code></td>
      <td><code>software/bowtie-0.12.9</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bowtie 2"><a href="http://bowtie-bio.sourceforge.net/bowtie2"><strong>Bowtie 2</strong></a></td>
      <td>Aligns sequencing reads to reference genomes.</td>
      <td><code>2.5.4</code></td>
      <td><code>software/bowtie2-2.5.4</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="breakdancer"><a href="https://github.com/genome/breakdancer"><strong>breakdancer</strong></a></td>
      <td>Genome-wide detection of structural variants.</td>
      <td><code>1.3.6</code></td>
      <td><code>software/breakdancer-1.3.6</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="bwa"><a href="https://github.com/lh3/bwa"><strong>BWA</strong></a></td>
      <td>Aligns sequencing reads to a reference genome.</td>
      <td><code>0.7.18</code></td>
      <td><code>software/bwa-0.7.18</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="cell ranger"><a href="https://www.10xgenomics.com/support/software/cell-ranger-atac/latest"><strong>Cell Ranger</strong></a></td>
      <td>Single-cell RNA-seq analysis pipeline (10x Genomics).</td>
      <td><code>7.2.0</code><br><code>8.0.0</code></td>
      <td><code>software/cellranger-7.2.0</code><br><code>software/cellranger-8.0.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="cell ranger arc"><a href="https://www.10xgenomics.com/support/software/cell-ranger-arc/latest"><strong>Cell Ranger ARC</strong></a></td>
      <td>Advanced analytical suite designed for Chromium Single Cell Multiome ATAC + Gene Expression sequencing.</td>
      <td><code>2.1.0</code></td>
      <td><code>software/cellranger-arc-2.1.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="cell ranger atac"><a href="https://www.10xgenomics.com/support/software/cell-ranger-atac/latest"><strong>Cell Ranger ATAC</strong></a></td>
      <td>Analysis pipelines that process Epi ATAC data.</td>
      <td><code>2.1.0</code></td>
      <td><code>software/cellranger-atac-2.1.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="delly"><a href="https://github.com/dellytools/delly"><strong>delly</strong></a></td>
      <td>Integrated structural variant prediction method</td>
      <td><code>1.3.3</code></td>
      <td><code>software/delly-1.3.3</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="diamond"><a href="https://github.com/bbuchfink/diamond"><strong>diamond</strong></a></td>
      <td>Fast sequence aligner for protein and translated DNA searches.</td>
      <td><code>2.1.9</code></td>
      <td><code>software/diamond-2.1.9</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="diann"><a href="https://github.com/vdemichev/DiaNN"><strong>diann</strong></a></td>
      <td>Proteomics data processing.</td>
      <td><code>1.9.2</code><br><code>2.1.0</code><br><code>2.3.2</code></td>
      <td><code>software/diann-1.9.2</code><br><code>software/diann-2.1.0</code><br><code>software/diann-2.3.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="dorado"><a href="https://github.com/nanoporetech/dorado"><strong>dorado</strong></a></td>
      <td>Basecaller for Oxford Nanopore reads.</td>
      <td><code>0.9.6</code><br><code>1.0.2</code><br><code>1.1.1</code><br><code>1.3.1</code></td>
      <td><code>software/dorado-0.9.6</code><br><code>software/dorado-1.0.2</code><br><code>software/dorado-1.1.1</code><br><code>software/dorado-1.3.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="fastqc"><a href="https://www.bioinformatics.babraham.ac.uk/projects"><strong>FASTQC</strong></a></td>
      <td>Quality control tool for sequencing data.</td>
      <td><code>0.12.1</code></td>
      <td><code>software/FastQC-0.12.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="freebayes"><a href="https://github.com/freebayes/freebayes"><strong>freebayes</strong></a></td>
      <td>Variant calling based on haplotype reconstruction.</td>
      <td><code>1.3.6</code></td>
      <td><code>software/freebayes-1.3.6</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="gatk"><a href="https://software.broadinstitute.org/gatk"><strong>GATK</strong></a></td>
      <td>Toolkit for variant discovery in genomic data.</td>
      <td><code>4.6.1.0</code></td>
      <td><code>software/gatk-4.6.1.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="geva"><a href="https://github.com/pkalbers/geva"><strong>geva</strong></a></td>
      <td>Genealogical Estimation of Variant Age.</td>
      <td><code>default</code></td>
      <td><code>software/geva</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="gffread"><a href="https://github.com/gpertea/gffread"><strong>gffread</strong></a></td>
      <td>Format conversions filtering FASTA sequence extraction and more.</td>
      <td><code>0.12.8</code></td>
      <td><code>software/gffread-0.12.8</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="hisat2"><a href="http://daehwankimlab.github.io/hisat2"><strong>hisat2</strong></a></td>
      <td>Fast alignment tool for RNA sequencing reads.</td>
      <td><code>2.2.1</code></td>
      <td><code>software/hisat2-2.2.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="iqtree2"><a href="https://github.com/iqtree/iqtree2"><strong>iqtree2</strong></a></td>
      <td>Phylogenomic inference.</td>
      <td><code>2.3.4</code></td>
      <td><code>software/iqtree2-2.3.4</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="jellyfish"><a href="https://www.genome.umd.edu/jellyfish.html"><strong>jellyfish</strong></a></td>
      <td>Tool for fast memory-efficient counting of k-mers in DNA.</td>
      <td><code>2.3.1</code></td>
      <td><code>software/jellyfish-2.3.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="kallisto"><a href="https://pachterlab.github.io/kallisto/starting"><strong>kallisto</strong></a></td>
      <td>Transcript quantification using pseudo-alignment.</td>
      <td><code>0.46.1</code></td>
      <td><code>software/kallisto-0.46.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="kraken2"><a href="https://github.com/DerrickWood/kraken2"><strong>kraken2</strong></a></td>
      <td>Taxonomic classification of metagenomic sequences.</td>
      <td><code>default</code></td>
      <td><code>software/kraken2</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="mafft"><a href="https://mafft.cbrc.jp/alignment/software"><strong>mafft</strong></a></td>
      <td>Multiple sequence alignment program.</td>
      <td><code>7.525</code></td>
      <td><code>software/mafft-7.525</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="maxquant"><a href="https://www.maxquant.org/maxquant/"><strong>MaxQuant</strong></a></td>
      <td>Quantitative proteomics software package.</td>
      <td><code>2.6.2.0</code></td>
      <td><code>software/MaxQuant-2.6.2.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="metabat"><a href="https://bitbucket.org/berkeleylab/metabat"><strong>metabat</strong></a></td>
      <td>A robust statistical framework for reconstructing genomes from metagenomic data.</td>
      <td><code>2.17</code></td>
      <td><code>software/metabat-2.17</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="minimap2"><a href="https://github.com/lh3/minimap2"><strong>Minimap2</strong></a></td>
      <td>Sequence alignment program for DNA and RNA reads.</td>
      <td><code>2.28</code></td>
      <td><code>software/minimap2-2.28</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="mothur"><a href="https://mothur.org/"><strong>mothur</strong></a></td>
      <td>Software to analyze community sequence data.</td>
      <td><code>1.48.1</code></td>
      <td><code>software/mothur-1.48.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="motifbinner2"><a href="https://github.com/HIVDiversity/MotifBinner2"><strong>MotifBinner2</strong></a></td>
      <td>MotifBinner processes high-throughput sequencing data of an RNA virus population.</td>
      <td><code>default</code></td>
      <td><code>software/MotifBinner2</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="mummer"><a href="http://mummer.sourceforge.net/"><strong>MUMmer</strong></a></td>
      <td>Rapid alignment of entire genomes.</td>
      <td><code>3.23</code></td>
      <td><code>software/MUMmer3.23</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="mzmine"><a href="https://mzmine.github.io/mzmine_documentation/index.html"><strong>mzmine</strong></a></td>
      <td>Software for mass spectrometry (MS) data processing and visualization</td>
      <td><code>4.7.29</code></td>
      <td><code>software/mzmine-4.7.29</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="picard"><a href="https://github.com/broadinstitute/picard/releases/tag/2.20.1"><strong>picard</strong></a></td>
      <td>Java-based command-line utilities that manipulate SAM files.</td>
      <td><code>2.20.1</code></td>
      <td><code>software/picard-2.20.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="pipseeker"><a href="https://www.fluentbio.com/"><strong>pipseeker</strong></a></td>
      <td>Single cell RNA analysis.</td>
      <td><code>3.3.0</code></td>
      <td><code>software/pipseeker-3.3.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="plink"><a href="https://www.cog-genomics.org/plink/"><strong>plink</strong></a></td>
      <td>Whole genome association analysis toolset.</td>
      <td><code>2.00a</code></td>
      <td><code>software/plink-2.00a</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="qiime2-amplicon"><a href="https://docs.qiime2.org/"><strong>qiime2-amplicon</strong></a></td>
      <td>Microbiome analysis package.</td>
      <td><code>default</code></td>
      <td><code>python/qiime2-amplicon</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="qiime2-metagenome"><a href="https://docs.qiime2.org/"><strong>qiime2-metagenome</strong></a></td>
      <td>Microbiome analysis package.</td>
      <td><code>default</code></td>
      <td><code>python/qiime2-metagenome</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="qiime2-tiny"><a href="https://docs.qiime2.org/"><strong>qiime2-tiny</strong></a></td>
      <td>Microbiome analysis package.</td>
      <td><code>default</code></td>
      <td><code>python/qiime2-tiny</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="quast"><a href="https://quast.sourceforge.net/"><strong>quast</strong></a></td>
      <td>Genome assembly quality assessment tool.</td>
      <td><code>5.2.0</code></td>
      <td><code>software/quast-5.2.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="racon"><a href="https://github.com/isovic/racon"><strong>racon</strong></a></td>
      <td>Consensus module for raw de novo DNA assembly of long uncorrected reads.</td>
      <td><code>1.5.0</code></td>
      <td><code>software/racon-1.5.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="rsem"><a href="https://github.com/deweylab/RSEM"><strong>RSEM</strong></a></td>
      <td>Accurate quantification of gene and isoform expression from RNA-Seq data.</td>
      <td><code>1.3.3</code></td>
      <td><code>software/RSEM-1.3.3</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="salmon"><a href="https://salmon.readthedocs.io/en/latest/salmon.html"><strong>salmon</strong></a></td>
      <td>Quantifies transcript expression from RNA-seq data.</td>
      <td><code>1.10.0</code></td>
      <td><code>software/salmon-1.10.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="samtools"><a href="http://sourceforge.net/projects/samtools/"><strong>SAMtools</strong></a></td>
      <td>Tools for manipulating SAM/BAM files.</td>
      <td><code>1.20</code></td>
      <td><code>software/samtools-1.20</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="skesa"><a href="https://github.com/ncbi/SKESA"><strong>skesa</strong></a></td>
      <td>Short read assembler.</td>
      <td><code>2.4.0</code></td>
      <td><code>software/skesa-2.4.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="snpeff"><a href="https://pcingola.github.io/SnpEff"><strong>snpeff</strong></a></td>
      <td>Annotates and predicts effects of genetic variants.</td>
      <td><code>5.2f</code></td>
      <td><code>software/snpeff-5.2f</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="spades"><a href="http://cab.spbu.ru/software/spades/"><strong>SPADES</strong></a></td>
      <td>Genome assembler for short-read sequencing data.</td>
      <td><code>4.0.0</code></td>
      <td><code>software/SPAdes-4.0.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="sratoolkit"><a href="https://github.com/ncbi/sra-tools"><strong>sratoolkit</strong></a></td>
      <td>SRA data tools.</td>
      <td><code>3.1.1</code></td>
      <td><code>software/sratoolkit-3.1.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="star"><a href="https://github.com/alexdobin/STAR"><strong>STAR</strong></a></td>
      <td>RNA-seq aligner for high-throughput sequencing data.</td>
      <td><code>2.7.11b</code></td>
      <td><code>software/STAR-2.7.11b</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="star-fusion"><a href="https://github.com/STAR-Fusion/STAR-Fusion"><strong>star-fusion</strong></a></td>
      <td>Identify candidate fusion transcripts supported by Illumina reads.</td>
      <td><code>1.15.0</code></td>
      <td><code>software/star-fusion-1.15.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="subread"><a href="https://subread.sourceforge.net/"><strong>subread</strong></a></td>
      <td>Next-gen sequencing read data processing.</td>
      <td><code>2.0.6</code></td>
      <td><code>software/subread-2.0.6</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="trim galore"><a href="https://github.com/FelixKrueger/TrimGalore"><strong>Trim Galore</strong></a></td>
      <td>Wrapper tool for quality and adapter trimming.</td>
      <td><code>0.6.10</code></td>
      <td><code>software/TrimGalore-0.6.10</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="trimal"><a href="https://trimal.cgenomics.org/"><strong>trimal</strong></a></td>
      <td>Removal of spurious sequences or poorly aligned regions from a multiple sequence alignment.</td>
      <td><code>1.5</code></td>
      <td><code>software/trimal-1.5</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="trimmomatic"><a href="https://github.com/usadellab/Trimmomatic"><strong>Trimmomatic</strong></a></td>
      <td>Trims adapters and low-quality bases from sequencing reads.</td>
      <td><code>0.40-rc1</code></td>
      <td><code>software/Trimmomatic-0.40-rc1</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="trinity"><a href="https://github.com/trinityrnaseq/trinityrnaseq"><strong>trinity</strong></a></td>
      <td>RNA-Seq de novo transcriptome assembly.</td>
      <td><code>2.15.2</code></td>
      <td><code>software/trinity-2.15.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="trinotate"><a href="https://github.com/Trinotate/Trinotate/releases"><strong>Trinotate</strong></a></td>
      <td>Transcriptome and protein data search.</td>
      <td><code>4.0.2</code></td>
      <td><code>software/Trinotate-4.0.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="vcftools"><a href="https://vcftools.github.io/"><strong>vcftools</strong></a></td>
      <td>Tools for working with VCF files.</td>
      <td><code>0.1.16</code></td>
      <td><code>software/vcftools-0.1.16</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="vep"><a href="https://www.ensembl.org/info/docs/tools/vep"><strong>vep</strong></a></td>
      <td>Variant Effect Predictor.</td>
      <td><code>default</code></td>
      <td><code>software/vep</code></td>
    </tr>
    <tr>
      <td data-sort-value="bioinformatics and genomics">Bioinformatics and genomics</td>
      <td data-sort-value="vsearch"><a href="https://github.com/torognes/vsearch"><strong>vsearch</strong></a></td>
      <td>Sequence search and detection.</td>
      <td><code>2.30.0</code></td>
      <td><code>software/vsearch-2.30.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="freesurfer"><a href="https://surfer.nmr.mgh.harvard.edu/"><strong>freesurfer</strong></a></td>
      <td>Structural and Functional Neuroimaging data.</td>
      <td><code>5.3.0</code><br><code>7.4.1</code></td>
      <td><code>software/freesurfer-5.3.0</code><br><code>software/freesurfer-7.4.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="fsl"><a href="https://fsl.fmrib.ox.ac.uk/"><strong>FSL</strong></a></td>
      <td>Analysis tools for FMRI MRI and diffusion brain imaging data.</td>
      <td><code>6.0.7.12</code></td>
      <td><code>software/fsl-6.0.7.12</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="jags"><a href="https://mcmc-jags.sourceforge.io/"><strong>jags</strong></a></td>
      <td>Bayesian hierarchical model analysis.</td>
      <td><code>4.3.1</code></td>
      <td><code>software/jags-4.3.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="julia"><a href="https://julialang.org/"><strong>julia</strong></a></td>
      <td>Julia compiler.</td>
      <td><code>1.10.3</code><br><code>1.12.1</code></td>
      <td><code>compilers/julia-1.10.3</code><br><code>compilers/julia-1.12.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="mathematica"><a href="https://www.wolfram.com/mathematica/"><strong>mathematica</strong></a></td>
      <td>Symbolic mathematics, numerical analysis, data visualization, and programming in an interactive notebook environment.</td>
      <td><code>14.0</code></td>
      <td><code>software/mathematica-14.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="matlab"><a href="https://www.mathworks.com/products/matlab.html"><strong>MATLAB</strong></a></td>
      <td>Numerical computing environment and programming platform.</td>
      <td><code>R2022b</code><br><code>R2023a</code><br><code>R2024b</code></td>
      <td><code>software/matlab-R2022b</code><br><code>software/matlab-R2023a</code><br><code>software/matlab-R2024b</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="paraview"><a href="https://www.paraview.org/"><strong>ParaView</strong></a></td>
      <td>Scientific data visualisation tool.</td>
      <td><code>5.12.1</code></td>
      <td><code>software/Paraview-5.12.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="quarto"><a href="https://quarto.org/"><strong>quarto</strong></a></td>
      <td>Scientific and technical publishing system.</td>
      <td><code>1.6.40</code></td>
      <td><code>software/quarto-1.6.40</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="r"><a href="http://www.r-project.org/"><strong>R</strong></a></td>
      <td>Statistical computing environment and programming language.</td>
      <td><code>4.3.3</code><br><code>4.3.3-usr</code><br><code>4.4.3</code><br><code>4.5.2</code></td>
      <td><code>R/R-4.3.3</code><br><code>R/R-4.3.3-usr</code><br><code>R/R-4.4.3</code><br><code>R/R-4.5.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="rstudio"><a href="https://docs.posit.co/ide/user/"><strong>RStudio</strong></a></td>
      <td>Integrated development environment for R.</td>
      <td><code>2025.05.1</code></td>
      <td><code>software/RStudio-2025.05.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="tortoise-gpu"><a href="https://github.com/QMICodeBase/TORTOISEV4"><strong>tortoise-gpu</strong></a></td>
      <td>CUDA enabled Diffusion MRI Processing Pipeline.</td>
      <td><code>4.1</code></td>
      <td><code>software/tortoise-gpu-4.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="data analysis, publishing and visualisation">Data analysis, publishing and visualisation</td>
      <td data-sort-value="vmd"><a href="https://www.ks.uiuc.edu/Research/vmd/"><strong>VMD</strong></a></td>
      <td>Molecular visualisation and analysis software for structures and simulation trajectories.</td>
      <td><code>1.9.3</code></td>
      <td><code>software/vmd-1.9.3</code></td>
    </tr>
    <tr>
      <td data-sort-value="earth, climate and geospatial">Earth, climate and geospatial</td>
      <td data-sort-value="cdo"><a href="https://code.mpimet.mpg.de/projects/cdo/wiki"><strong>CDO</strong></a></td>
      <td>A large tool set for working on climate and NWP model data.</td>
      <td><code>2.5.0</code></td>
      <td><code>software/cdo-2.5.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="earth, climate and geospatial">Earth, climate and geospatial</td>
      <td data-sort-value="gmstar"><a href="https://topex.ucsd.edu/gmtsar"><strong>gmstar</strong></a></td>
      <td>InSAR processing system</td>
      <td><code>6.2</code></td>
      <td><code>software/gmstar-6.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="earth, climate and geospatial">Earth, climate and geospatial</td>
      <td data-sort-value="snap"><a href="https://step.esa.int/main/download/snap-download/"><strong>snap</strong></a></td>
      <td>Earth Observation processing.</td>
      <td><code>8.0</code><br><code>9.0</code></td>
      <td><code>software/snap-8.0</code><br><code>software/snap-9.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="engineering and simulation">Engineering and simulation</td>
      <td data-sort-value="abaqus"><a href="https://discover.3ds.com/"><strong>abaqus</strong></a></td>
      <td>Finite element analysis software.</td>
      <td><code>6.14</code><br><code>2024</code><br><code>2025</code></td>
      <td><code>software/abaqus-6.14</code><br><code>software/abaqus-2024</code><br><code>software/abaqus-2025</code></td>
    </tr>
    <tr>
      <td data-sort-value="engineering and simulation">Engineering and simulation</td>
      <td data-sort-value="ansys"><a href="https://ansys.com/"><strong>ansys</strong></a></td>
      <td>Engineering simulation software suite.</td>
      <td><code>2023R1-v231</code><br><code>2024R1-v241</code><br><code>2025R1-v251</code><br><code>2025R2-v252</code></td>
      <td><code>software/ansys-2023R1-v231</code><br><code>software/ansys-2024R1-v241</code><br><code>software/ansys-2025R1-v251</code><br><code>software/ansys-2025R2-v252</code></td>
    </tr>
    <tr>
      <td data-sort-value="engineering and simulation">Engineering and simulation</td>
      <td data-sort-value="dealii"><a href="https://www.gidsimulation.com"><strong>dealii</strong></a></td>
      <td>A C++ software library supporting the creation of finite element codes.</td>
      <td><code>9.3.3</code></td>
      <td><code>software/dealii-9.3.3</code></td>
    </tr>
    <tr>
      <td data-sort-value="engineering and simulation">Engineering and simulation</td>
      <td data-sort-value="dualsphysics"><a href="https://dual.sphysics.org/"><strong>DualSPHysics</strong></a></td>
      <td>Smoothed Particle Hydrodynamics model.</td>
      <td><code>v5.4</code></td>
      <td><code>software/DualSPHysics_v5.4</code></td>
    </tr>
    <tr>
      <td data-sort-value="engineering and simulation">Engineering and simulation</td>
      <td data-sort-value="gid-simulation"><a href="pre and post processor for numerical simulations in science and engineering."><strong>gid-simulation</strong></a></td>
      <td>Pre- and post processor for numerical simulations in science and engineering.</td>
      <td><code>17.1.5d</code></td>
      <td><code>software/gid-simulation-17.1.5d</code></td>
    </tr>
    <tr>
      <td data-sort-value="engineering and simulation">Engineering and simulation</td>
      <td data-sort-value="ls-dyna"><a href="https://www.ansys.com/products/structures/ansys-ls-dyna"><strong>ls-dyna</strong></a></td>
      <td>Finite element simulation.</td>
      <td><code>2024R1</code><br><code>2025R1</code></td>
      <td><code>software/ls-dyna-2024R1</code><br><code>software/ls-dyna-2025R1</code></td>
    </tr>
    <tr>
      <td data-sort-value="hpc, parallel computing and workflows">HPC, parallel computing and workflows</td>
      <td data-sort-value="gnu-parallel"><a href="https://docs.hpc.qmul.ac.uk/apps/general/gnuparallel/"><strong>gnu-parallel</strong></a></td>
      <td>A shell tool for executing jobs in parallel using one or more computers.</td>
      <td><code>20240922</code></td>
      <td><code>software/gnu-parallel-20240922</code></td>
    </tr>
    <tr>
      <td data-sort-value="hpc, parallel computing and workflows">HPC, parallel computing and workflows</td>
      <td data-sort-value="load-test"><strong>load-test</strong></td>
      <td>—</td>
      <td><code>default</code></td>
      <td><code>software/load-test</code></td>
    </tr>
    <tr>
      <td data-sort-value="hpc, parallel computing and workflows">HPC, parallel computing and workflows</td>
      <td data-sort-value="mpich"><a href="http://www.mpich.org/"><strong>MPICH</strong></a></td>
      <td>Message Passing Interface for parallel software.</td>
      <td><code>4.3.0b1</code></td>
      <td><code>mpi/mpich-4.3.0b1</code></td>
    </tr>
    <tr>
      <td data-sort-value="hpc, parallel computing and workflows">HPC, parallel computing and workflows</td>
      <td data-sort-value="nextflow"><a href="https://www.nextflow.io/"><strong>Nextflow</strong></a></td>
      <td>Workflow manager for reproducible computational pipelines.</td>
      <td><code>23.04.3</code><br><code>24.10.0</code><br><code>25.04.7</code><br><code>25.10.2</code></td>
      <td><code>software/nextflow-23.04.3</code><br><code>software/nextflow-24.10.0</code><br><code>software/nextflow-25.04.7</code><br><code>software/nextflow-25.10.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="hpc, parallel computing and workflows">HPC, parallel computing and workflows</td>
      <td data-sort-value="openmpi"><a href="https://www.open-mpi.org/"><strong>OPENMPI</strong></a></td>
      <td>Implementation of the MPI standard for parallel computing.</td>
      <td><code>4.0.5</code><br><code>4.0.5a</code><br><code>4.1.6</code><br><code>5.0.3</code></td>
      <td><code>mpi/openmpi-4.0.5</code><br><code>mpi/openmpi-4.0.5a</code><br><code>mpi/openmpi-4.1.6</code><br><code>mpi/openmpi-5.0.3</code></td>
    </tr>
    <tr>
      <td data-sort-value="physics, chemistry and materials">Physics, chemistry and materials</td>
      <td data-sort-value="castep"><a href="https://www.castep.org/"><strong>castep</strong></a></td>
      <td>Tool for calculating the properties of materials from first principles.</td>
      <td><code>21.11</code></td>
      <td><code>software/castep-21.11</code></td>
    </tr>
    <tr>
      <td data-sort-value="physics, chemistry and materials">Physics, chemistry and materials</td>
      <td data-sort-value="gromacs"><a href="https://www.gromacs.org/"><strong>gromacs</strong></a></td>
      <td>Molecular dynamics simulation package.</td>
      <td><code>2024.2</code></td>
      <td><code>software/gromacs-2024.2</code></td>
    </tr>
    <tr>
      <td data-sort-value="physics, chemistry and materials">Physics, chemistry and materials</td>
      <td data-sort-value="jewel"><a href="https://jewel.hepforge.org/"><strong>jewel</strong></a></td>
      <td>A Monte Carlo event generator simulating QCD jet evolution in heavy-ion collisions.</td>
      <td><code>2.4.0</code></td>
      <td><code>software/jewel-2.4.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="physics, chemistry and materials">Physics, chemistry and materials</td>
      <td data-sort-value="namd"><a href="http://www.ks.uiuc.edu/Research/namd"><strong>NAMD</strong></a></td>
      <td>Molecular dynamics simulation package.</td>
      <td><code>2.14-smp-CUDA</code><br><code>3.0.1-smp-CUDA</code></td>
      <td><code>software/NAMD-2.14-smp-CUDA</code><br><code>software/NAMD-3.0.1-smp-CUDA</code></td>
    </tr>
    <tr>
      <td data-sort-value="physics, chemistry and materials">Physics, chemistry and materials</td>
      <td data-sort-value="pythia"><a href="https://www.pythia.org/"><strong>pythia</strong></a></td>
      <td>Program for the generation of high-energy physics collision events.</td>
      <td><code>8317</code></td>
      <td><code>software/pythia-8317</code></td>
    </tr>
    <tr>
      <td data-sort-value="physics, chemistry and materials">Physics, chemistry and materials</td>
      <td data-sort-value="vasp"><a href="https://www.vasp.at/"><strong>VASP</strong></a></td>
      <td>Electronic structure and materials modelling software.</td>
      <td><code>6.3.0-vtst</code><br><code>6.4.3</code></td>
      <td><code>software/vasp-6.3.0-vtst</code><br><code>software/vasp-6.4.3</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="autoconf"><a href="https://hpc.guix.info/package/autoconf"><strong>autoconf</strong></a></td>
      <td>A set of M4 macros which expand into shell code to test the features of Unix-like systems.</td>
      <td><code>2.71</code></td>
      <td><code>tools/autoconf-2.71</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="boost"><a href="https://www.boost.org/libraries/latest/grid/"><strong>boost</strong></a></td>
      <td>a general-purpose, high-level C++ template metaprogramming framework of compile-time algorithms, sequences and metafunctions.</td>
      <td><code>1.86.0</code></td>
      <td><code>tools/boost-1.86.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="gcc"><a href="https://gcc.gnu.org/"><strong>GCC</strong></a></td>
      <td>Compiler suite for C, C++, and Fortran.</td>
      <td><code>11.2.0</code><br><code>12.3.0</code><br><code>14.3.0</code></td>
      <td><code>compilers/gcc-11.2.0</code><br><code>compilers/gcc-12.3.0</code><br><code>compilers/gcc-14.3.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="google-cloud-utils"><strong>google-cloud-utils</strong></td>
      <td>—</td>
      <td><code>default</code></td>
      <td><code>software/google-cloud-utils</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="hdf5"><strong>HDF5</strong></td>
      <td>—</td>
      <td><code>1.14.2-vasp</code><br><code>1.14.6-mpi</code></td>
      <td><code>tools/hdf5-1.14.2-vasp</code><br><code>tools/hdf5-1.14.6-mpi</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="intel-compiler"><a href="https://www.intel.com/content/www/us/en/developer/tools"><strong>intel-compiler</strong></a></td>
      <td>Intel C and Fortran.</td>
      <td><code>2024.2.1</code><br><code>2025.1.0</code></td>
      <td><code>compilers/intel-compiler-2024.2.1</code><br><code>compilers/intel-compiler-2025.1.0</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="intel-compiler-ifort"><strong>intel-compiler-ifort</strong></td>
      <td>—</td>
      <td><code>2024.2.1</code></td>
      <td><code>compilers/intel-compiler-ifort-2024.2.1</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="java"><a href="https://www.oracle.com/za/java/"><strong>java</strong></a></td>
      <td>General-purpose programming language and runtime environment.</td>
      <td><code>17</code><br><code>21</code></td>
      <td><code>java/java-17</code><br><code>java/java-21</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="miniconda3"><a href="https://docs.conda.io/en/latest/miniconda.html"><strong>miniconda3</strong></a></td>
      <td>Python distribution and environment manager.</td>
      <td><code>py3.9</code><br><code>py3.12</code><br><code>py3.12-usr</code></td>
      <td><code>python/miniconda3-py3.9</code><br><code>python/miniconda3-py3.12</code><br><code>python/miniconda3-py3.12-usr</code></td>
    </tr>
    <tr>
      <td data-sort-value="programming and development">Programming and development</td>
      <td data-sort-value="vs code"><a href="https://code.visualstudio.com/"><strong>VS Code</strong></a></td>
      <td>An integrated development environment.</td>
      <td><code>4.103.0</code><br><code>4.105.1</code></td>
      <td><code>software/Vscode-4.103.0</code><br><code>software/Vscode-4.105.1</code></td>
    </tr>
  </tbody>
</table>
</div>


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
