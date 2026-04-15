# Connect to HPC

## Purpose

Connect to the HPC system to prepare work, submit jobs, and inspect results.

---

## Before you begin

You need:
- approved HPC access
- your username
- a terminal (Linux/macOS) or SSH client (Windows)

---

## Connect

```bash
ssh <username>@hpc.uct.ac.za
```

If you are off-campus, connect via VPN first.

---

## Confirm connection

```bash
whoami
hostname
pwd
```

---

## Create a working directory

```bash
mkdir -p ~/projects/my-project
cd ~/projects/my-project
```

---

## Next

- [Manage files and storage](./manage-files-and-storage.md)  
- [Submit a job](./submit-a-job.md)