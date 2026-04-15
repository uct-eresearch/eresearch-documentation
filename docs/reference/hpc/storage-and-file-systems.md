# Storage and file systems

## Overview

UCT HPC provides two main storage locations:

- `/home` — persistent storage
- `/scratch` — high-performance temporary storage

Each is designed for a specific purpose.

---

## /home

Use `/home` for:
- code and scripts
- configuration files
- small datasets

Characteristics:
- persistent
- limited capacity
- suitable for low I/O workloads

Avoid using `/home` for large or compute-intensive data operations.

---

## /scratch

Use `/scratch` for:
- job input and output
- large datasets
- intermediate files

Characteristics:
- high-performance
- not persistent
- subject to quotas and cleanup

Data in `/scratch` may be removed.  
Move results you want to keep to a persistent location.

---

## Typical workflow

1. store code in `/home`
2. copy data to `/scratch`
3. run jobs using `/scratch`
4. move results out of `/scratch`
5. remove temporary files

---

## Checking usage

```bash
df -h
du -sh *
```

---

## Common issues

Jobs may fail if:
- storage quota is exceeded
- large data is written to `/home`

Performance may be reduced if:
- heavy I/O is performed outside `/scratch`

Data may be lost if:
- results are left in `/scratch`

---

## Good practice

- keep `/home` small and organised
- use `/scratch` for computation
- remove unnecessary files regularly