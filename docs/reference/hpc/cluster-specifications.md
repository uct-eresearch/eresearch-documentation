# Cluster specifications

## Overview

The UCT HPC cluster consists of multiple node types grouped into partitions with different performance characteristics.

---

## Partitions and resources

| Partition | Description | Cores per node | Memory | Time limit |
|----------|-------------|----------------|--------|-----------|
| ada (100 series) | Fast cores, less RAM | 48 | ~384 GB | 250 hours |
| ada (200 series) | Slower cores, more RAM | 40 | ~384 GB | 250 hours |
| curie | Alternate partition | 64 | varies | 100 hours |
| l40s | GPU partition | GPU-enabled | varies | 48 hours |

---

## What this means for users

- Different partitions are suited to different workloads  
- GPU partitions are required for GPU-based jobs  
- Memory and CPU characteristics vary between partitions  

---

## Related pages

- [Choosing resources](../../good-practice/hpc/choosing-resources.md)