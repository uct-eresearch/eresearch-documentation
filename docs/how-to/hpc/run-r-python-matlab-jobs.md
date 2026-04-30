# Run R, Python and MATLAB jobs

Run R, Python and MATLAB scripts on the UCT HPC cluster using the scheduler.

---

## When to use this guide

Use this guide when you already have an R, Python or MATLAB script and want to run it as a scheduled batch job on the HPC system.

Do not run computationally intensive R, Python or MATLAB scripts directly on the login node. Submit them to the scheduler using `sbatch`.

---

## Before you start

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- your script is saved on the HPC system
- your input data is accessible from the HPC system
- you know which software module you need to load
- you know your HPC account or research group allocation

You can list available software modules with:

```bash
module avail
```

---

## General job script structure

R, Python and MATLAB jobs all use the same basic pattern:

1. create a shell script
2. request resources using `#SBATCH` directives
3. load the required software module
4. run your script
5. submit the job with `sbatch`

!!! warning "Do not run the job script directly"
    Submit the job with `sbatch`.  
    Do not run `bash job.sh`, because this runs the script on the login node.

---

## Run an R job

Create a job script, for example `run-r-job.sh`:

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --job-name="MyRJob"

module load software/R-4.3.3
R CMD BATCH MyRScript.R
```

Submit the job:

```bash
sbatch run-r-job.sh
```

Replace:

- `myaccount` with your HPC account or research group allocation
- `MyRScript.R` with the name of your R script
- `software/R-4.3.3` with the appropriate R module, if needed

---

## Run a Python job

Create a job script, for example `run-python-job.sh`:

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --job-name="MyPythonJob"

module load python/miniconda3-py3.12
python MyPythonScript.py
```

Submit the job:

```bash
sbatch run-python-job.sh
```

Replace:

- `myaccount` with your HPC account or research group allocation
- `MyPythonScript.py` with the name of your Python script
- `python/miniconda3-py3.12` with the appropriate Python module, if needed

!!! note "Python modules"
    UCT HPC uses Miniconda for Python modules. The Python version is usually included in the module name.

---

## Run a MATLAB job

Create a job script, for example `run-matlab-job.sh`:

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=10:00
#SBATCH --job-name="MyMatlabJob"

module load software/matlab-R2024b
matlab -batch MyMatlabScript
```

Submit the job:

```bash
sbatch run-matlab-job.sh
```

Replace:

- `myaccount` with your HPC account or research group allocation
- `MyMatlabScript` with the name of your MATLAB script
- `software/matlab-R2024b` with the appropriate MATLAB module, if needed

!!! warning "MATLAB script names"
    When using `matlab -batch`, do not include the `.m` extension.  
    Use `matlab -batch MyMatlabScript`, not `matlab -batch MyMatlabScript.m`.

---

## Check job status

After submitting your job, check whether it is queued or running:

```bash
squeue -u <username>
```

Replace `<username>` with your UCT username.

You can also check the output file:

```bash
tail -f slurm-<jobid>.out
```

---

## Adjust resources

The examples above request one node and one task:

```bash
#SBATCH --nodes=1
#SBATCH --ntasks=1
```

This is suitable for many simple R, Python and MATLAB scripts.

If your script can use multiple cores, adjust the resource request and make sure your code is configured to use those cores. Requesting more cores will not automatically make a script run faster.

For parallel jobs, see:

- [Run parallel jobs](run-parallel-jobs.md)

---

## Common mistakes

- running the job script with `bash` instead of `sbatch`
- forgetting to load the required software module
- using the wrong module version
- requesting more cores than the script can use
- running large jobs from the login node
- including `.m` when using `matlab -batch`

---

## Troubleshooting

### Command not found

The required software module may not be loaded.

Check available modules:

```bash
module avail
```

Load the relevant module before running your script.

### Job fails immediately

Check the Slurm output file:

```bash
cat slurm-<jobid>.out
```

Look for errors such as missing files, incorrect paths, missing packages or incorrect module names.

### Script cannot find input files

Check that your input files are in the expected location and that your job script uses the correct paths.

### Python package is missing

Check whether a suitable Python module is available. If you need additional Python packages, follow the local guidance for using Python environments on the HPC system or contact support.

### R package is missing

Check whether the package is already available in the loaded R module. If not, you may need to install it in your user environment or request advice from support.

### MATLAB script does not start

Make sure you are using:

```bash
matlab -batch MyMatlabScript
```

Do not include the `.m` extension in the command.

---

## Next steps

- [Submit a job](submit-a-job.md)
- [Check job status](check-job-status.md)
- [Run parallel jobs](run-parallel-jobs.md)
- [Run interactive jobs](run-interactive-jobs.md)