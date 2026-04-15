# Nextcloud

## Overview

Nextcloud is a web-based collaboration and file sharing platform available at UCT.

At UCT, Nextcloud should be understood as a **collaboration and data transfer layer**, not as a primary research storage service. It provides a browser-based interface for sharing, receiving, and managing files, and it can connect to other storage systems such as the Research Data Store (RDS).

This makes it useful for collaboration and secure file exchange, especially when researchers need a simpler, more user-friendly interface on top of institutional storage.

---

## What Nextcloud is

Nextcloud is:
- a web-based file management and sharing platform
- available to UCT users with their UCT credentials
- useful for collaboration and secure data transfer
- able to connect to supported storage backends such as SMB/CIFS or SSH-accessible systems

At UCT, it can be used to:
- share files with collaborators
- receive files securely from external parties
- manage files stored on connected backends such as RDS
- provide a more accessible interface for working with institutional storage

---

## What Nextcloud is not

Nextcloud is **not**:
- a primary research storage service
- a replacement for RDS
- a replacement for HPC-connected storage
- a long-term archival service

This distinction is important.

The default Nextcloud allocation is small and should not be treated as the main location for research data. Researchers should store research data in an appropriate storage service such as RDS or Microsoft storage, and use Nextcloud as the interface for sharing, collaboration, or transfer where appropriate.

---

## Access

Nextcloud is available to:
- UCT staff
- UCT students
- approved third-party users with UCT credentials

Access is via UCT login credentials.

---

## Typical use cases

Use Nextcloud when you need:

### Secure file exchange
Nextcloud supports upload-only sharing through FileDrop, which allows external users to upload files to a designated folder without seeing existing contents.

### Web-based access to institutional storage
Researchers can connect external storage and manage files through a browser rather than only through mapped drives or VPN-based desktop access.

### Sharing with collaborators
Nextcloud can generate share links and support controlled access to specific files or folders.

### A simpler interface for storage already hosted elsewhere
Where data is already stored in RDS or another suitable backend, Nextcloud can provide a more convenient interface for browsing and sharing.

---

## Connection to storage backends

Nextcloud can connect to supported external storage systems.

Common examples include:
- RDS via SMB/CIFS
- other endpoints accessible via SSH/SFTP

This means the data may live in another approved storage service while being accessed through the Nextcloud interface.

---

## FileDrop

FileDrop is one of the most useful Nextcloud features for research workflows.

It allows a user to:
- designate a target folder
- generate an upload link
- send that link to an external person
- receive files without exposing the rest of the folder contents

This is useful when:
- collaborators need to send files to UCT researchers
- the sender should not browse other files
- a lightweight alternative to more complex transfer tools is sufficient

---

## Limitations

### Not primary storage
Nextcloud should not be presented as the main storage location for research data.

### Not HPC storage
Nextcloud does not replace storage that must be directly attached to HPC workflows.

### Performance depends on the backend
If Nextcloud is connected to another storage system, the performance experienced through the web interface may differ from direct access.

### Backup depends on where the data actually lives
Backup and recovery depend on the underlying storage backend, not on the fact that the data is visible in Nextcloud.

### Not for long-term preservation
If data needs to be retained or published long-term, other services are more appropriate.

---

## When to recommend Nextcloud

Recommend Nextcloud when:
- researchers need secure upload from external collaborators
- browser-based sharing is more practical than direct filesystem access
- the main storage is elsewhere, but an easier collaboration layer is needed
- the transfer task does not require large-scale system-to-system tooling

---

## When not to recommend Nextcloud

Do not recommend Nextcloud as the primary solution when:
- the main requirement is high-performance active storage
- the workflow depends on HPC-attached storage
- the dataset requires a formal archival or publication destination
- the researcher needs institutional storage rather than an interface layer

---

## Related pages

- `services/data-transfer/index.md`
- `reference/storage/rds.md`
- `how-to/data-transfer/transfer-with-nextcloud.md`