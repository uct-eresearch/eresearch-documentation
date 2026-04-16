# UCT eResearch Documentation

Research computing, software, data, and infrastructure guidance at the University of Cape Town.

→ **View the documentation:** https://uct-eresearch.github.io/eresearch-documentation/

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

- **Tasks** — what you want to do  
- **How-to** — how to do one thing  
- **Services** — what each service is for  
- **Reference** — factual system information  
- **Tutorials** — how steps fit together  

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

You can contribute by:

- fixing errors or unclear guidance  
- improving how-to steps  
- adding tutorials based on real workflows  
- identifying gaps in documentation  

→ **Contribute on GitHub:** https://github.com/uct-eresearch/eresearch-documentation

For contribution guidelines:

→ See [CONTRIBUTING.md](CONTRIBUTING.md)

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