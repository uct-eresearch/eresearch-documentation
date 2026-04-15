# UCT GitLab

## What this service is

UCT GitLab is a platform for managing, sharing, and collaborating on research code and related project materials.

It provides a central place to:
- store and version-control code
- collaborate with others on software development
- track work through issues and tasks
- manage projects in a structured and reproducible way

GitLab is based on **Git**, a distributed version control system widely used in research and software development.

---

## Who this is for

UCT GitLab is suitable for researchers who:

- write or maintain code as part of their research
- collaborate with others on software or data workflows
- want to track changes and maintain a history of their work
- need structured project management (issues, tasks, documentation)

It is commonly used in:
- computational research (e.g. data science, bioinformatics)
- software development projects
- collaborative research teams

---

## What GitLab provides

### Version control (Git)

GitLab allows you to:
- track changes to code over time
- revert to previous versions if needed
- work on different versions of a project (branches)

This supports:
- reproducibility
- safe experimentation
- collaborative development

---

### Collaboration and access control

- projects can be private or shared
- access is controlled at a fine-grained level
- collaborators can be added with different permissions

This ensures:
- secure sharing of code
- controlled collaboration across teams :contentReference[oaicite:0]{index=0}  

---

### Merge requests (code review)

GitLab supports structured collaboration through merge requests:

- propose changes to code
- review and discuss changes before merging
- maintain quality and transparency

---

### Issue tracking and project management

Each project can include:
- issue tracking (tasks, bugs, ideas)
- milestones and planning tools

This helps teams:
- organise work
- track progress
- coordinate contributions :contentReference[oaicite:1]{index=1}  

---

### Documentation (wikis and READMEs)

Projects can include:
- README files (project overview and instructions)
- wikis (extended documentation)

This supports:
- onboarding new collaborators
- documenting workflows and methods

---

## How GitLab works

GitLab uses a **repository-based workflow**:

- each project has a repository (a version-controlled folder)
- changes are made locally and then shared (pushed) to GitLab
- collaborators can contribute through branches and merge requests

Work is typically done:
- locally on your machine or HPC
- then synchronised with GitLab

---

## What GitLab supports

GitLab is designed for:

- managing research code
- collaborative software development
- tracking project changes over time
- documenting computational workflows
- integrating code with analysis environments (e.g. HPC)

---

## What GitLab does not provide

It is important to use GitLab alongside other services:

- not designed for large data storage  
  → use RDS for datasets  

- not a compute environment  
  → use HPC to run analyses  

- not a file-sharing platform for large data  
  → use Nextcloud or data transfer tools  

---

## How GitLab fits with other services

GitLab is part of a broader research workflow:

- **GitLab** → manage code and workflows  
- **RDS (Research Data Store)** → store research data  
- **HPC** → run computational analyses  
- **Data transfer tools** → move data between systems  

Together, these enable:
- reproducible research
- collaborative development
- scalable workflows

---

## When to use GitLab

Use GitLab when:

- you are writing or maintaining code
- you need to collaborate on software
- you want to track changes and maintain version history
- your research involves reproducible computational workflows

If you are unsure:
→ [Choose the right service](../../start-here/choose-the-right-service.md)

---

## Get started

To begin using GitLab:

- create a project (repository)
- add your code
- invite collaborators

→ [Create a GitLab project](../../how-to/research-software/create-a-gitlab-project.md)

---

## Related tasks

- → [Collaborate on code](../../tasks/collaborate-on-code.md)  
- → [Run large-scale analysis](../../tasks/run-large-scale-analysis.md)

---

## Good practice

To use GitLab effectively:

- commit changes regularly
- use clear commit messages
- organise code into structured projects
- document your workflows (README, wiki)
- use branches for new features or experiments

→ See: [Project structure](../../good-practice/project-structure.md)

---

## Need help?

- → [Support](../../support/index.md)