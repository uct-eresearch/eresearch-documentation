# Sync repository changes

## Purpose

Keep your local repository aligned with the remote repository and publish your changes.

---

## What you need to decide first

- whether you need to download remote changes
- whether your local changes are ready to commit
- whether you are working directly on the main branch or a feature branch

---

## Check repository status

```bash
git status
```

---

## Download remote changes

```bash
git pull
```

---

## Stage local changes

```bash
git add .
```

Or stage selected files:

```bash
git add path/to/file
```

---

## Commit local changes

```bash
git commit -m "Describe the change"
```

---

## Push changes to the remote repository

```bash
git push
```

---

## Check recent history

```bash
git log --oneline -5
```

---

## Notes

- Pull before starting new work if others may have changed the repository
- Commit small, meaningful changes
- Do not commit large data files or generated outputs unless the project expects them

---

## Next

- Collaborate on code
- Document how to run the project