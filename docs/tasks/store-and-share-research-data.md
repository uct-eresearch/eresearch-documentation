# Store and share research data

## What this helps you do

This page helps you choose how to store, manage, and share your research data at UCT.

Use it if you are:
- starting a new project and need to decide where data should live
- working with growing datasets
- collaborating with others (inside or outside UCT)
- unsure which storage or sharing option to use

---

## When you need this

You should think about data storage and sharing when:

- your dataset is too large for your laptop or local storage
- you need reliable access to data over time
- you are working with collaborators
- your data must meet funder or legal requirements (e.g. POPIA)
- you need to connect data to HPC for analysis

---

## Your main options at UCT

### Research Data Store (RDS)

Best for:
- active research data
- large or growing datasets
- HPC-connected workflows
- sensitive or regulated data

RDS provides:
- secure, on-premise storage
- high performance and low latency
- integration with HPC
- controlled access for collaborators

→ See: Services → Research data storage

---

### Microsoft OneDrive / SharePoint

Best for:
- small to medium datasets
- document-based collaboration
- lightweight sharing within teams

Limitations:
- not designed for large-scale research data
- no true backup (sync-based)
- not suitable for HPC workflows

→ See: Services → Research data storage

---

### Nextcloud (sharing and collaboration interface)

Best for:
- sharing files with external collaborators
- receiving data securely (FileDrop)
- managing data across multiple storage systems

⚠️ Important:  
Nextcloud is **not a storage system**.  
It connects to storage (such as RDS or OneDrive) and provides a web interface for sharing and collaboration.

→ See: Services → Data transfer

---

### DIRISA / Tape (archival storage)

Best for:
- long-term storage of inactive data
- post-project retention
- reducing storage costs

Not suitable for:
- active analysis
- frequent access

---

## Choosing the right approach

Use this as a quick guide:

- **Use RDS if:**
  - your data is large or growing
  - you need HPC access
  - your data must remain in South Africa
  - you need reliable backup and performance

- **Use OneDrive / SharePoint if:**
  - your data is small to moderate
  - you are mainly working with documents
  - you need simple collaboration

- **Use Nextcloud if:**
  - you need to share or receive files easily
  - you are working with external collaborators
  - you want a simple web-based interface

- **Use DIRISA or Tape if:**
  - the data is no longer actively used
  - you need long-term retention

If you are unsure, start with:
→ [Choose the right service](../start-here/choose-the-right-service.md)

---

## Common combinations

In practice, you will often use more than one service:

- **RDS + HPC**  
  Store large datasets on RDS and analyse them on HPC

- **RDS + Nextcloud**  
  Store data securely on RDS and use Nextcloud to share it with collaborators

- **OneDrive + Nextcloud**  
  Use OneDrive for storage and Nextcloud for controlled sharing

---

## What to do next

Once you’ve chosen your approach:

- Learn about the service:
  - → [Research data storage](../services/storage/index.md)

- Follow step-by-step instructions:
  - → [Transfer data using Globus](../how-to/storage/transfer-data-using-globus.md)

- If working with HPC:
  - → [Run large-scale analysis](run-large-scale-analysis.md)

---

## Good practice

To make your data easier to manage and reuse:

- organise your files clearly
- plan access and permissions early
- separate active and archival data
- ensure your storage choice matches how the data will be used

→ See: [Project structure](../good-practice/project-structure.md)

---

## Need help?

If you are unsure which option is best for your project:

- → [Support](../support/index.md)