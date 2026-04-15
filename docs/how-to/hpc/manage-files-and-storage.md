# Manage files and storage

## Purpose

Organise, inspect, and control data on HPC systems.

---

## Storage types (conceptual)

- home
- project
- scratch

Each differs in:
- performance
- persistence
- quota

---

## Structure

```bash
~/project/
  code/
  data/
  results/
  logs/
```

---

## Key commands

```bash
ls -lah
du -sh .
df -h
```

---

## Movement

```bash
cp
mv
rm
```

---

## Constraints

- avoid duplication
- do not misuse scratch for long-term storage
- respect quotas

---

## Common issues

- disk full
- permission denied
- missing outputs

---

## Good practice

- structured directories
- explicit naming
- clean up intermediates

---

## Next step

use-software-modules.md