# High Performance Computing (HPC)

## What this service is

The UCT High Performance Computing (HPC) service is a shared computing cluster designed to support data-intensive and computationally demanding research.

It provides access to:
- large-scale compute resources (CPUs, GPUs, high-memory nodes)
- parallel processing capabilities
- a controlled, multi-user research environment

HPC allows you to run analyses that would be too slow or impossible on a personal computer.

---

## Who this is for

HPC is suitable for researchers who:

- work with large datasets
- run long or computationally intensive analyses
- need parallel processing or batch execution
- require specialised resources (e.g. GPUs, large RAM)

It is commonly used in:
- bioinformatics
- engineering and physics simulations
- machine learning and AI workflows
- data science and large-scale statistical analysis

---

## How HPC works at UCT

The HPC system is a **cluster-based environment** made up of:

- a **login (head) node**  
  → where you connect and prepare your work

- multiple **compute (worker) nodes**  
  → where your jobs are executed

- a **job scheduler** (e.g. SLURM)  
  → manages how jobs are queued and run across the cluster

You do not run analysis directly on the login node.  
Instead, you submit jobs to the scheduler, which allocates resources and runs them on available compute nodes.

---

## How work is done

HPC uses a **job-based workflow**, not an interactive one.

Typical workflow:

1. Connect to the cluster via SSH  
2. Prepare a job script (resources + commands)  
3. Submit the job to the scheduler  
4. The system runs the job when resources are available  
5. Results are written to output files  

This allows:
- efficient use of shared resources
- reproducible and scalable workflows
- unattended execution of long-running jobs

---

## Storage on HPC

HPC provides two main types of storage:

### `/home`
- small, persistent storage
- used for scripts, configuration, and small files
- limited quota

---

### `/scratch`
- high-performance temporary storage
- used during active computation
- not intended for long-term storage
- **not backed up**

---

### When to use external storage (RDS)

For most research workflows, you should use HPC together with the Research Data Store (RDS):

Use RDS when:
- your data is large or long-lived
- you need reliable storage between jobs
- you exceed HPC storage limits

RDS can be mounted on HPC and provides:
- persistent storage
- backup and recovery
- high-performance access

→ See: [Research data storage](../storage/index.md)

---

## What HPC supports

The HPC service supports:

- batch job execution via scheduler
- parallel computing (multi-core, distributed jobs)
- GPU workloads
- custom research software environments
- command-line workflows (Linux-based)

Researchers can:
- install and run their own software (within guidelines)
- automate workflows through scripts
- scale analyses across multiple nodes

---

## What HPC does not provide

It is important to understand what HPC is not:

- not a desktop environment  
- not designed for interactive, GUI-based work  
- not a storage service for long-term data  
- not suitable for small, lightweight tasks  

If your work fits comfortably on a laptop or workstation, HPC is not necessary.

---

## Constraints and responsibilities

Because HPC is a shared resource:

- jobs must be submitted through the scheduler  
- heavy computation on login nodes is not allowed  
- resources (CPU, memory, time) must be requested appropriately  
- inefficient use of resources affects other users  

Researchers are expected to:
- test jobs on small datasets first
- request only the resources they need
- structure workflows for batch execution

---

## How HPC fits with other services

HPC is most effective when used together with other UCT services:

- **RDS (Research Data Store)**  
  → for storing and managing large datasets

- **GitLab**  
  → for version control and collaboration on code

- **Data transfer tools (e.g. Globus, Nextcloud)**  
  → for moving data to and from the cluster

These services work together as part of a complete research workflow.

---

## When to use HPC

Use HPC when:
- your analysis is too slow or large for local machines
- you need parallel processing or batch jobs
- your workflow requires GPUs or high-memory nodes

If you are unsure:
→ [Choose the right service](../../start-here/choose-the-right-service.md)

---

## Get started

To begin using HPC:

- → [Log into HPC](../../how-to/hpc/log-into-hpc.md)  
- → [Submit your first job](../../how-to/hpc/submit-your-first-job.md)

---

## Related tasks

- → [Run large-scale analysis](../../tasks/run-large-scale-analysis.md)  
- → [Store and share research data](../../tasks/store-and-share-research-data.md)

---

## Need help?

- → [Support](../../support/index.md)