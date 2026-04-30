# Scheduler and job submission (SLURM)

## Overview

UCT HPC uses a job scheduler called SLURM to manage how work runs on the system.

All computational work is submitted as jobs. These jobs are queued and executed on compute nodes when the required resources become available.

Work should not be run directly on the login node.

---

## What the scheduler does

The scheduler is responsible for coordinating all work on the cluster.

It:

- allocates resources (CPU, memory, GPU)
- decides when and where jobs run
- ensures fair usage across users
- manages queues and priorities

This allows many users to share the system efficiently.

---

## How jobs are scheduled

When a job is submitted:

- it is placed in a queue
- it waits until the requested resources are available
- it runs on a suitable compute node

Jobs do not run immediately unless resources are free.

---

## Partitions (queues)

Compute resources are grouped into partitions (also called queues).

Each partition represents a set of nodes with specific capabilities.

Examples include:

- CPU partitions for general workloads
- GPU partitions for accelerated workloads

Jobs must specify a partition that matches their requirements.

---

## Job lifecycle

All jobs follow the same lifecycle:

1. **Submission** — job is sent to the scheduler  
2. **Pending** — job waits in the queue  
3. **Running** — job executes on compute resources  
4. **Completion** — job finishes successfully or fails  

Output and error logs are written during execution.

---

## Resource allocation

Each job requests a set of resources, such as:

- number of CPU cores
- amount of memory
- number and type of GPUs
- wall time (maximum runtime)

The scheduler uses these requests to determine when and where the job can run.

Accurate resource requests are important:

- requesting more than needed can increase queue time
- requesting too little can cause failures or poor performance

---

## Backfill scheduling

SLURM may run smaller jobs earlier if they can fit into available gaps between larger jobs.

This is known as backfill scheduling.

Providing accurate wall time increases the likelihood that a job can be scheduled sooner.

---

## Job isolation

Each job runs in an isolated allocation of resources:

- dedicated CPU cores
- dedicated memory
- optionally dedicated GPUs

This prevents interference between users and ensures predictable performance.

---

## Login node vs compute nodes

The login node is a shared access point used for:

- connecting to the system
- preparing jobs
- submitting jobs

Compute nodes are used for:

- running all computational work

Running heavy workloads on the login node is not permitted and may result in processes being terminated.

---

## Related pages

- [Submit a job](../../how-to/hpc/submit-a-job.md)
- [Run interactive jobs](../../how-to/hpc/run-interactive-jobs.md)
- [Choosing resources](../../good-practice/hpc/choosing-resources.md)
- [System overview](../../reference/hpc/system-overview.md)