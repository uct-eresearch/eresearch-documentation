# Policies and service conditions

## Overview

UCT HPC is a shared institutional resource designed to support research.

Use of the system is governed by policies and service conditions to ensure:

- fair access across users and groups
- system stability and performance
- appropriate use of institutional infrastructure

All users are expected to understand and follow these conditions.

---

## Core principles

Use of HPC is based on the following principles:

- **shared resource** — all users must act in a way that does not negatively impact others  
- **research-focused use** — the system is intended for legitimate research activities  
- **responsible usage** — users are accountable for how they use compute, storage, and software  
- **reproducibility and traceability** — workflows should be structured and documented  

---

## Appropriate use

HPC resources may be used for:

- academic research
- data analysis and modelling
- simulation and computation
- development of research software

HPC should not be used for:

- personal or non-research purposes
- unrelated commercial activities
- activities that violate institutional policies or law

---

## Login node usage

The login (head) node is a **shared access point**, not a compute resource.

Allowed:

- connecting to the system
- editing files
- submitting jobs
- lightweight commands

Not allowed:

- running computational workloads
- running graphical applications
- compiling large software packages
- long-running or resource-intensive processes

Misuse of the login node may result in:

- termination of processes
- temporary or permanent restriction of access

---

## Compute usage

All computational work must be run via:

- batch jobs (scheduled)
- interactive jobs (for development or GUI use)

Users must:

- request appropriate resources (CPU, memory, time)
- avoid over-requesting resources unnecessarily
- release resources when no longer needed

---

## Fair usage

To ensure equitable access:

- jobs may be prioritised or limited by the scheduler
- excessive or inefficient use may be restricted
- users may be contacted if usage patterns affect others

Good practice includes:

- testing jobs on small inputs before scaling
- optimising code before large runs
- avoiding repeated failed jobs

---

## Storage usage

Users are responsible for managing their data.

Expectations:

- store only active and relevant research data
- remove unnecessary or duplicate files
- avoid using HPC storage for long-term archiving (unless designated)

Large or unmanaged datasets may:

- impact system performance
- be subject to cleanup policies

---

## Software and installation

Software environments are shared.

Users must:

- use centrally provided software where appropriate
- avoid modifying shared environments
- install personal packages in user space

Heavy installation or compilation must:

- not be performed on the login node
- be done via interactive jobs

---

## Security and access

Users are responsible for:

- keeping credentials secure
- not sharing accounts
- ensuring appropriate access to data

Do not:

- expose HPC services insecurely
- bypass authentication mechanisms
- run services that create security risks

---

## Data responsibility

Users are responsible for:

- the integrity of their data
- backing up important results where required
- complying with data governance and ethical requirements

HPC systems are not guaranteed backup environments unless explicitly stated.

---

## Monitoring and enforcement

System usage may be monitored to ensure:

- compliance with policies
- system stability
- fair resource allocation

If misuse is detected, actions may include:

- warning or guidance from support staff
- termination of running processes
- temporary suspension of access
- escalation under institutional policies

---

## When to ask for guidance

Contact HPC support if you are unsure about:

- whether a workflow is appropriate
- how to use resources efficiently
- large-scale or unusual workloads
- software installation requirements

Early engagement helps avoid issues.

---

## Good practice summary

- use compute nodes, not the login node
- run jobs through the scheduler
- request appropriate resources
- clean up unused data
- document and structure workflows
- respect that HPC is a shared system

---

## Related pages

- Scheduler and job submission → `Reference > HPC`
- Software and modules → `Reference > HPC`
- Storage and file systems → `Reference > HPC`
- Graphical applications → `Reference > HPC`
- Support → `Support`