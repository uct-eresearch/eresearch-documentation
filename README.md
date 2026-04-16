# UCT eResearch Documentation

Research computing, software, data, and infrastructure guidance at the University of Cape Town.

→ **View the documentation:** [https://uct-eresearch.github.io/eresearch-documentation/](https://uct-eresearch.github.io/eresearch-documentation/)

---

## What this repository contains

This repository contains the source for the UCT eResearch documentation site.

The documentation helps researchers:

- identify what they need to do  
- choose the right UCT eResearch service  
- take the next step with confidence  

It is designed for **clarity, speed, and execution**.

---

## Documentation structure

The site follows a strict content model:

- **[Tasks](./docs/tasks/index.md)** — what you want to do  
- **[How-to](./docs/how-to/index.md)** — how to do one thing  
- **[Services](./docs/services/index.md)** — what each service is for  
- **[Reference](./docs/reference/index.md)** — factual system information  
- **[Tutorials](./docs/tutorials/index.md)** — how steps fit together  

Each layer has a specific role. Content should not overlap.

---

## Local development

To build the site locally:

```bash
pip install -r requirements.txt
mkdocs serve
```

Then open:

http://127.0.0.1:8000/

---

## Build

To validate changes:

```bash
mkdocs build --strict
```

The `--strict` flag ensures:

- no broken links  
- no invalid navigation  
- no silent errors  

---

## Deployment

The site is deployed automatically via GitHub Actions.

- push to `main` triggers a build  
- the site is published to GitHub Pages  

---

## Contributing

Contributions are welcome.

If something is unclear, missing, or incorrect — you can either let us know by email or creating an issue or by suggesting a fix.

Start here:

→ See [CONTRIBUTING.md](CONTRIBUTING.md)

This explains:

- how to report a problem (issue, email, Service-Now request)
- how to contribute (issue → fork → PR)
- where content belongs
- the rules that must be followed

---

## Scope

This documentation covers:

- high performance computing (HPC)  
- storage  
- data transfer  
- research software  

---

## License

[![CC BY 4.0][cc-by-shield]][cc-by]

This work is licensed under a  
[Creative Commons Attribution 4.0 International License][cc-by].

You are free to:

- share — copy and redistribute the material in any medium or format  
- adapt — remix, transform, and build upon the material  

Under the following terms:

- attribution — give appropriate credit, provide a link to the license, and indicate if changes were made  

[cc-by]: https://creativecommons.org/licenses/by/4.0/
[cc-by-shield]: https://img.shields.io/badge/License-CC%20BY%204.0-lightgrey.svg