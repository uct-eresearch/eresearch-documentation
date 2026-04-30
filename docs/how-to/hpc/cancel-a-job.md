# Cancel a job

Cancel a queued or running job on the HPC system.

---

## When to cancel a job

Cancel a job when:

- you submitted it by mistake
- you requested the wrong resources
- the job is no longer needed
- the job is running the wrong command or input file
- the job is producing incorrect output

Cancelling a job releases the resources allocated to it.

---

## Before you start

You should know the job ID of the job you want to cancel.

To view your jobs:

```bash
qstat
```

Or use:

```bash
squeue -u <username>
```

Replace `<username>` with your UCT username.

---

## Cancel a job

Use `scancel` followed by the job ID:

```bash
scancel <job-id>
```

Example:

```bash
scancel 123456
```

This requests that the scheduler stop the job.

---

## Confirm that the job has been cancelled

Check the queue again:

```bash
qstat
```

Or:

```bash
squeue -u <username>
```

If the job no longer appears in the queue, it has been cancelled or has already completed.

---

## Cancel multiple jobs

You can cancel more than one job by listing the job IDs:

```bash
scancel 123456 123457 123458
```

Only cancel jobs that you are sure you no longer need.

---

## Important notes

- Cancelling a job stops it before it finishes.
- Output files already written may remain in your working directory.
- Partially written output files may be incomplete or unusable.
- If you cancel a job and resubmit it, check that it will not overwrite existing output files.

!!! warning "Check before cancelling"
    Make sure you are cancelling the correct job. Use `qstat` or `squeue` to confirm the job ID before running `scancel`.

---

## Troubleshooting

### Job does not disappear immediately

The scheduler may take a short time to remove the job from the queue.

Check again with:

```bash
qstat
```

or:

```bash
squeue -u <username>
```

### Job has already finished

If the job no longer appears in the queue, it may already have completed.

Check your working directory for output files, including:

```text
slurm-<jobid>.out
```

### Permission denied

You can usually only cancel jobs that you submitted yourself.

If you think a job is causing a problem and you cannot cancel it, contact the HPC administrators.

---

## Next steps

- [Submit a job](submit-a-job.md)
- [Check job status](check-job-status.md)
- [Run interactive jobs](run-interactive-jobs.md)