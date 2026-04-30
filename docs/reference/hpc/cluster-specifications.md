# HPC cluster specifications

This page provides factual information about the UCT High Performance Computing (HPC) cluster, including available partitions and their resource characteristics.

---

## Overview

The HPC cluster consists of multiple partitions (queues), each providing access to a set of compute nodes with specific capabilities and limits.

Partitions differ in:

- number of nodes  
- CPU cores per node  
- memory per node  
- GPU availability  
- maximum cores per user  
- maximum job runtime  
- access restrictions  

---

## CPU partitions

These partitions are used for general CPU-based workloads.

| Partition | Nodes | Cores per node | Memory per node | Max cores per user | Max job time |
|----------|------|----------------|------------------|---------------------|--------------|
| `ada`    | ~100 | 32             | ~128 GB          | ~320                | 7 days       |
| `curie`  | ~200 | 32             | ~128 GB          | ~640                | 7 days       |

Notes:

- These are the primary partitions for most workloads  
- Resource limits are enforced per user to ensure fair usage  

---

## GPU partitions

These partitions provide access to GPU-enabled nodes.

| Partition | GPU type        | GPUs per node | CPU cores per node | Notes |
|----------|------------------|---------------|--------------------|------|
| `l40s`   | NVIDIA L40S      | varies        | ~32                | General GPU workloads |
| `a100`   | NVIDIA A100      | varies        | ~32                | High-performance GPU workloads |
| `gpumk`  | Mixed GPU types  | varies        | varies             | Legacy / mixed GPU pool |
| `sadacc` | GPU-enabled      | varies        | varies             | Restricted / project-based access |

Notes:

- GPU resources are limited and may require specific access permissions  
- Exact configurations may vary between nodes  

---

## Additional partitions

Some partitions represent subsets or specialised allocations.

| Partition | Description |
|----------|------------|
| `ada-100` | Subset of `ada` with lower allocation limits |
| `ada-200` | Subset of `ada` with higher allocation limits |
| `sadacc`  | Restricted partition for specific projects |

These partitions may differ in:

- allocation limits  
- scheduling priority  
- access controls  

---

## Resource limits

### Maximum cores per user

Typical limits:

- `ada`: ~320 cores  
- `curie`: ~640 cores  

These limits apply across active jobs within a partition.

---

### Maximum job runtime

- Standard maximum runtime: **7 days**  
- Some partitions may enforce shorter limits  

Jobs exceeding the time limit are terminated by the system.

---

## Notes

- Partition configurations may change over time as hardware is upgraded  
- Not all partitions are accessible to all users  
- For memory allocation details, see:  
  `../../reference/hpc/memory-and-cpu-allocation.md`