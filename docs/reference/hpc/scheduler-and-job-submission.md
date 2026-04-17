# Scheduler and job submission (SLURM)

## Overview

UCT HPC uses SLURM to manage how work runs on the system.

Jobs are submitted to a queue and executed on compute nodes.  
Work should not be run directly on the login node.

---

## Key commands

```bash
sbatch job.sh
squeue -u $USER
sacct -j <jobid>
scancel <jobid>
sinfo
```

---

## Partitions

Compute resources are grouped into partitions.

Common partitions include:

- `ada` — general CPU workloads
- `curie` — additional CPU capacity
- `l40s`, `a100` — GPU-enabled nodes

Check current partitions and availability:

```bash
sinfo
```

---

## Job script

```bash
#!/bin/bash
#SBATCH --job-name=my-job
#SBATCH --partition=ada
#SBATCH --cpus-per-task=4
#SBATCH --mem=16G
#SBATCH --time=02:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

module purge
module load python/miniconda3-py3.12

python script.py
```

---

## Resource requests

Each job defines its required resources.

- more resources than needed → longer queue times  
- fewer resources than needed → job failure or reduced performance  

Shorter jobs are often scheduled sooner.

---

## Job lifecycle

1. submit job (`sbatch`)
2. wait in queue
3. run on compute node
4. complete or fail

Check output:

```bash
cat logs/job-<jobid>.out
cat logs/job-<jobid>.err
```

---

## Interactive jobs

Use for short or exploratory work:

```bash
srun --partition=ada --cpus-per-task=2 --mem=8G --time=01:00:00 --pty bash
```

---

## Login node usage

The login node is a shared access point.

Use it for:

- connecting
- editing files
- submitting jobs

Do not use it for:

- running computations
- long-running processes

Processes that impact other users may be terminated.

---

## Good practice

- test jobs with small inputs
- request only what you need
- use logs to diagnose issues