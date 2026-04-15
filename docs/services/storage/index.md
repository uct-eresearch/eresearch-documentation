# Storage

## Choose the right storage for your research

Research data storage is not one-size-fits-all.

The right choice depends on:
- how actively the data is used
- how much data you have
- whether it contains sensitive information
- whether it needs to integrate with compute (e.g. HPC)
- how long it needs to be retained

UCT provides multiple storage options to support different stages of the research lifecycle.

---

## Storage options at UCT

### Research Data Store (RDS)

**Best for:** Active research data, large datasets, HPC workflows

- On-premise, secure storage located at UCT
- POPIA compliant (data remains in South Africa)
- High performance (low latency, high bandwidth)
- Scalable as projects grow
- Integrated with HPC
- Reliable backup and disaster recovery

Use RDS when your data is:
- large or growing
- actively analysed
- sensitive or compliance-bound
- part of compute workflows

→ See `reference/storage/rds.md`

---

### Tape storage (long-term)

**Best for:** Archival storage, infrequently accessed data

- Lower cost than RDS
- Designed for long-term retention
- Not suitable for active analysis or frequent access

Use tape when:
- the project is complete
- data must be retained but not actively used

---

### Microsoft OneDrive / SharePoint

**Best for:** Collaboration and lightweight storage

- Cloud-based storage within UCT’s Microsoft environment
- Suitable for documents and small-to-medium datasets
- Easy sharing within and outside UCT
- Subject to quotas and sync limitations

Use OneDrive/SharePoint when:
- collaboration is the primary need
- data volumes are modest
- HPC integration is not required

---

### DIRISA (national infrastructure)

**Best for:** No-cost storage where replication is sufficient

- National research infrastructure
- Free to use
- Provides replication (not full backup)
- Limited direct integration with UCT workflows

Use DIRISA when:
- budget is constrained
- replication is sufficient for your needs
- institutional integration is not critical

---

### ZivaHub

**Best for:** Publishing and sharing research outputs

- Open data repository
- Assigns DOIs to datasets
- Supports long-term access and citation

Use ZivaHub when:
- your data is ready to be shared or published
- you want to support reproducibility and reuse

---

## How to choose

Use this simple framing:

- **Active + large + compute-intensive → RDS**
- **Inactive but must be retained → Tape**
- **Collaborative + lightweight → OneDrive / SharePoint**
- **No budget → DIRISA (with limitations)**
- **Publishing outputs → ZivaHub**

If your needs span multiple categories, you will likely use more than one service.

---

## What we need to advise you

Before recommending a storage solution, we typically need to understand:

- What type of data are you working with?
- How much data do you need to store?
- How long will it need to be retained?
- Does the data contain personal or sensitive information?
- Do you need active access or long-term preservation only?
- Will collaborators need access (internal or external)?
- Is there funding available for storage?

→ See `how-to/storage/request-storage.md`

---

## Storage and your workflow

Storage is part of a broader research workflow.

You may also need:
- **Data transfer tools** → see `services/data-transfer/`
- **Compute resources (HPC)** → see `services/hpc/`
- **Guidance on managing research data** → see `good-practice/`

---