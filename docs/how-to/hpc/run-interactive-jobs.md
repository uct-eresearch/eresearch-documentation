# Run interactive jobs

## Overview

Run an interactive session on a compute node.

Interactive jobs provide a temporary shell on a compute node for testing, debugging, or short exploratory work.

---

## When to use interactive jobs

Use an interactive job when you need:

- a command-line session on a compute node  
- to test code before submitting a batch job  
- to debug scripts or workflows  
- to run short or exploratory tasks  

For background on how resources are allocated and scheduled, see:  
[Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)

---

## Start an interactive session

From the login node:

```bash
sintx
```

If resources are available, your session will start on a compute node.

---

## Run commands

Once the session starts:

- commands run on the compute node  
- you can execute programs as needed  

---

## Specify resources (optional)

Request specific resources if needed:

```bash
sintx --ntasks=4 --time=01:00:00 --partition=ada --account=myaccount
```

Choose resources carefully:  
[Choosing resources](../../good-practice/hpc/choosing-resources.md)

---

## End the session

To exit:

```bash
exit
```

This releases all allocated resources.

---

## Important notes

- interactive sessions consume resources while active  
- sessions may wait in a queue if resources are not immediately available  
- always confirm you are on a compute node before running work  

---

## Troubleshooting

**Session does not start**
- resources may not be available  
- try requesting fewer resources or wait  

**Commands run on login node**
- confirm the session has started  
- check hostname if unsure  

---

## Related pages

- [Submit a job](submit-a-job.md)
- [Run parallel jobs](run-parallel-jobs.md)
- [Choosing resources](../../good-practice/hpc/choosing-resources.md)
- [Scheduler and job submission](../../reference/hpc/scheduler-and-job-submission.md)