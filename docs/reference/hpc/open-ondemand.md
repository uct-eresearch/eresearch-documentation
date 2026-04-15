# Open OnDemand (web-based HPC access)

## Overview

Open OnDemand provides a browser-based interface to UCT HPC.

It allows you to:

- access HPC through a web browser
- launch graphical applications without SSH configuration
- run interactive sessions on compute nodes
- manage files directly through a web interface

This represents a shift toward more **accessible HPC workflows**, reducing reliance on command-line interaction.

---

## What Open OnDemand provides

Through Open OnDemand, you can:

- launch interactive desktop sessions
- run applications such as:
  - Jupyter notebooks
  - RStudio Server
  - MATLAB
  - VS Code (server-based)
- open terminal sessions on compute nodes
- browse, upload, and download files

All applications still run on **HPC compute nodes**, not on your local machine.

---

## Key concept

Open OnDemand does not replace HPC scheduling.

Instead, it:

- requests resources on your behalf
- launches sessions on compute nodes
- manages those sessions through the browser

This means:

- you are still using the scheduler
- resource limits still apply
- sessions consume allocated compute time

---

## When to use Open OnDemand

Use Open OnDemand when:

- you need a graphical interface
- you are new to HPC
- you want a simpler way to run interactive workflows
- you need persistent sessions you can reconnect to
- you want to avoid SSH/X11 setup

---

## Session behaviour

Open OnDemand sessions are:

- **interactive** — you work in real time
- **stateful** — you can disconnect and reconnect
- **resource-bound** — limited by requested CPU, memory, and time

Always remember:

- sessions consume HPC resources
- long-running sessions should be used carefully

---

## Relationship to other workflows

Open OnDemand complements, rather than replaces:

- batch jobs (for large-scale computation)
- command-line workflows (for automation and scripting)

Typical usage patterns:

- exploratory analysis → Open OnDemand  
- production runs → batch jobs  
- debugging → interactive sessions  

---

## Limitations

Open OnDemand is not ideal for:

- very large-scale parallel jobs
- highly automated pipelines
- workflows that require full control over scheduling

In these cases, use standard batch job submission.

---

## Good practice

- use Open OnDemand for interactive and exploratory work
- avoid leaving sessions running unnecessarily
- match requested resources to actual needs
- move stable workflows into batch jobs

---

## When to ask for help

Contact HPC support if:

- an application you need is not available
- sessions fail to start
- performance is consistently poor
- you are unsure how to map your workflow to Open OnDemand

---

## Related pages

- Graphical applications → `Reference > HPC`
- Scheduler and job submission → `Reference > HPC`
- Software and modules → `Reference > HPC`
- Submit your first job → `How-to > HPC`