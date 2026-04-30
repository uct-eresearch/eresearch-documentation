# Run interactive jobs

Run an interactive session on a compute node.

---

## When to use interactive jobs

Use an interactive job when you need:

- a command-line session on a compute node  
- to test code before submitting a batch job  
- to run graphical applications  
- to debug or explore data  

---

## Start an interactive session

From the login node, run:

```bash
sintx
```

If resources are available, your prompt will change to a compute node.

---

## Run commands

Once the session starts:

- all commands run on the compute node  
- you can execute programs as you would on a normal system  

---

## Specify resources (optional)

You can request specific resources:

```bash
sintx --ntasks=4 --time=01:00:00 --partition=ada --account=myaccount
```

---

## End the session

To exit the interactive session:

```bash
exit
```

This releases the allocated resources.

---

## Important notes

- Do not run heavy workloads on the login node  
- If you do not see confirmation that the session has started, you are still on the login node  
- Interactive sessions consume resources while active  

---

## Troubleshooting

### Session does not start

- resources may not be available  
- try requesting fewer resources or wait  

### Commands run on login node

- ensure the interactive session has started  
- check the hostname if unsure  

---

## Next steps

- [Submit a job](submit-a-job.md)  
- [Run parallel jobs](run-parallel-jobs.md)