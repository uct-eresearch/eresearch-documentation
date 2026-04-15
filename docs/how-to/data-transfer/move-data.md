# Move data

## Purpose

Transfer data between your local machine, HPC, and managed storage.

---

## What you need to decide first

- whether this is a one-time copy or repeated sync
- whether the data is small or large
- where the data should live after transfer

---

## Choose a transfer method

Use:

- `scp` for simple, one-time copies
- `rsync` for repeated transfers or large directories
- Globus, where available, for large managed transfers

---

## Copy a file with `scp`

From your local machine to HPC:

```bash
scp local-file.txt <username>@hpc.uct.ac.za:~/projects/my-project/
```

From HPC to your local machine:

```bash
scp <username>@hpc.uct.ac.za:~/projects/my-project/results.txt .
```

---

## Synchronise a directory with `rsync`

From your local machine to HPC:

```bash
rsync -avh data/ <username>@hpc.uct.ac.za:~/projects/my-project/data/
```

From HPC to your local machine:

```bash
rsync -avh <username>@hpc.uct.ac.za:~/projects/my-project/results/ results/
```

---

## Check transferred data

```bash
ls -lah ~/projects/my-project/
du -sh ~/projects/my-project/data/
```

---

## Notes

- Use `/scratch` for large active datasets during computation
- Use `/home` for code and small files
- Avoid repeated full copies when `rsync` is sufficient

---

## Next

- Manage files and storage
- Store and share research data