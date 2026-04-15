# Sync a Repository

## Overview

Update your local repository and send your changes to the remote repository.

---

## Before you begin

Make sure:

- you have cloned the repository  
  (see: [Clone a repository](clone-a-repository.md))
- you are inside the repository directory
- you have permission to update the repository

---

## Steps

### 1. Open a terminal

Open a terminal on your local machine.

---

### 2. Navigate to the repository

```bash
cd <repository-name>
```

---

### 3. Check repository status

```bash
git status
```

---

### 4. Get latest changes

```bash
git pull
```

---

### 5. Add your changes

```bash
git add <file-or-directory>
```

To add all changes:

```bash
git add .
```

---

### 6. Commit your changes

```bash
git commit -m "<commit-message>"
```

Replace `<commit-message>` with a short description of your change.

---

### 7. Send changes to the repository

```bash
git push
```

---

## Verify

Check that:

- your changes are committed:

```bash
git status
```

- your branch is up to date:

```bash
git log -n 3
```

---

## Troubleshooting

### Nothing to commit

Possible causes:

- no changes were made
- changes were not added

Check:

```bash
git status
```

---

### Push rejected

Possible causes:

- remote repository has new changes
- you need to pull before pushing

Run:

```bash
git pull
```

then retry:

```bash
git push
```

---

### Authentication failed

Possible causes:

- incorrect credentials
- authentication method not configured

---

## Related pages

- [Clone a repository](clone-a-repository.md)
- [Create a repository](create-a-repository.md)
- [UCT GitLab](../../services/research-software/uct-gitlab.md)