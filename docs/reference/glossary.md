# Glossary

## Common terms in UCT eResearch

This glossary defines key terms used across research computing, data, and software workflows at UCT.

---

## HPC and compute

### High Performance Computing (HPC)
A shared computing environment designed for running large-scale or resource-intensive analyses across multiple compute nodes.

### Cluster
A group of interconnected computers (nodes) that work together to perform computational tasks.

### Login node (head node)
The entry point to the HPC system where users connect, prepare jobs, and manage files. Not intended for heavy computation.

### Compute node (worker node)
A machine within the cluster where jobs are executed.

### Scheduler
A system that manages job queues and allocates compute resources. At UCT, this is based on SLURM.

### Job
A unit of work submitted to the scheduler for execution on the cluster.

### Job script
A file that defines how a job should run, including required resources and commands.

### Partition
A subset of compute resources within the cluster, often grouped by capability (e.g. CPU vs GPU).

### GPU (Graphics Processing Unit)
A specialised processor used for parallel workloads such as machine learning and simulation.

---

## Storage and data

### /home
A user’s personal storage space on HPC for configuration files, code, and small datasets.

### /scratch
High-performance temporary storage used during active computations. Not intended for long-term storage.

### Quota
A limit on the amount of storage a user or project can use.

### Research Data Storage (RDS)
A managed storage service for longer-term research data that needs to be retained and organised.

---

## Access and transfer

### SSH (Secure Shell)
A protocol used to securely connect to remote systems such as HPC.

### SCP (Secure Copy)
A method for copying files between local and remote systems over SSH.

### Rsync
A tool for efficiently transferring and synchronising files between systems.

### Globus
A platform for reliable, high-performance data transfer between storage systems.

### VPN (Virtual Private Network)
A secure connection required for accessing certain UCT services from off-campus.

---

## Software and environments

### Module
A system used on HPC to load and manage software environments.

### Module system
A tool that allows users to dynamically load different software versions (e.g. using `module avail` and `module load`).

### Environment
A configured set of software and dependencies used to run a workflow.

---

## General research computing

### Workflow
A sequence of steps combining code, data, and compute resources to produce research outputs.

### Reproducibility
The ability to run the same workflow again and obtain consistent results.

### Intermediate data
Temporary data generated during processing that may not need to be retained long-term.

---

## Notes

- Terms may appear in multiple sections of the documentation.
- Where needed, pages link back to more detailed explanations in Services or How-to guides.