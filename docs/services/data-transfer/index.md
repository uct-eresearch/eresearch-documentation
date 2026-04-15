# Data transfer

## What this service is

Data transfer provides the tools and methods for moving research data between:

- your local machine and UCT systems
- storage systems and HPC
- UCT and external collaborators or institutions

This service helps you choose the **right transfer method for your data size, workflow, and collaborators**.

---

## When to use this service

Use data transfer when you need to:

- move data onto HPC for analysis
- retrieve results from compute environments
- share datasets with collaborators
- receive data from external partners
- synchronise data between systems
- move large volumes of data reliably and securely

If your data does not need to move between systems, you likely only need storage.

→ See [Storage](../storage/index.md)

---

## Transfer options at UCT

Different tools are appropriate depending on scale, complexity, and workflow.

### Nextcloud

**Best for:** Simple sharing, secure uploads, browser-based access

- Web-based interface available to all UCT users
- Supports sharing via links
- Supports secure upload (FileDrop) from external collaborators
- Can connect to storage such as RDS

Use Nextcloud when:
- you need to receive files from external collaborators
- you want a simple, browser-based sharing method
- the transfer does not require high-performance or automation

→ See `reference/data-transfer/nextcloud.md`  
→ See `how-to/data-transfer/transfer-with-nextcloud.md`

---

### :contentReference[oaicite:0]{index=0}

**Best for:** Large-scale data transfer, system-to-system workflows

- Designed for high-performance data movement between systems
- Suitable for large datasets (hundreds of GB to TB+)
- Reliable transfer with automatic retries and integrity checks
- Works between configured endpoints (e.g. HPC, storage systems)

Use Globus when:
- you are transferring large datasets
- both source and destination are systems (not just people)
- reliability and performance are critical
- transfers need to run unattended

→ See `how-to/data-transfer/transfer-with-globus.md`

---

### Command-line tools (e.g. rsync, scp, rclone)

**Best for:** Direct control, scripting, and automation

- Run from the command line
- Suitable for repeatable or scripted workflows
- Commonly used for HPC and Linux-based environments

Use command-line tools when:
- you are comfortable working in a terminal
- you need automation or fine-grained control
- the transfer is part of a workflow or pipeline

---

## Choosing a transfer method

Use this as a starting point:

- **Small to medium files, simple sharing → Nextcloud**
- **Large datasets, system-to-system → Globus**
- **Automated or scripted workflows → command-line tools**

If unsure:
- start with Nextcloud for ease of use
- move to Globus when scale or reliability becomes a constraint

---

## How this fits with other services

Data transfer connects directly to:

- [Storage](../storage/index.md) — where your data lives
- [High Performance Computing (HPC)](../hpc/index.md) — where data is processed
- [Research software](../research-software/index.md) — where workflows are defined

Transfer is typically one step in a broader workflow.

---

## Start from your task

If you know what you want to do:

- [Move data securely](../../tasks/move-data-securely.md)
- [Store and share research data](../../tasks/store-and-share-research-data.md)
- [Run large-scale analysis](../../tasks/run-large-scale-analysis.md)

---

## Need more detail?

For concepts and system behaviour:

- `reference/data-transfer/nextcloud.md`
- `reference/hpc/data-transfer-and-movement.md`

---

## Need help?

- [Support overview](../../support/index.md)
- [FAQ](../../support/faq.md)
- [Contact points](../../support/contact-points.md)