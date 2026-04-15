# Clone a repository

## Purpose

Create a local copy of a Git repository so you can work on the code.

---

## What you need to decide first

- whether the repository is hosted on GitLab or GitHub
- whether you need read-only access or write access
- where the repository should live on your system

---

## Go to your working directory

```bash
mkdir -p ~/projects
cd ~/projects
```

---

## Clone the repository

Using HTTPS:

```bash
git clone https://gitlab.example.org/group/project.git
```

Using SSH:

```bash
git clone git@gitlab.example.org:group/project.git
```

---

## Go into the repository

```bash
cd project
```

---

## Check repository status

```bash
git status
git remote -v
```

---

## Notes

- Store code in your project space
- Keep large datasets out of the repository
- Use a separate storage location for data and outputs

---

## Next

- Sync repository changes
- Collaborate on code