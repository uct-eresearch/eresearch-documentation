# Submit a job (UCT-specific)

## Purpose

Run workloads on UCT HPC using the SLURM scheduler.

---

## UCT HPC scheduler model

UCT HPC uses SLURM:
- jobs are submitted with `sbatch`
- resources are allocated via partitions
- queues may differ (CPU vs GPU)

Reference:
../../reference/hpc/scheduler-and-job-submission.md

---

## Minimal job script (UCT example)

```bash
#!/bin/bash
#SBATCH --job-name=uct-test
#SBATCH --partition=compute
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

module load python/3.10

python script.py
```

---

## Directory setup

```bash
mkdir -p ~/projects/my-project/{logs,results}
cd ~/projects/my-project
```

---

## Submit job

```bash
sbatch job.sh
```

Expected output:
```
Submitted batch job <jobid>
```

---

## Monitor jobs

```bash
squeue -u $USER
```

---

## Inspect job

```bash
scontrol show job <jobid>
```

---

## After completion

Check outputs:

```bash
cat logs/job-<jobid>.out
cat logs/job-<jobid>.err
```

---

## GPU jobs (UCT example)

```bash
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
```

Full example:

```bash
#!/bin/bash
#SBATCH --job-name=gpu-test
#SBATCH --partition=gpu
#SBATCH --gres=gpu:1
#SBATCH --time=02:00:00

module load cuda

python train.py
```

Reference:
../../reference/hpc/gpu-access-and-partitions.md

---

## Common UCT-specific pitfalls

- using wrong partition (job stays pending)
- exceeding memory limits (job killed)
- forgetting module load
- writing outputs to wrong directory

---

## Good practice

- always test with small jobs first
- monitor queue behaviour
- keep logs organised
- match partition to workload

---

## Next step

manage-files-and-storage.md