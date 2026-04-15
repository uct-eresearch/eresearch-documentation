# Data transfer

## What this service is

UCT provides several tools to move research data securely between systems, collaborators, and storage environments.

These tools support:
- transferring data to and from HPC
- sharing data with collaborators (internal and external)
- moving large datasets between systems
- receiving data securely from external parties

No single tool fits all use cases — the right choice depends on:
- data size
- who you are sharing with
- how often you need to transfer data
- whether automation or scale is required

---

## Who this is for

Data transfer services are relevant if you:

- need to move data to or from HPC
- are collaborating with others on shared datasets
- need to send or receive large files
- work across multiple storage systems (e.g. RDS, cloud storage)

---

## Available tools

### Nextcloud

Nextcloud is a web-based platform for managing and sharing data.

Best for:
- sharing files with collaborators
- receiving files securely (FileDrop)
- managing data across multiple storage systems
- simple, browser-based access

Key characteristics:
- accessible via web browser
- integrates with storage systems (e.g. RDS, OneDrive)
- supports secure sharing links and controlled access

⚠️ Important:  
Nextcloud is **not a storage service**.  
It provides a **collaboration and sharing interface** on top of existing storage.

---

### Globus (and similar tools)

Globus is designed for large-scale, system-to-system data transfer.

Best for:
- transferring large datasets
- moving data between HPC systems
- automated or repeated transfers
- high-performance, reliable transfers

Key characteristics:
- requires setup on both source and destination systems
- optimised for speed and reliability
- suitable for research-scale data movement

---

### Other tools

Depending on your workflow, you may also use:

- **Command-line tools (e.g. `scp`, `rsync`)**  
  → for direct transfers between systems  

- **Cloud-based tools (e.g. Microsoft services)**  
  → for transferring data within cloud environments  

These are typically used for more technical or specialised workflows.

---

## Choosing the right tool

Use this as a quick guide:

- **Use Nextcloud if:**
  - you need to share files with collaborators
  - you want a simple, web-based interface
  - external users need to upload data (FileDrop)
  - ease of use is more important than scale

---

- **Use Globus if:**
  - your data is large
  - you are transferring between systems (e.g. HPC ↔ storage)
  - you need reliable, high-speed transfers
  - you are working with repeated or automated workflows

---

- **Use command-line tools if:**
  - you are comfortable with the terminal
  - transfers are small to moderate
  - you need direct control over file movement

---

If you are unsure:
→ [Choose the right service](../../start-here/choose-the-right-service.md)

---

## How data transfer fits with other services

Data transfer is part of a broader workflow:

- **RDS (Research Data Store)**  
  → store and manage your data  

- **HPC**  
  → run analysis on your data  

- **Nextcloud**  
  → share and manage data access  

- **Globus**  
  → move large datasets between systems  

These tools are often used together.

---

## Common patterns

### Sharing data with collaborators
- store data on RDS  
- share access directly or via Nextcloud  

---

### Receiving data from external users
- use Nextcloud FileDrop  
- optionally connect to RDS for storage  

---

### Moving data to HPC
- transfer data using Globus or command-line tools  
- store persistent data on RDS  

---

### Managing data across systems
- use Nextcloud to connect multiple storage backends  
- use Globus for large transfers between them  

---

## What this service does not provide

- long-term storage (use RDS or archival services)  
- data analysis or computation (use HPC)  
- backup (depends on underlying storage system)  

---

## When to use data transfer tools

Use these tools when:
- data needs to move between systems or people
- collaborators need access to files
- workflows involve multiple environments (local, HPC, cloud)

---

## Get started

To begin:

- → [Transfer data using Globus](../../how-to/storage/transfer-data-using-globus.md)

---

## Related tasks

- → [Move data securely](../../tasks/move-data-securely.md)  
- → [Store and share research data](../../tasks/store-and-share-research-data.md)

---

## Need help?

- → [Support](../../support/index.md)