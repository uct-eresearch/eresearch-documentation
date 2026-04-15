# Submit a Job

## Overview

Run a batch job on the HPC system using the job scheduler.

---

## Before you begin

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- your code or executable is available on the system
- your input data is accessible
- you know how long your job is expected to run
- you have identified the resources your job requires (CPU, memory, GPU if needed)

---

## Steps

### 1. Log into HPC

```bash
ssh <username>@hpc.uct.ac.za
```

---

### 2. Create a job script

Create a file called `job.slurm`:

```bash
nano job.slurm
```

Add the following content:

```bash
#!/bin/bash
#SBATCH --job-name=<job-name>
#SBATCH --output=job-%j.out
#SBATCH --error=job-%j.err
#SBATCH --time=01:00:00
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --mem=4G

# Load required modules (if needed)
# module load <module-name>

# Run your program
<command-to-run>
```

Replace:
- `<job-name>` with a meaningful name
- `<command-to-run>` with your actual command

---

### 3. Submit the job

```bash
sbatch job.slurm
```

You should see output similar to:

```text
Submitted batch job <job-id>
```

---

### 4. Check job status

```bash
squeue -u <username>
```

This shows your running and queued jobs.

---

## Verify

### Check output files

After the job completes:

```bash
ls
```

You should see:

- `job-<job-id>.out`
- `job-<job-id>.err`

Inspect output:

```bash
cat job-<job-id>.out
```

---

### Check job completion

If the job no longer appears in the queue:

```bash
squeue -u <username>
```

then it has finished or failed.

---

## Troubleshooting

### Job stays in queue

Possible causes:

- insufficient resources requested
- queue is busy
- job requires a specific partition or resource

---

### Job fails immediately

Check:

```bash
cat job-<job-id>.err
```

Possible causes:

- incorrect command
- missing input files
- required modules not loaded

---

### Output files are empty

Possible causes:

- job did not execute correctly
- command produced no output
- job terminated early

---

### Command not found

Possible causes:

- required software is not loaded
- incorrect command path

---

## Related pages

- [Log into HPC](log-into-hpc.md)
- [Use modules](use-modules.md)
- [Use GPUs](use-gpus.md)