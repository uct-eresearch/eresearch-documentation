# Use GPUs

## Purpose

Run jobs that require GPU acceleration.

---

## Before you begin

You should be able to:
- connect to HPC
- submit jobs
- load software modules

GPU access must be enabled for your account.

---

## Check available GPU partitions

```bash
sinfo
```

---

## Create a GPU job script

```bash
#!/bin/bash
#SBATCH --job-name=gpu-job
#SBATCH --partition=l40s
#SBATCH --gres=gpu:l40s:1
#SBATCH --time=01:00:00
#SBATCH --mem=16G
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

module purge
module load cuda

python script.py
```

---

## Submit job

```bash
sbatch job.sh
```

---

## Check status

```bash
squeue -u $USER
```

---

## Check GPU usage

```bash
nvidia-smi
```

---

## Notes

- Partition and GPU type must match  
- Jobs will wait if GPUs are not available  