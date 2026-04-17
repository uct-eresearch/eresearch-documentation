# Storage Comparison

## Purpose

This page provides a high-level comparison of how data is stored, accessed, and moved.

It distinguishes between:

- storage systems (where data lives)
- access and synchronisation tools
- data transfer tools

For detailed behaviour and policies, follow the linked reference pages.

---

## System categories

| Category | Description | See |
|----------|-------------|-----|
| Storage (authoritative) | Systems where research data is stored and managed | [Storage service](../../services/storage/index.md) |
| Access and synchronisation | Tools for accessing and sharing data | [Storage service](../../services/storage/index.md) |
| Data transfer | Tools for moving data between systems | [Data transfer](../../services/data-transfer/index.md) |

---

## Comparison

| System | Category | Best for | Not suitable for | See details |
|--------|----------|----------|------------------|-------------|
| HPC file systems (home, project, scratch) | Storage | Compute workflows | External sharing, long-term unmanaged storage | [HPC storage and file systems](../hpc/storage-and-file-systems.md) |
| Research Data Store (RDS) | Storage | Active research data (team access) | High-performance compute workloads | [Storage service](../../services/storage/index.md) |
| Nextcloud | Access / synchronisation | Sharing and collaboration | Large datasets, compute workflows | [Storage service](../../services/storage/index.md) |
| Globus / SCP / rsync | Data transfer | Moving data between systems | Storing data | [Data transfer](../../services/data-transfer/index.md) |

---

## Key distinctions

- Storage systems hold the **authoritative copy of data**
- Access tools provide **user-facing interaction and sharing**
- Transfer tools **move data but do not retain it**

These systems are complementary and should be used together, not interchangeably.

---

## Related pages

- [Storage service](../../services/storage/index.md)
- [Data transfer](../../services/data-transfer/index.md)
- [HPC storage and file systems](../hpc/storage-and-file-systems.md)