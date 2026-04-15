# Submit a job

## Purpose

Run work on compute nodes using the scheduler.

---

## Go to project directory

```bash
cd ~/projects/my-project
```

---

## Create logs directory

```bash
mkdir -p logs
```

---

## Create job script

```bash
#!/bin/bash
#SBATCH --job-name=my-job
#SBATCH --partition=ada
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --time=01:00:00
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

module purge
module load python/miniconda3-py3.12

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

## Check output

```bash
cat logs/job-<jobid>.out
cat logs/job-<jobid>.err
```