
---

## `docs/how-to/storage/mount-rds.md`

```markdown
# Mount RDS

## Overview

Use this guide when you need to access a Research Data Store (RDS) location from a client machine or supported environment.

RDS is used for managed research data storage and shared project access. This guide explains the information you need before mounting and the basic process for getting access working.

For an overview of where RDS fits, see:
- [Storage service](../../services/storage/index.md)
- [Storage comparison](../../reference/storage/storage-comparison.md)

---

## Before you begin

Make sure that:

- the RDS location already exists
- you have been granted access
- you know the path, share name, or mount details you were given
- you know which machine or environment you are mounting from

If the storage has not yet been provisioned, start here:
- [Request storage](request-storage.md)

---

## What you need

Before attempting to mount RDS, confirm the following:

### 1. The storage location

You need the exact storage location or share details provided for your project.

### 2. Your access rights

You must already have permission to access the location.

If access has not been granted yet, mounting will fail even if the path is correct.

### 3. The client environment

Mounting steps depend on where you are accessing the data from, for example:

- a Linux workstation
- a macOS machine
- a Windows machine
- an HPC environment
- a managed institutional machine

The exact method may vary by environment.

---

## General mounting process

The process usually follows this order:

### 1. Confirm access has been provisioned

Do not start with local troubleshooting until you know:
- the storage exists
- your account has been added
- the path or share details are correct

### 2. Use the connection details provided for your environment

Use the method appropriate to your operating system or environment.

This may involve:
- mounting a network share
- connecting through a file browser
- using a command-line mount command
- accessing the location through HPC if it is exposed there

### 3. Verify that the mount is usable

Once mounted, check that you can:
- list files
- create a test file if you have write access
- read existing project data
- access the share again after reconnecting, if persistent mounting is expected

---

## Common issues

### Access denied

Possible causes:
- your account has not yet been added
- the wrong account is being used
- permissions are read-only where write access was expected

### Path not found

Possible causes:
- incorrect share or mount path
- incorrect hostname or service name
- the storage has not yet been provisioned

### Mount succeeds but files are missing

Possible causes:
- you are looking at the wrong location
- you only have access to part of the project space
- the project data has not yet been copied into the location

### Connection works in one environment but not another

Possible causes:
- the storage is only exposed in selected environments
- a different mount method is required on the second system
- network or authentication requirements differ

---

## When to ask for help

Ask for support if:
- you have confirmed the path but still cannot mount it
- you can connect but access is incomplete or incorrect
- the mount works intermittently
- you need the storage exposed in an additional environment

When asking for help, include:
- the name of the project or storage area
- the machine or environment you are using
- the exact error message
- whether you are trying to read, write, or both

---

## Related pages

- [Request storage](request-storage.md)
- [Storage service](../../services/storage/index.md)
- [Storage comparison](../../reference/storage/storage-comparison.md)