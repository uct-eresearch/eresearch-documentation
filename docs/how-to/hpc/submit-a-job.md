# Submit a job

Submit a batch job to the UCT HPC cluster using the scheduler.

---

## Before you start

You should:

- have an active HPC account  
- are logged into the HPC system  
- have your code or script ready to run  

See:

- [Log into HPC](log-into-hpc.md)  
- [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)

---

## Create a job script

Jobs are submitted using a shell script that defines:

- the resources your job needs  
- the command to run your program  

Create a file (e.g. `job.sh`):

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --time=10:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --job-name="MyJob"

myprogram input.txt
```

---

## Specify resources

Adjust the `#SBATCH` directives:

- `--account` → your research group or allocation  
- `--partition` → compute queue  
- `--time` → expected runtime  
- `--nodes` → number of nodes  
- `--ntasks` → number of CPU cores  

### Optional directives

You can also include:

- `--mail-user=<your-email>` → receive email notifications  
- `--mail-type=ALL` → notify on job start, end, and failure  

Example:

```bash
#SBATCH --mail-user=yourname@uct.ac.za
#SBATCH --mail-type=ALL
```

!!! note "Request only what you need"
    Over-requesting resources can delay your job.

---

## Submit the job

```bash
sbatch job.sh
```

You should see:

```text
Submitted batch job <job-id>
```

This sends the job to the scheduler queue.

!!! warning "Do not run scripts directly"
    Do not run `bash job.sh`.  
    This runs the job on the login node and may result in termination.

---

## Check job output

Output is written to:

```
slurm-<jobid>.out
```

View it:

```bash
tail -f slurm-123456.out
```

---

## Check job status

```bash
squeue
```

To view only your jobs:

```bash
squeue -u <username>
```

You may also use:

```bash
qstat
```

---

## Verify your job

After submission:

- your job should appear in the queue  
- output files will be created when the job runs  

Check your files:

```bash
ls
```

Typical output:

- `slurm-<jobid>.out`

---

## Troubleshooting

### Job stays in queue

- resources requested may not be available  
- queue may be busy  

### Job fails

Check output:

```bash
cat slurm-<jobid>.out
```

### Command not found

- required software may not be loaded  

---

## Example

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --time=10:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=4
#SBATCH --job-name="ExampleJob"

module load software/package
myprogram -i input.txt -o output.txt
```

---

## Common mistakes

- running jobs on the login node instead of using `sbatch`  
- requesting multiple nodes for non-parallel jobs  
- not specifying a time limit  
- writing output to the same file across multiple jobs  

---

## Next steps

- [Check job status](check-job-status.md)  
- [Cancel a job](cancel-a-job.md)  
- [Run parallel jobs](run-parallel-jobs.md)