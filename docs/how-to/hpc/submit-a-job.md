# Submit a job

## Run your work on HPC using the scheduler

Use this guide to run your analysis or script on HPC.

Do not run compute-intensive work directly on login nodes.

---

## Before you begin

Make sure you:

- can [connect to HPC](connect-to-hpc.md)
- have your code or script ready
- know where your input data is stored

---

## 1. Create a working directory

```bash
mkdir -p ~/projects/my-project
cd ~/projects/my-project
```

---

## 2. Create a job script

Create a file (for example, `job.sh`):

```bash
#!/bin/bash
#SBATCH --job-name=my-job
#SBATCH --time=01:00:00
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --output=logs/job-%j.out
#SBATCH --error=logs/job-%j.err

module load python

python script.py
```

Adjust:
- time
- memory
- CPUs
- modules
- script name

---

## 3. Submit the job

```bash
sbatch job.sh
```

You should see output similar to:

```
Submitted batch job <jobid>
```

---

## 4. Check job status

```bash
squeue -u $USER
```

---

## 5. Check results

When the job finishes, inspect:

```bash
cat logs/job-<jobid>.out
cat logs/job-<jobid>.err
```

---

## If something does not work

Check:

- output and error files
- file paths
- that required modules are loaded
- resource requests (time, memory, CPUs)

---

## Learn more

- [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)
- [Software and modules](../../reference/hpc/software-and-modules.md)
- [GPU access and partitions](../../reference/hpc/gpu-access-and-partitions.md)