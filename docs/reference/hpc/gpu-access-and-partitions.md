# GPU access and partitions

## Overview

GPU resources provide accelerated computation for suitable workloads.

They are limited and managed separately from standard CPU resources.

---

## Access

GPU access is not enabled by default.

You must be granted access before submitting GPU jobs.

Jobs that request GPUs without access will not start.

---

## GPU partitions

GPU-enabled nodes are grouped into specific partitions, such as:

- `l40s`
- `a100`

Check available partitions:

```bash
sinfo
```

---

## Requesting GPUs

Example job configuration:

```bash
#SBATCH --partition=l40s
#SBATCH --gres=gpu:l40s:1
```

The partition and GPU type must match.

---

## Behaviour

GPU jobs:
- may queue longer due to limited availability
- require correct configuration to use GPU resources

Not all workloads benefit from GPUs.

---

## Common issues

Jobs may not start if:
- GPU access has not been granted
- incorrect partition is specified

GPUs may not be used if:
- software is not configured for GPU execution

---

## Good practice

- test workflows on CPU first
- request only the GPUs required
- confirm configuration before scaling