# Memory and CPU allocation

This page explains how CPU and memory resources are allocated on the HPC cluster and how they affect your jobs.

---

## How resources are allocated

When you submit a job, you request compute resources from the scheduler:

- **CPU cores** → processing power  
- **Memory (RAM)** → working space for your job  

These resources are allocated on worker nodes and are reserved for the duration of your job.

---

## CPU cores and tasks

In SLURM:

- `ntasks` specifies the number of CPU cores allocated to a job  
- Each task typically corresponds to one processing thread  

Key points:

- More cores do not automatically make a job faster  
- Performance depends on whether your software can use multiple cores  
- Some jobs run efficiently on a single core  

---

## Memory allocation

Memory is allocated relative to CPU usage.

- Each worker node has a fixed amount of RAM  
- Memory is distributed across cores  
- The available memory for your job depends on how resources are requested  

Two common approaches:

- Request memory explicitly (e.g. `mem-per-cpu`)  
- Request additional cores to increase available memory  

---

## Memory per core

On most nodes, memory is approximately proportional to the number of cores.

Example:

- A node with 40 cores and 384 GB RAM  
- Approximate ratio: **~9 GB per core**

This means:

- 1 core → ~9 GB RAM  
- 2 cores → ~18 GB RAM  
- 5 cores → ~45 GB RAM  

This ratio may vary between partitions.

---

## What happens if memory is exceeded

If a job uses more memory than allocated:

- The job is automatically terminated  
- Output may be incomplete or lost  

Memory-related failures are a common cause of job crashes.

---

## Choosing between cores and memory

There is a trade-off between CPU and memory:

- Increasing cores:
  - increases available memory  
  - may not improve performance if the code is not parallel  

- Requesting memory explicitly:
  - gives more control  
  - avoids unnecessary CPU allocation  

The appropriate choice depends on your workload.

---

## Multi-node considerations

For jobs using multiple nodes:

- Memory is distributed across nodes  
- Each node provides its own CPU and memory allocation  

Using multiple nodes does not combine memory into a single pool unless the software is designed for distributed computing.

---

## Key concepts at a glance

- CPU cores control **compute capacity**  
- Memory controls **how much data your job can process at once**  
- Memory is often tied to the number of cores requested  
- Exceeding memory limits will terminate your job  
- Resource choices should match your software’s behaviour  

---

## Related pages

- **Choosing resources**  
  → [Choosing resources](../../good-practice/hpc/choosing-resources.md)

- **Scheduler and queues**  
  → [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)

- **Submit a job**  
  → [Submit a job](../../how-to/hpc/submit-a-job.md)