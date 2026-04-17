# HPC Storage and File Systems

## Purpose

This page describes the file systems available in the HPC environment and how they behave.

It covers:

- the different storage areas available
- how they are intended to be used
- key constraints such as performance and data persistence

This page does not provide instructions for managing files.

---

## Overview

The HPC system provides multiple file systems.

These are designed for different roles within a research workflow and are not interchangeable.

The main file systems are:

- home directories
- project spaces
- scratch storage

---

## Home directories

Home directories are allocated to individual users.

### Characteristics

- small storage allocation
- intended for personal files
- suitable for code, scripts, and configuration
- typically persistent

### Constraints

- not intended for large datasets
- limited capacity compared to other file systems

---

## Project spaces

Project spaces are shared storage areas for research groups.

### Characteristics

- accessible to multiple users within a project
- larger capacity than home directories
- used for active research data

### Constraints

- shared across a group
- subject to allocation limits
- performance is suitable for general workflows but not optimised for temporary high-throughput workloads

---

## Scratch storage

Scratch storage is temporary, high-performance storage.

### Characteristics

- optimised for fast read/write operations
- suitable for active computation and intermediate data
- typically provides the highest performance of the available file systems

### Constraints

- not persistent
- data may be deleted automatically according to system policies
- not backed up

---

## Key distinctions

| Feature | Home | Project | Scratch |
|--------|------|---------|---------|
| Intended use | Personal files | Shared project data | Temporary working data |
| Persistence | Yes | Yes | No |
| Performance | Standard | Standard | High |
| Capacity | Small | Medium to large | High (temporary) |
| Sharing | Individual | Group | Limited |

---

## Data persistence and lifecycle

Different file systems have different expectations for how long data is retained:

- home and project spaces are intended for ongoing use
- scratch storage is temporary and may be cleared automatically

Users are responsible for ensuring that important data is stored in appropriate locations.

---

## Relationship to other storage systems

HPC file systems are part of the compute environment.

They are distinct from:

- managed research storage systems
- synchronisation and sharing tools

For comparison across storage systems, see:

- [Storage comparison](../storage/storage-comparison.md)

---

## Working with files

To manage files within these storage locations, see:

- [Manage files and storage](../../how-to/hpc/manage-files-and-storage.md)