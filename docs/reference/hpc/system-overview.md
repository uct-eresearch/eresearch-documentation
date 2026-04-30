# HPC system overview

This page describes the core technical characteristics of the UCT High Performance Computing (HPC) environment.

---

## Core system specifications

| Component | Details |
|----------|--------|
| **Architecture** | x86_64 |
| **Operating system** | Rocky Linux 9.7 (Blue Onyx) |
| **Kernel** | Linux 5.14.0-611.47.1.el9_7.x86_64 |
| **Scheduler** | SLURM 23.11.5 |
| **Parallel libraries** | OpenMPI, MPICH, PMI2, PMIx5 |

---

## System components

### Architecture

The system uses a 64-bit x86 architecture (x86_64), which is standard for modern HPC environments and supports a wide range of scientific software.

---

### Operating system

Rocky Linux 9.7 provides the base software environment for the cluster. This determines compatibility for compiled software, libraries, and system tools.

---

### Kernel

Linux kernel version:

5.14.0-611.47.1.el9_7.x86_64


The kernel manages hardware resources, process scheduling, and system performance.

---

### Scheduler

SLURM (23.11.5) is used to manage all compute workloads.

It is responsible for:
- allocating compute resources
- queuing and prioritising jobs
- managing job execution across nodes

See [Scheduler and job submission](scheduler-and-job-submission.md) for detailed reference information.

---

### Parallel libraries

The system provides multiple parallel computing libraries:

- **OpenMPI**
- **MPICH**
- **PMI2**
- **PMIx5**

These libraries support distributed computing across multiple nodes and are typically used for MPI-based workloads.

See [Software and modules](software-and-modules.md) for details on how these are made available.

---

## Notes

- All compute jobs are executed via the scheduler; direct execution on compute nodes is not supported.
- Software compatibility depends on the operating system and available modules.
- Parallel libraries enable scaling workloads beyond a single node.

---

## Related reference pages

- [Scheduler and job submission](scheduler-and-job-submission.md)
- [Software and modules](software-and-modules.md)
- [Storage and file systems](storage-and-file-systems.md)