# Graphical applications

## Running graphical applications on UCT HPC

Some research workflows require graphical interfaces, such as:

- visualisation tools
- IDEs
- MATLAB or similar environments

On HPC, graphical applications run on compute nodes, with output displayed remotely.

---

## Recommended approach

For most users, graphical applications should be run via:

→ Open OnDemand (web-based access)

This provides a more stable, accessible, and persistent interface.

See:

- Open OnDemand → Reference > HPC

---

## Alternative approach: X11 forwarding

X11 forwarding allows graphical applications to display on your local machine over SSH.

This approach:

- is older and less reliable
- depends on local configuration
- can be slow over typical network connections

Use X11 only when:

- the application is not available via Open OnDemand
- you need a lightweight graphical tool
- you understand the limitations

---

## Do not run GUI applications on the login node

Login nodes are for:

- connecting to the system
- editing files
- submitting jobs

They are not designed for running applications.

Always use interactive jobs.

---

## Interactive job example

```bash
srun --partition=ada --nodes=1 --ntasks=1 --time=02:00:00 --pty bash
```

---

## Using X11 forwarding

### Connect with X forwarding

```bash
ssh -X username@hpc.uct.ac.za
```

or

```bash
ssh -Y username@hpc.uct.ac.za
```

### Start an interactive job

```bash
srun --partition=ada --nodes=1 --ntasks=1 --time=02:00:00 --pty bash
```

### Test

```bash
xclock
```

---

## Running applications (examples)

### MATLAB

```bash
module load matlab
matlab
```

### R

```bash
module load R/R-4.3.3
R
```

### Python

```bash
module load python/miniconda3-py3.12
python
```

---

## Performance considerations

X11 forwarding can be:

- slow
- laggy
- sensitive to network quality

Prefer:

- saving outputs to file
- viewing results locally
- using Open OnDemand where possible

---

## Alternatives to GUI workflows

Many workflows are better without graphical interfaces.

Prefer:

- batch jobs
- scripts
- file-based outputs
- notebooks

---

## Troubleshooting

### Cannot open display

Check:

- ssh -X or -Y was used
- a local X server is running

### Test X11

```bash
xclock
```

---

## Good practice

- prefer Open OnDemand for GUI workflows
- use X11 only when necessary
- always run applications via interactive jobs
- avoid login node usage
- minimise reliance on GUI tools

---

## Related pages

- Open OnDemand → Reference > HPC
- Software and modules → Reference > HPC
- Scheduler and job submission → Reference > HPC
- Storage and file systems → Reference > HPC