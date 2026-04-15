# Storage and file systems

## Storage on UCT HPC

The UCT HPC system provides different storage areas for different purposes. Understanding how to use each correctly is essential for performance, reliability, and responsible use of shared resources.

---

## Overview

There are two primary storage locations available to users:

- `/home` → for code, small files, and persistent user data  
- `/scratch` → for active computations and temporary data  

These serve different roles and should not be used interchangeably.

---

## `/home`

### Purpose

`/home` is your personal storage space on the HPC system.

Use it for:
- code and scripts
- configuration files
- small datasets
- lightweight outputs you want to retain

### Characteristics

- persistent (files are retained between sessions)
- backed up (where applicable)
- limited in size compared to `/scratch`
- accessible from login nodes and compute nodes

### What not to store here

Avoid using `/home` for:
- large datasets
- intermediate files from jobs
- high-throughput I/O workloads

This can negatively affect system performance and may exceed quotas.

---

## `/scratch`

### Purpose

`/scratch` is designed for **high-performance, temporary storage during computation**.

Use it for:
- intermediate files generated during jobs
- large datasets used in active processing
- temporary outputs that will be moved or deleted after use

### Characteristics

- high-performance (optimised for fast read/write during jobs)
- not intended for long-term storage
- shared across users
- subject to quotas and cleanup policies

### Expected usage

You should:
- write job outputs to `/scratch`
- process data in `/scratch`
- move final results to a more persistent location when jobs complete

---

## Quotas

Storage on HPC is limited and managed.

- `/scratch` typically has a default quota (e.g. 100GB per user)
- quotas may vary depending on project or allocation
- exceeding quota can cause jobs to fail or data writes to stop

Check your usage regularly and clean up unnecessary files.

---

## Data lifecycle on HPC

A typical workflow looks like:

1. Store code and small inputs in `/home`
2. Transfer large datasets to `/scratch`
3. Run jobs using data in `/scratch`
4. Write intermediate and output files to `/scratch`
5. Move final results to long-term storage (e.g. RDS)
6. Clean up `/scratch`

---

## Relationship to other storage services

HPC storage is **not intended for long-term data management**.

For persistent research data:
- use **Research Data Storage (RDS)** or other managed storage services

For data transfer:
- use tools such as Globus, SCP, or rsync to move data between systems

---

## Good usage practices

- keep `/home` small and organised
- use `/scratch` for all compute-intensive work
- remove intermediate files once they are no longer needed
- do not treat `/scratch` as archival storage
- plan where your data will live after computation

---

## Common issues

### Jobs failing due to storage

- caused by exceeding quota or writing to the wrong location  
- ensure jobs use `/scratch` for large or temporary data  

### Slow performance

- often due to heavy I/O in `/home`  
- move data-intensive operations to `/scratch`  

### Lost data

- occurs when temporary data in `/scratch` is not moved after jobs complete  
- always transfer important outputs to a persistent location  

---

## Related pages

- HPC overview → `Services > HPC`
- Running analyses → `Tasks`
- Transferring data → `How-to`
- Long-term storage → `Services > RDS`