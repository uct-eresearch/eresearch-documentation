# Scheduler and queues (SLURM)

## What the scheduler does

SLURM manages how jobs are queued and executed across the cluster.

- Allocates resources (CPU, memory, GPU)
- Ensures fair usage across users
- Decides when and where jobs run

---

## How jobs are scheduled

- Jobs are placed in a queue
- Jobs run when requested resources become available
- Jobs do not run immediately unless resources are free

---

## Why jobs may be delayed

- Resources are currently in use
- Higher-priority jobs are running
- Requested resources are too large

---

## Backfill scheduling

Shorter jobs may run earlier if they can fit into available gaps.

This means:
- specifying accurate wall time can reduce wait time

---

## Job isolation

Each job is allocated dedicated resources:
- CPU cores
- memory
- (optionally) GPUs

This prevents interference between users.

---

## Related pages

- [Submit a job](../../how-to/hpc/submit-a-job)
- [Choosing resources](../../how-to/choose-resources)