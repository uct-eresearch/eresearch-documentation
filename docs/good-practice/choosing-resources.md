# Choosing resources for your job

This page helps you decide how much CPU, memory, and time to request when running jobs on the HPC cluster.

---

## Why resource selection matters

The resources you request determine:

- how long your job waits in the queue  
- whether your job runs successfully  
- how efficiently the cluster is used  

Requesting too many resources can delay your job unnecessarily.  
Requesting too few can cause your job to fail.

---

## Start with your workload

Before choosing resources, consider:

- Is your job **single-threaded** or **parallel**?  
- How much **data** does it process?  
- Does it require **high memory**?  
- Does it use a **GPU**?  

Your resource request should match how your software behaves.

---

## CPU: how many cores?

### Use a single core if:
- your code does not support parallel execution  
- you are running simple or lightweight tasks  

### Use multiple cores if:
- your software supports parallel processing (e.g. MPI, multithreading)  
- the workload can be divided across cores  

Be aware:

- More cores do not automatically make jobs faster  
- Some jobs see little or no benefit from additional cores  

---

## Nodes vs cores

A node is a physical machine. Each node contains multiple cores.

- Most jobs should run on **a single node**  
- Request multiple nodes only if:
  - your software supports distributed computing (e.g. MPI)  

Using multiple nodes unnecessarily can:
- reduce performance  
- increase queue time  
- waste resources  

---

## Memory: how much RAM?

Memory requirements depend on:

- dataset size  
- algorithm complexity  
- number of processes  

If your job runs out of memory:
- it will be terminated  

Strategies:

- Increase memory if your job fails due to memory limits  
- Avoid over-requesting memory, as this may delay scheduling  

→ Learn more:  
[Memory and CPU allocation](../../reference/hpc/memory-and-cpu-allocation.md)

---

## Time: how long will the job run?

You must estimate how long your job will take.

- Shorter jobs are easier for the scheduler to place  
- Overestimating time can increase queue delays  
- Underestimating time can cause jobs to stop prematurely  

A good approach:

- Start with a conservative estimate  
- Refine based on actual runtime  

---

## GPUs (if applicable)

Request a GPU only if your software requires it.

- GPU resources are limited  
- Jobs requesting GPUs may wait longer in the queue  

---

## Common mistakes

### Requesting too many cores
- Does not improve performance for non-parallel jobs  
- Increases queue time  

### Using multiple nodes unnecessarily
- Can slow down jobs due to communication overhead  

### Underestimating memory
- Leads to job termination  

### Overestimating runtime
- Reduces scheduling efficiency  
- Delays job start  

---

## Practical strategy

For new workflows:

1. Start small:
   - single node  
   - few cores  
   - moderate memory  

2. Test your job:
   - observe runtime and memory usage  

3. Adjust:
   - increase resources only where needed  

---

## Key concepts at a glance

- Match resources to how your software actually runs  
- More resources ≠ faster jobs  
- Use multiple nodes only when necessary  
- Accurate time estimates improve scheduling  
- Iteration is part of efficient HPC use  

---

## Related pages

- **Memory and CPU allocation**  
  → [Memory and CPU allocation](../../reference/hpc/memory-and-cpu-allocation.md)

- **Scheduler and queues**  
  → [Scheduler and queues](../../reference/hpc/scheduler-and-queues.md)

- **Submit a job**  
  → [Submit a job](../../how-to/hpc/submit-a-job.md)