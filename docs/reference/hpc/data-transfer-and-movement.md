# Data transfer and movement (HPC)

## What this page covers

This page explains how data moves into, within, and out of the HPC environment.

It focuses on:

- how data transfer works conceptually
- constraints and performance considerations
- common patterns and trade-offs

It does **not** provide step-by-step instructions.

---

## Why data transfer matters

Data transfer is often the **hidden bottleneck** in research workflows.

Poor transfer strategies can:

- slow down analysis significantly
- overload shared systems
- cause failed or incomplete jobs
- create unnecessary duplication of data

Efficient data movement is essential for:

- reproducibility
- performance
- responsible use of shared infrastructure

---

## Types of data movement

### 1. Ingress (data into HPC)

Moving data from:

- personal machines (laptops/desktops)
- institutional storage (e.g. network drives)
- external systems (cloud, collaborators)

Typical use cases:

- uploading input datasets
- staging data before computation

---

### 2. Internal movement (within HPC)

Moving data between:

- directories
- storage tiers (e.g. home vs scratch)
- compute nodes and storage systems

Typical use cases:

- preparing data for jobs
- reorganising outputs
- optimising I/O performance

---

### 3. Egress (data out of HPC)

Moving data from HPC to:

- local machines
- institutional storage
- external collaborators or repositories

Typical use cases:

- retrieving results
- archiving outputs
- sharing datasets

---

## Key concepts

### Bandwidth vs latency

- **Bandwidth**: how much data can be transferred per unit time  
- **Latency**: delay before transfer begins

Large files benefit from high bandwidth.  
Many small files are heavily affected by latency.

---

### File size and structure

Performance depends strongly on how data is organised:

- **Few large files** → generally efficient  
- **Many small files** → slow and inefficient  

This is especially important on shared filesystems.

---

### Network boundaries

Data movement crosses different network zones:

- local machine ↔ campus network  
- campus network ↔ HPC environment  
- HPC ↔ external systems  

Each boundary may introduce:

- bandwidth limits
- security controls
- authentication requirements

---

### Transfer nodes vs login nodes

HPC systems often distinguish between:

- **Login nodes**  

  - intended for light interaction  
  - not designed for heavy data transfer  

- **Transfer nodes (if available)**  

  - optimised for data movement  
  - designed to handle large transfers efficiently  

Using the wrong node type can degrade performance for all users.

---

### Shared filesystems

HPC environments typically use shared storage systems.

Implications:

- many users access the same storage simultaneously  
- metadata operations (e.g. listing files) can be expensive  
- large numbers of small files can degrade performance  

---

## Common data transfer protocols

Different protocols are suited to different use cases:

- **SCP / SFTP**  
  - simple, widely available  
  - suitable for smaller transfers  

- **rsync**  
  - efficient for incremental updates  
  - reduces redundant data transfer  

- **Globus (if available)**  
  - optimised for large-scale, reliable transfers  
  - handles retries and parallelism  

Each protocol has trade-offs in:

- performance
- reliability
- ease of use

---

## Performance considerations

### Many small files

This is one of the most common performance problems.

Issues:

- high overhead per file  
- slow transfer speeds  
- heavy load on filesystem metadata  

Common mitigation approach:

- aggregate files before transfer (e.g. archive)

---

### Large datasets

Challenges:

- long transfer times  
- potential interruptions  

Considerations:

- use tools that support resuming transfers  
- minimise repeated transfers of unchanged data  

---

### Parallel vs sequential transfer

Some tools support parallel transfer:

- can improve throughput  
- may increase load on shared systems  

Balance is required to avoid impacting other users.

---

## Data staging patterns

### Stage-in → compute → stage-out

A common HPC workflow:

1. transfer data into HPC (stage-in)  
2. run compute jobs  
3. transfer results out (stage-out)  

---

### Use of scratch storage

Temporary (scratch) storage is often:

- faster  
- optimised for computation  

Typical pattern:

- move data to scratch before running jobs  
- write outputs to scratch  
- move final results to long-term storage  

---

## Constraints and policies

Data transfer is subject to system constraints:

- network bandwidth limits  
- fair usage policies  
- storage quotas  
- security and access controls  

Users are expected to:

- avoid excessive or unnecessary transfers  
- use appropriate tools for the task  
- minimise impact on shared infrastructure  

---

## Common pitfalls

- transferring large datasets via login nodes  
- repeatedly copying the same data  
- working with many small files without aggregation  
- ignoring storage location (e.g. not using scratch)  
- assuming local-machine performance applies to HPC  

---

## Relationship to other documentation

- **Services → Data transfer**  
  Overview of available tools and when to use them  

- **How-to → Data transfer**  
  Step-by-step instructions for specific tools  

- **Reference → Storage and file systems**  
  Details on how storage is structured and behaves  

---

## Summary

Effective data transfer in HPC requires understanding:

- where data is moving (ingress, internal, egress)  
- how it is structured (file size and layout)  
- which systems and constraints apply  

Good data movement practices:

- improve performance  
- reduce system load  
- support reproducible research workflows  