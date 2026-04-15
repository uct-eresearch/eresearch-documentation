# Scheduler and job submission

## How jobs run on UCT HPC

The UCT HPC system uses a scheduler to manage how computational work is executed across shared resources.

Instead of running code directly, you submit **jobs** to the scheduler, which then:
- queues your work
- allocates resources
- runs your job on an available compute node

---

## Key concepts

### Job

A **job** is a unit of work submitted to the scheduler.

A job typically includes:
- the commands or script to run
- the resources required, such as CPUs, memory, and time
- optional output and error handling

---

### Job script

A **job script** is a file that defines how your job should run.

It usually includes:
- scheduler directives for resource requests
- commands to execute your code
- environment setup such as loading modules

---

### Scheduler

The scheduler is responsible for:
- managing job queues
- deciding when jobs run
- allocating compute resources fairly across users

At UCT, the scheduler is based on **SLURM**.

---

### Queue

Jobs are placed into a **queue** while waiting for resources to become available.

The time a job waits depends on:
- resource availability
- requested resources
- other jobs already in the system

---

### Compute nodes

Jobs run on **compute nodes**, not on the login node.

Compute nodes provide:
- CPUs and memory
- access to storage
- specialised resources such as GPUs, where available

---

## Submitting a job

Jobs are typically submitted using:

```bash
sbatch job_script.sh