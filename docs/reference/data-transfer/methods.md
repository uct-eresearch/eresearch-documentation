# Data Transfer Methods

## Purpose

This page describes common methods used to move research data between systems.

It is a reference page, not a setup guide. Use it to understand the role, strengths, and limitations of each method.

For task-oriented guidance, see:
- [Move data securely](../../tasks/move-data-securely.md)
- [Data transfer](../../services/data-transfer/index.md)

---

## Main categories

Data transfer methods used in research workflows usually fall into three broad categories:

| Category | Typical methods | Best suited for |
|----------|------------------|-----------------|
| Managed transfer services | Globus | Large or important transfers between systems |
| Command-line transfer tools | `scp`, `rsync`, `sftp` | Direct transfers where shell access is available |
| Sync and sharing platforms | Nextcloud | User-facing sharing and synchronisation |

These methods are not interchangeable. The appropriate method depends on scale, reliability requirements, environment, and collaborator access.

---

## Managed transfer services

### Globus

Globus is designed for reliable, high-volume transfer between connected systems and endpoints.

#### Characteristics

- built for large-scale data movement
- supports monitored and restartable transfers
- suitable for institution-to-institution workflows
- reduces the need to keep an interactive session open during long transfers

#### Best suited for

- large datasets
- repeated transfers between systems
- transfers that need better reliability than ad hoc command-line copying
- movement between storage systems and supported institutional endpoints

#### Limitations

- requires appropriate endpoint availability
- not itself a storage system
- may require service-specific setup or institutional support

---

## Command-line transfer tools

### SCP

`scp` copies files directly over SSH.

#### Characteristics

- simple and widely available
- useful for direct copy operations
- suited to smaller or straightforward transfers

#### Best suited for

- one-off transfers
- moving individual files or small groups of files
- environments where SSH access is already available

#### Limitations

- less suitable for very large or fragile transfers
- limited transfer resilience compared with managed services
- not ideal for repeated synchronisation workflows

---

### rsync

`rsync` synchronises files between locations and transfers only changed content where possible.

#### Characteristics

- efficient for repeated transfers
- useful for keeping directories in sync
- commonly used over SSH

#### Best suited for

- updating an existing copy of a dataset
- repeated transfers where only some files change
- mirroring directory structures

#### Limitations

- requires more care than simple copy tools
- still depends on command-line access and correct usage
- not a storage system or collaboration platform

---

### SFTP

SFTP provides file transfer over SSH using an interactive file transfer model.

#### Characteristics

- widely supported
- suitable for file-by-file movement
- often available in GUI clients as well as command-line tools

#### Best suited for

- simple transfer workflows
- users who prefer a file transfer interface over shell commands
- environments where SSH-based access is available

#### Limitations

- not optimised for very large-scale transfer workflows
- less efficient than `rsync` for repeated synchronisation

---

## Sync and sharing platforms

### Nextcloud

Nextcloud provides file access, synchronisation, and sharing.

#### Characteristics

- web and desktop-client access
- synchronisation across devices
- sharing with internal or external collaborators

#### Best suited for

- collaborative document exchange
- smaller research files
- workflows that require user-friendly sharing

#### Limitations

- not a primary research storage system
- not suitable for high-performance workflows
- not appropriate for large dataset movement at scale

For more detail, see:
- [Nextcloud](nextcloud.md)

---

## Choosing between methods

| Need | Most suitable method |
|------|----------------------|
| Move a very large dataset reliably between systems | Globus |
| Copy a small number of files over SSH | SCP |
| Keep two directories in sync over time | rsync |
| Share files with collaborators through a user-facing interface | Nextcloud |

---

## Important distinction

Data transfer methods move data between systems.

They do not all provide:
- durable storage
- authoritative data management
- collaboration controls
- compute-local performance

Those functions are provided by storage and access services, not by transfer methods alone.

---

## Related pages

- [Data transfer](../../services/data-transfer/index.md)
- [Move data securely](../../tasks/move-data-securely.md)
- [Nextcloud](nextcloud.md)
- [Storage comparison](../storage/storage-comparison.md)