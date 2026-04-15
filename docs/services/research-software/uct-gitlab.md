# UCT GitLab

## What this service is

UCT GitLab is a centrally managed platform for version control, collaboration, and project management of research software and code.

It is provided by ICTS and enables researchers to:
- store and manage code in version-controlled repositories
- collaborate with others on software and computational workflows
- track work through issues and project planning tools
- document and organise research software projects

GitLab is based on Git, a widely used version control system.

---

## Who this is for

UCT GitLab is suitable for researchers who:

- develop or use code as part of their research
- collaborate with others on computational work
- need to track and manage changes to code over time
- want to organise projects in a structured and reproducible way

It is commonly used in:
- data science and machine learning
- bioinformatics and computational biology
- engineering and simulation workflows
- collaborative research software projects

---

## What GitLab provides

### Version control (Git)

GitLab allows you to:
- track changes to code over time
- maintain a complete history of your work
- revert to earlier versions if needed
- work on different versions of a project using branches

This supports reproducibility and safe experimentation.

---

### Collaboration and access control

- projects can be private or shared
- collaborators can be added with controlled permissions
- access is managed using UCT credentials

This enables secure collaboration within and across research teams.

---

### Merge requests (code review)

GitLab supports structured collaboration through merge requests:

- propose and review changes before integrating them
- discuss and refine contributions
- maintain quality and transparency in shared codebases

---

### Issue tracking and project management

Each project can include:
- issue tracking (tasks, bugs, ideas)
- milestones and planning tools

This helps teams:
- organise work
- track progress
- coordinate contributions

---

### Documentation

Projects can include:
- README files (project overview and instructions)
- wikis for extended documentation

This supports onboarding, reuse, and long-term sustainability of research software.

---

## How GitLab works

GitLab uses a repository-based workflow:

- each project has a repository (a version-controlled folder)
- work is typically done locally (on your machine or HPC)
- changes are committed and pushed to GitLab
- collaborators contribute through branches and merge requests

---

## What GitLab supports

GitLab is designed for:

- managing research code
- collaborative software development
- documenting computational workflows
- tracking project evolution over time

It plays a central role in reproducible research workflows.

---

## What GitLab does not provide

GitLab should be used alongside other services:

- not designed for large data storage  
  → use RDS for datasets  

- not a compute environment  
  → use HPC to run analyses  

- not a data transfer platform  
  → use Nextcloud or Globus for sharing and transfer  

---

## How GitLab fits with other services

GitLab is part of a broader research workflow at UCT:

- **GitLab** → manage code and workflows  
- **RDS (Research Data Store)** → store research data  
- **HPC** → run computational analyses  
- **Data transfer tools** → move data between systems  

Together, these enable:
- reproducibility
- collaboration
- scalable research workflows

---

## When to use GitLab

Use GitLab when:

- you are writing or maintaining code
- you are collaborating on software or analysis workflows
- you want to track changes and maintain version history
- your work needs to be reproducible and well-documented

If you are unsure:
→ [Choose the right service](../../start-here/choose-the-right-service.md)

---

## Get started

To begin using GitLab:

- create a new project (repository)
- add your code or project files
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
- use clear and meaningful commit messages
- organise projects into logical structures
- document your workflows (README, wiki)
- use branches for new features or experiments

→ See: [Project structure](../../good-practice/project-structure.md)

---

## Need help?

- → [Support](../../support/index.md)