# Connect to HPC (UCT-specific)

## Purpose

Establish a secure connection to the UCT HPC systems so you can:
- access your files
- prepare and submit jobs
- monitor outputs

---

## Preconditions

You must have:
- an active UCT account
- approved access to UCT HPC
- your HPC username
- network access (VPN may be required off-campus)

---

## SSH connection (UCT HPC)

Use SSH to connect to the login node.

```bash
ssh <username>@login.chpc.uct.ac.za
```

Replace:
- `<username>` with your UCT HPC username

---

## First login

On first connection:
- accept the host key prompt
- enter your password
- complete MFA if required

---

## Verify connection

```bash
hostname
whoami
pwd
```

You should see:
- a login node hostname
- your correct username
- your home directory

---

## Directory setup (UCT convention)

```bash
mkdir -p ~/projects/my-project
cd ~/projects/my-project
```

Avoid working directly in `$HOME` for large workflows.

---

## Open OnDemand (UCT)

UCT provides web-based access via Open OnDemand.

Typical usage:
- open browser
- navigate to UCT HPC OnDemand portal
- login with UCT credentials

Use this for:
- file browsing
- terminal access
- graphical tools

Reference:
../../reference/hpc/open-ondemand.md

---

## Important constraints

- login nodes are NOT for heavy computation
- always submit jobs via the scheduler
- large data transfers should use appropriate transfer tools

---

## Common issues (UCT context)

### Connection refused
- check hostname
- confirm VPN if off-campus

### Authentication fails
- confirm UCT credentials
- check account activation

---

## Next step

Proceed to:
submit-a-job.md