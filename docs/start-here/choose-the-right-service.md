# Choose the right service

## What this page helps you do

Research workflows often involve multiple tools for storage, transfer, computation, and collaboration.

This page helps you:
- choose the right service for your specific need
- understand the differences between available options
- avoid common mistakes (e.g. using the wrong tool for the job)

If you already know what you need to do, go to **Tasks**.  
If you want full details about a specific system, go to **Services**.

---

## Start with your need

Use the scenarios below to guide your decision.

### I need to store active research data
- Use **Research Data Store (RDS)**  
  - high-performance, on-premise storage  
  - designed for large datasets  
  - integrates directly with HPC  
  - supports secure access and collaboration  

→ See: Services → Research data storage

---

### I need to run large-scale analysis
- Use **HPC (High Performance Computing)**  
- Store your data on **RDS** if:
  - datasets are large
  - you exceed HPC scratch limits
  - you need persistent storage between jobs

→ See: Tasks → Run large-scale analysis

---

### I need to share data with collaborators
- For structured collaboration:
  - use **RDS** (with controlled access)

- For easy sharing or external uploads:
  - use **Nextcloud** (FileDrop or share links)

⚠️ Nextcloud is **not a storage system** — it is a collaboration interface connected to storage.

→ See: Services → Data transfer / Nextcloud

---

### I need to transfer data securely
- Use:
  - **Nextcloud** for simple sharing and uploads
  - **Globus** (or similar tools) for large-scale transfers

→ See: Tasks → Move data securely

---

### I need long-term or archival storage
- Use:
  - **Tape storage** or **DIRISA** for archival
- Do **not** use RDS for long-term inactive data

---

### I need to publish or share final datasets
- Use:
  - **ZivaHub** (for DOI and publication)

---

### I need simple file storage and collaboration
- Use:
  - **Microsoft OneDrive / SharePoint**

Best for:
- small to medium datasets
- document collaboration

Not suitable for:
- large-scale research data
- HPC workflows

---

## Compare your options

Use this table to quickly compare common storage and data options.

| Option | Best for | Backup | POPIA compliant | Notes |
|--------|----------|--------|-----------------|------|
| **RDS** | Active research data | Yes | Yes | High performance, HPC integration |
| **Tape storage** | Archival | Yes | Yes | Not for active use |
| **OneDrive / SharePoint** | Collaboration | No (sync only) | Yes | Quotas apply |
| **DIRISA** | National archive | Replication | Yes | No backup |
| **ZivaHub** | Publishing | Yes | Yes | Generates DOI |
| **Google Drive** | General use | No | No | Not recommended for research data |

---

## Key decision rules

Use these simple rules to guide your choices:

### Use RDS when:
- your data is large or growing
- you need high performance
- you are working with HPC
- your data must remain in South Africa (POPIA)

---

### Use Nextcloud when:
- you need to share or receive files
- you want a simple web interface to manage data
- you are working across multiple storage systems

⚠️ Always store the data itself in RDS, OneDrive, or another storage system.

---

### Use OneDrive / SharePoint when:
- your data is small to moderate
- you need simple collaboration
- HPC and high performance are not required

---

### Use DIRISA or Tape when:
- the data is no longer actively used
- you need long-term retention
- cost needs to be minimised

---

## Important concepts (avoid common mistakes)

### Nextcloud is not storage
Nextcloud is a **management and sharing layer**.  
It connects to storage systems like RDS or OneDrive — it does not replace them.

---

### Backup vs replication vs archive
- **Backup** → protects against data loss and human error  
- **Replication** → copies data, but does not preserve history  
- **Archive** → long-term storage for compliance and retention  

These are not interchangeable.

---

### Cloud is not always cheaper
Some cloud services:
- charge for data transfer (egress)
- do not include backup
- have changing quotas

RDS uses a transparent cost-recovery model with no hidden fees.

---

## What to do next

- Explore **Tasks** if you know what you want to do  
- Explore **Services** to understand specific platforms  
- Go to **Support** if you are unsure or need help choosing  