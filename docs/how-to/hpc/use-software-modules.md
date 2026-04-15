# Use software modules

## Purpose

Load and manage software environments.

---

## Why modules exist

- avoid conflicts
- support multiple versions
- isolate environments

---

## Discover

```bash
module avail
```

---

## Load

```bash
module load python
```

---

## Verify

```bash
module list
which python
```

---

## Unload

```bash
module unload python
```

---

## Common issues

- wrong version loaded
- missing dependency
- module not found

---

## Good practice

- explicitly load modules in job scripts
- avoid relying on defaults

---

## Next step

submit-a-job.md