# Connect to HPC

## Purpose

Establish a secure connection to the HPC system so you can:
- access files
- prepare jobs
- inspect outputs

---

## Preconditions

You must have:
- HPC access approved
- valid credentials
- a terminal or browser

---

## SSH connection

```bash
ssh <username>@<host>
```

On first login:
- accept host key
- complete authentication

---

## Validate environment

```bash
hostname
whoami
pwd
```

---

## Working directory setup

```bash
mkdir -p ~/projects/my-project
cd ~/projects/my-project
```

---

## Open OnDemand (optional)

Use browser-based access for:
- file browsing
- light interactive work
- graphical tools

See:
../../reference/hpc/open-ondemand.md

---

## Constraints

- do not run heavy compute on login nodes
- use scheduler for all compute jobs

---

## Next step

Proceed to:
submit-a-job.md