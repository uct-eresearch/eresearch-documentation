# Move Data Securely

## What you are trying to do

You want to move data between systems, such as:

- from your local machine to a research environment
- between storage systems
- between institutions or collaborators

This requires choosing an appropriate transfer method based on data size, location, and reliability requirements.

---

## Key decisions

Before transferring data, clarify:

### How large is the data?

- small files
- medium datasets
- large datasets (100s of GB or more)

### Where is the data moving?

- local machine to UCT systems
- between internal systems
- between institutions

### How reliable does the transfer need to be?

- one-off transfer
- repeated or ongoing transfers
- transfers that must be monitored or resumed if interrupted

---

## Recommended path

### 1. Choose an appropriate transfer method

Start here:
- [Data transfer](../services/data-transfer/index.md)

Understand available approaches:
- [Data transfer methods](../reference/data-transfer/methods.md)

---

### 2. Perform the transfer

Use the appropriate method:

- [Move data](../how-to/data-transfer/move-data.md)

For specific tools:

- [Transfer with Globus](../how-to/data-transfer/transfer-with-globus.md)
- [Transfer with Nextcloud](../how-to/data-transfer/transfer-with-nextcloud.md)

---

### 3. Verify the transfer

After transfer:

- confirm that all files are present
- check file sizes where relevant
- ensure the data is accessible in the target system

---

## Related tasks

- [Store and share research data](store-and-share-research-data.md)
- [Run large-scale analysis](run-large-scale-analysis.md)