# Run Large-Scale Analysis

## What you are trying to do

You want to run analysis that exceeds the capacity of a local machine.

This typically involves:

- using shared compute infrastructure
- running jobs in a managed environment
- working with larger datasets or longer-running processes

---

## Key decisions

Before starting, clarify:

### What type of workload are you running?

- batch processing
- parallel or distributed workloads
- GPU-accelerated computation

### How large is the data?

- data that fits locally
- large datasets requiring shared storage
- data generated during computation

### How will the analysis run?

- short interactive runs
- long-running jobs
- repeated or automated workflows

---

## Recommended path

### 1. Use an appropriate compute service

Start here:

- [HPC service](../services/hpc/index.md)

---

### 2. Prepare your data

Ensure that:

- your data is available in the compute environment
- input and output locations are clearly defined

If data needs to be moved:

- [Move data securely](move-data-securely.md)

---

### 3. Run your analysis

Submit and manage your workload using the appropriate tools:

- [Submit a job](../how-to/hpc/submit-a-job.md)

If needed:

- [Use GPUs](../how-to/hpc/use-gpus.md)
- [Use modules](../how-to/hpc/use-software-modules.md)

---

### 4. Retrieve and manage results

After the analysis:

- retrieve output data
- store results in an appropriate location
- share results if required

---

## Related tasks

- [Store and share research data](store-and-share-research-data.md)
- [Move data securely](move-data-securely.md)