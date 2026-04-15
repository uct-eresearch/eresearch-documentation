# Clone a Repository

## Overview

Download a copy of a repository from GitLab to your local machine.

---

## Before you begin

Make sure:

- you have access to the repository
- you have the repository URL
- Git is installed on your system

---

## Steps

### 1. Open a terminal

Open a terminal on your local machine.

---

### 2. Choose a location

Navigate to the directory where you want the repository:

```bash
cd <target-directory>
```

---

### 3. Clone the repository

```bash
git clone <repository-url>
```

Replace `<repository-url>` with the URL provided by GitLab.

---

### 4. Enter the repository directory

```bash
cd <repository-name>
```

---

## Verify

Check that:

- the directory was created:

```bash
ls
```

- files are present:

```bash
ls
```

- the repository is connected:

```bash
git status
```

---

## Troubleshooting

### Permission denied

Possible causes:

- no access to the repository
- authentication not configured

---

### Repository not found

Possible causes:

- incorrect repository URL
- repository does not exist
- access not granted

---

### Command not found: git

Possible cause:

- Git is not installed or not available in your environment

---

## Related pages

- [Create a repository](create-a-repository.md)
- [Sync a repository](sync-repository.md)
- [UCT GitLab](../../services/research-software/uct-gitlab.md)