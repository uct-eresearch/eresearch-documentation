# Manage files and storage

## Purpose

Organise files and prepare data for computation.

---

## Create a project directory

```bash
mkdir -p ~/projects/my-project
cd ~/projects/my-project
```

---

## Create a structure

```bash
mkdir -p code data results logs
```

---

## Inspect storage

```bash
ls -lah
du -sh .
df -h .
```

---

## Move and organise files

```bash
cp input.txt data/
mv results.txt results/
```

---

## Remove files

```bash
rm unwanted-file.txt
```

---

## Notes

- Use `/home` for code and small files  
- Use `/scratch` for large data and job output  

---

## Next

- Use software modules  
- Submit a job