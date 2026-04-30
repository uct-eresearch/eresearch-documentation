# Manage Files and Storage

## Overview

Manage files and directories on the HPC system during your workflow.

---

## Before you begin

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- you know where your data is stored (home, project, or other locations)
- you have appropriate permissions for the files you are working with

!!! warning "Storage limits apply"
    - `/home` has strict quotas  
    - `/scratch` is not backed up  

    See: [Storage and file systems](../../reference/hpc/storage-and-file-systems.md)

---

## Steps

### 1. Log into HPC

```bash
ssh <username>@hpc.uct.ac.za
```

---

### 2. Check your current location

```bash
pwd
```

This shows your current directory.

---

### 3. List files and directories

```bash
ls
```

For more detail:

```bash
ls -lh
```

---

### 4. Change directories

```bash
cd <directory-name>
```

Example:

```bash
cd data
```

To move up one level:

```bash
cd ..
```

---

### 5. Create directories

```bash
mkdir <directory-name>
```

Example:

```bash
mkdir results
```

---

### 6. Copy files

```bash
cp <source> <destination>
```

Example:

```bash
cp input.txt results/
```

---

### 7. Move or rename files

```bash
mv <source> <destination>
```

Example:

```bash
mv input.txt data/
```

Rename a file:

```bash
mv old.txt new.txt
```

---

### 8. Remove files or directories

Remove a file:

```bash
rm <file-name>
```

Remove a directory:

```bash
rm -r <directory-name>
```

Use with caution. This action cannot be undone.

---

### 9. Check disk usage

```bash
du -sh *
```

Check total usage of current directory:

```bash
du -sh .
```

---

### 10. Check available space

```bash
df -h
```

---

## Verify

Check that:

- files are present in expected locations (`ls`)
- file sizes are as expected (`ls -lh`)
- directories contain the correct contents

---

## Troubleshooting

### Permission denied

Possible causes:

- insufficient permissions
- attempting to modify protected files or directories

---

### File not found

Possible causes:

- incorrect path
- file does not exist in current directory

Check location:

```bash
pwd
ls
```

---

### Disk quota exceeded

Possible causes:

- storage limit reached
- too many files or large datasets

Check usage:

```bash
du -sh .
```

---

## Related pages

- [Log into HPC](log-into-hpc.md)
- [Submit a job](submit-a-job.md)
- [Use software modules](use-software-modules.md)