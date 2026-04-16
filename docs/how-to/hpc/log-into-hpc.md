# Log into HPC

## Overview

Connect to the HPC system using SSH from your local machine.

---

## Before you begin

Make sure:

- you have an HPC account
- you know your HPC username
- you have network access to the HPC system
- you have an SSH client installed (Linux, macOS, or Windows with SSH support)

---

## Steps

### 1. Open a terminal

On your local machine, open a terminal application.

---

### 2. Connect using SSH

Run the following command:

```bash
ssh <username>@hpc.uct.ac.za
```

Replace `<username>` with your HPC username.

---

### 3. Enter your password

When prompted:

- enter your HPC password
- press Enter

Note:
- no characters will appear while typing the password
- this is normal behaviour

---

### 4. Confirm login

After successful login, you should see:

- a welcome message or system notice
- a command prompt on the HPC system

---

## Verify

Confirm that you are connected to the HPC system:

```bash
hostname
```

The output should show the name of an HPC login node.

You can also check your home directory:

```bash
pwd
```

---

## Troubleshooting

### Permission denied

Possible causes:

- incorrect username
- incorrect password
- account not yet activated

---

### Connection timed out

Possible causes:

- no network access
- VPN required but not connected
- incorrect hostname

---

### Command not found: ssh

Possible cause:

- SSH client is not installed or not available in your environment

---

## Related pages

- [Submit a job](submit-a-job.md)
- [Use modules](use-software-modules.md)
- [Use GPUs](use-gpus.md)