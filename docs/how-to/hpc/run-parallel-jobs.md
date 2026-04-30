# Run parallel jobs

## Overview

Run jobs that use multiple CPU cores or multiple nodes on the HPC system.

Parallel jobs are used for workloads that can execute simultaneously across cores or machines.

---

## When to use parallel jobs

Use parallel jobs when your software:

- can use multiple CPU cores  
- supports multithreading (e.g. OpenMP)  
- supports distributed computing (e.g. MPI)  

If your software is not parallel-aware, requesting more resources will not improve performance.

For background on how resources are allocated and scheduled, see:  
[Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)

---

## Parallel job types

### Single-node parallel jobs

- run on one node  
- use multiple CPU cores  
- suitable for multithreaded applications  

### Multi-node parallel jobs

- run across multiple nodes  
- require MPI or similar frameworks  
- suitable for distributed workloads  


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

### 1. Create a job script

#### Single-node parallel job

```bash
#!/bin/bash
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --job-name=parallel-job

myprogram -n ${SLURM_NTASKS}
```

---

#### Multi-node MPI job

```bash
#!/bin/bash
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --time=02:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --job-name=mpi-job

module load mpi/openmpi

srun my_mpi_program
```

---

### 2. Submit the job

```bash
sbatch job.sh
```

---

### 3. Monitor the job

```bash
squeue -u $USER
```

---

## Key directives

- `--nodes` → number of nodes  
- `--ntasks` → total number of tasks (cores)  
- `--ntasks-per-node` → tasks per node  

Choose resources carefully:  
[Choosing resources](../../good-practice/hpc/choosing-resources.md)

---

## Using environment variables

Match your program to allocated resources:

- `${SLURM_NTASKS}` → total number of tasks  
- `${SLURM_TASKS_PER_NODE}` → tasks per node  

Example:

```bash
myprogram -n ${SLURM_NTASKS}
```

---

## OpenMP jobs

If your program uses OpenMP:

```bash
export OMP_NUM_THREADS=${SLURM_NTASKS}
```

---

## Important notes

- only request multiple nodes if your software supports it  
- more resources do not always mean faster performance  
- multi-node jobs may incur communication overhead  

---

## Troubleshooting

**Job does not scale**
- software may not support parallel execution  
- try fewer cores  

**Poor performance**
- avoid multi-node jobs unless necessary  
- check CPU and memory usage  

---

## Related pages

- [Submit a job](submit-a-job.md)
- [Run interactive jobs](run-interactive-jobs.md)
- [Check job status](check-job-status.md)
- [Choosing resources](../../good-practice/hpc/choosing-resources.md)
- [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)