# Submit a job

## Overview

Submit a batch job to the HPC system using the scheduler.

Jobs are submitted from the login node and executed on compute nodes.

---

## Before you begin

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- your code or executable is available
- your input data is accessible
- you know roughly how long your job will run
- you have identified required resources  
  (see: [Choosing resources](../../good-practice/hpc/choosing-resources.md))

For background on how jobs are scheduled, see:  
[Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)

!!! warning "Cluster limits apply"
    - Maximum runtime: **7 days**
    - Core limits per user:
        - `ada`: ~320 cores  
        - `curie`: ~640 cores  

    Jobs exceeding these limits will be terminated or delayed.

    See: [Cluster specifications](../../reference/hpc/cluster-specifications.md)


!!! warning "Do not run jobs on the login node"
    The login node is for preparing and submitting jobs only.

    Running compute workloads here may result in your process being terminated.

    Use an [interactive](./run-interactive-jobs.md) or batch job with `sbatch` instead.

!!! warning "Storage limits apply"
    - `/home` has strict quotas  
    - `/scratch` is not backed up  

    See: [Storage and file systems](../../reference/hpc/storage-and-file-systems.md)

---

## Steps

### 1. Log into HPC

```bash
ssh <username>@hpc.uct.ac.za
```

---

### 2. Create a job script

Create a file, for example `job.sh`:

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

### 3. Submit the job

```bash
sbatch job.sh
```

This returns a job ID.

---

### 4. Check job status

```bash
squeue -u $USER
```

---

### 5. View output

```bash
cat logs/job-<jobid>.out
cat logs/job-<jobid>.err
```

---

## After submission

- the job enters the queue
- it runs when resources become available
- output is written to log files

---

## Troubleshooting

**Job not starting**
- check partition and resource requests
- reduce requested resources if too large

**Job fails**
- check `.err` file
- verify modules and paths

**No output**
- confirm script runs locally
- check working directory

---

## Related pages

- [Check job status](check-job-status.md)
- [Cancel a job](cancel-a-job.md)
- [Run interactive jobs](run-interactive-jobs.md)
- [Choosing resources](../../good-practice/hpc/choosing-resources.md)
- [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)