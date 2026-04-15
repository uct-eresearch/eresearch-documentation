# High Performance Computing (HPC)

## Run large-scale analyses on shared compute infrastructure

The UCT High Performance Computing (HPC) service provides access to powerful shared computing resources for running large-scale, compute-intensive research workloads.

It is designed for workloads that go beyond what a personal computer or standard server can handle.

---

## When to use HPC

Use HPC if you need to:

- run long or computationally intensive analyses  
- process large datasets  
- run parallel or batch workloads  
- use specialised resources such as GPUs  

If your work involves small datasets, interactive analysis, or simple scripting, HPC is likely not necessary.

---

## How HPC works (in brief)

HPC is a shared system where:

- you connect to a **login node** to prepare your work  
- you submit jobs to a **scheduler**  
- your jobs run on **compute nodes**  
- results are written to shared storage  

Work is not run directly on the login node. Instead, all compute-intensive tasks are submitted as jobs.

→ See technical details: `Reference > HPC > Scheduler and job submission`

---

## What HPC supports

HPC supports a wide range of research workloads, including:

- simulations and modelling  
- data analysis pipelines  
- machine learning and AI workloads  
- batch processing of large datasets  

Work is typically done via the command line in a Linux environment.

---

## Storage on HPC

HPC provides two main storage areas:

- `/home` for code and small files  
- `/scratch` for active computations and temporary data  

You should run jobs using data in `/scratch` and move important results to long-term storage when complete.

→ See full details: `Reference > HPC > Storage and file systems`

---

## GPUs and specialised resources

Some HPC resources, such as GPUs, are not enabled by default and may require a request or approval process.

→ See details: `Reference > HPC > GPU access and partitions`

---

## How HPC fits into your workflow

HPC is typically used alongside other services:

- **RDS** → for long-term storage of research data  
- **Data transfer tools** → to move data to and from HPC  
- **GitLab** → for version control and collaboration on code  

A typical workflow:
1. develop code locally or in GitLab  
2. transfer data to HPC  
3. run analysis on HPC  
4. move results to RDS or another storage system  

---

## Getting started

To begin using HPC:

- apply for access  
- connect to the system  
- prepare and submit your first job  

→ See:
- `How-to > Log into HPC`
- `How-to > Submit your first job`

---

## Important considerations

HPC is a shared resource. This means:

- resources are allocated through a scheduler  
- usage must follow service policies  
- misuse (e.g. running heavy workloads on login nodes) may result in restrictions  

→ See: `Reference > HPC > Policies and service conditions`

---

## Need help?

If you need assistance with:

- access or accounts  
- troubleshooting jobs  
- software availability  

→ See: `Support`