# Run R, Python and MATLAB jobs

## Overview

Run R, Python and MATLAB scripts on the HPC system using the scheduler.

These jobs are submitted as batch jobs and run on compute nodes.

---

## Before you begin

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- your script is available on the system
- your input data is accessible
- you know which software module to use  
- you have identified the required resources  
  (see: [Choosing resources](../../good-practice/hpc/choosing-resources.md))

For background on how jobs are scheduled, see:  
[Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)

---

## Steps

### 1. Create a job script

All jobs follow the same structure:

- request resources using `#SBATCH`
- load the required module
- run your script

---

### 2. Run an R job

```bash
#!/bin/bash
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --job-name=my-r-job

module load software/R-4.3.3

R CMD BATCH MyRScript.R
```

---

### 3. Run a Python job

```bash
#!/bin/bash
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --job-name=my-python-job

module load python/miniconda3-py3.12

python MyPythonScript.py
```

---

### 4. Run a MATLAB job

```bash
#!/bin/bash
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=00:10:00
#SBATCH --job-name=my-matlab-job

module load software/matlab-R2024b

matlab -batch MyMatlabScript
```

---

### 5. Submit the job

```bash
sbatch job.sh
```

---

### 6. Check job status

```bash
squeue -u $USER
```

---

## Important notes

- do not run scripts directly on the login node  
- always submit jobs using `sbatch`  
- loading the correct module is required  
- requesting more resources does not automatically improve performance  

---

## Adjust resources

The examples above use a single task:

```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
```

If your script supports parallel execution:

- increase `--ntasks`
- configure your code to use multiple cores  

For parallel execution, see:  
[Run parallel jobs](run-parallel-jobs.md)

---

## Troubleshooting

**Command not found**
- ensure the correct module is loaded  

**Job fails immediately**
- check output files for errors  

**Missing packages (R/Python)**
- verify installed packages or use appropriate environments  

**MATLAB script does not start**
- use `matlab -batch MyMatlabScript` (no `.m` extension)  

---

## Related pages

- [Submit a job](submit-a-job.md)
- [Run parallel jobs](run-parallel-jobs.md)
- [Run interactive jobs](run-interactive-jobs.md)
- [Check job status](check-job-status.md)
- [Choosing resources](../../good-practice/hpc/choosing-resources.md)
- [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)