# Nextcloud

## Purpose

This page describes Nextcloud as a system used for file access, synchronisation, and sharing.

It covers:
- how Nextcloud is structured
- how data is accessed and synchronised
- key characteristics of the platform

This page does not provide instructions for using Nextcloud.

---

## Overview

Nextcloud is a file synchronisation and sharing platform.

It provides a user-facing interface for accessing and managing files stored on server-side infrastructure.

Users interact with Nextcloud through:

- a web interface
- desktop synchronisation clients
- mobile applications

---

## Data model

Nextcloud manages files within a central storage system.

Data is:

- stored on server-side infrastructure
- accessed through user accounts
- synchronised across connected devices

Files may exist as:

- server-side copies
- synchronised local copies on user devices

---

## Access model

Access to data is controlled through:

- user authentication
- permissions assigned to files and directories
- sharing mechanisms between users

Access may be:

- individual (private files)
- shared within groups
- shared externally via links or permissions

---

## Synchronisation

Nextcloud supports file synchronisation between:

- server storage
- user devices

Changes made in one location are propagated to other connected devices.

Synchronisation behaviour depends on:

- client configuration
- network connectivity
- file size and structure

---

## Key characteristics

### User-facing access

- provides a graphical interface for file interaction
- accessible from multiple device types

### Sharing

- supports file and directory sharing
- enables controlled access through permissions and links

### Synchronisation

- maintains consistency between server and client copies
- allows files to be accessed across devices

### Performance

- suitable for general file access and collaboration
- not optimised for high-performance or large-scale data workflows

---

## Relationship to other systems

Nextcloud is part of the broader research data environment.

It is distinct from:

- storage systems that manage authoritative research data
- compute-attached file systems
- data transfer tools used for system-to-system movement

For comparison across systems, see:

- [Storage comparison](../storage/storage-comparison.md)

---

## Working with Nextcloud

To transfer or access files using Nextcloud, see:

- [Transfer with Nextcloud](../../how-to/data-transfer/transfer-with-nextcloud.md)