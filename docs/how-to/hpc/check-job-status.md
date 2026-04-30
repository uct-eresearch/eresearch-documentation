# Check job status

Check the status of your jobs on the HPC system.

---

## View your jobs

To see your running and queued jobs:

```bash
squeue
```

To view only your jobs:

```bash
squeue -u <username>
```

Replace `<username>` with your UCT username.

---

## Understand job states

Jobs in the queue are shown with a status code:

- **R (Running)** — job is currently running  
- **PD (Pending)** — job is waiting in the queue  
- **CG (Completing)** — job is finishing  
- **F (Failed)** — job terminated with an error  

---

## Check why a job is pending

If your job is not running:

```bash
squeue -u <username>
```

Look at the **REASON** column.

Common reasons include:

- `(Resources)` — requested resources are not yet available  
- `(Priority)` — other jobs are ahead in the queue  

---

## Check detailed job information

For more detail about a specific job:

```bash
scontrol show job <job-id>
```

---

## Check job output

Jobs write output to a file:

```
slurm-<jobid>.out
```

View output:

```bash
cat slurm-<jobid>.out
```

For live updates:

```bash
tail -f slurm-<jobid>.out
```

---

## Confirm job completion

A job has finished when:

- it no longer appears in `squeue`  
- output files have been written  

---

## Next steps

- [Submit a job](submit-a-job.md)  
- [Cancel a job](cancel-a-job.md)