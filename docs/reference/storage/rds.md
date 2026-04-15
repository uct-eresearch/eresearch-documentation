# Research Data Store (RDS)

## Purpose

This page describes the Research Data Store (RDS) and how it behaves as a storage system.

It covers:
- the role of RDS in research workflows
- how data is organised and accessed
- key characteristics such as persistence and sharing

This page does not provide instructions for accessing or using RDS.

---

## Overview

The Research Data Store (RDS) is a managed storage system for research data.

It provides shared storage that can be accessed by individuals and research groups across different environments.

RDS is designed to support ongoing research activities where data needs to be retained and accessed over time.

---

## Data organisation

RDS is typically structured around:

- project or group-based storage areas
- shared directories accessible to multiple users
- controlled access based on project membership

Data is organised to support collaboration within a research project.

---

## Access model

RDS is accessible from multiple environments, which may include:

- institutional systems
- research compute environments
- user workstations (depending on configuration)

Access is managed through permissions assigned to users or groups.

---

## Key characteristics

### Persistence

- RDS is intended for ongoing storage of research data
- data is retained according to system policies

### Sharing

- supports group-based access
- multiple users can read and write within shared project spaces

### Performance

- suitable for general research data access
- not optimised for high-performance, compute-intensive workloads

### Capacity

- designed for medium to large datasets
- subject to allocation limits and quotas

---

## Data management responsibilities

Users are responsible for:

- organising data within project spaces
- managing access within their research group (where applicable)
- ensuring that data is stored in appropriate locations for its use

---

## Relationship to other systems

RDS is one component of the broader research data environment.

It is distinct from:

- compute-attached file systems used during analysis
- synchronisation and sharing platforms
- data transfer tools

For comparison across systems, see:

- [Storage comparison](storage-comparison.md)

---

## Working with RDS

To request or access RDS storage, see:

- [Request storage](../../how-to/storage/request-storage.md)
- [Mount RDS](../../how-to/storage/mount-rds.md)