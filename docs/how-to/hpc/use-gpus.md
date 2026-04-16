# Use GPUs

## Overview

Run GPU-accelerated jobs on the HPC system using the job scheduler.

---

## Before you begin

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- your code supports GPU execution
- required software or libraries are available
- you know how many GPUs your job requires

---

## Steps

### 1. Log into HPC

```bash
ssh <username>@hpc.uct.ac.za
```

---

### 2. Create a GPU job script

Create a file called `gpu-job.slurm`:

```bash
nano gpu-job.slurm
```

Add the following content:

```bash
#!/bin/bash
#SBATCH --job-name=<job-name>
#SBATCH --output=gpu-%j.out
#SBATCH --error=gpu-%j.err
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=2
#SBATCH --mem=8G
#SBATCH --gres=gpu:1

# Load required modules (if needed)
# module load <gpu-enabled-module>

# Run your program
<command-to-run>
```

Replace:
- `<job-name>` with a meaningful name
- `<command-to-run>` with your GPU-enabled command

---

### 3. Submit the job

```bash
sbatch gpu-job.slurm
```

---

### 4. Check job status

```bash
squeue -u <username>
```

---

## Verify

### Check GPU allocation

After the job starts, check output:

```bash
cat gpu-<job-id>.out
```

Look for indicators that GPUs are being used (depends on your software).

---

### Check job completion

```bash
squeue -u <username>
```

If the job no longer appears, it has finished or failed.

---

## Troubleshooting

### Job does not start

Possible causes:

- no GPUs available
- incorrect resource request
- queue limitations

---

### GPU not used

Possible causes:

- software not configured for GPU
- incorrect command or parameters
- required modules not loaded

---

### Job fails

Check error output:

```bash
cat gpu-<job-id>.err
```

---

## Related pages

- [Submit a job](submit-a-job.md)
- [Use modules](use-software-modules.md)
- [Log into HPC](log-into-hpc.md)