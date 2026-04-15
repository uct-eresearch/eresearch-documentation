# Run large-scale analysis

## What this helps you do

This page helps you decide how to run computationally intensive analyses at UCT using High Performance Computing (HPC).

Use it if you:
- need more compute power than your laptop or workstation can provide
- are working with large datasets or long-running analyses
- want to run jobs in parallel or at scale
- need access to GPUs or high-memory systems

---

## When you need this

You should use HPC when:

- your analysis takes too long on a local machine
- your data is too large to process locally
- your workflow requires parallel processing or many cores
- you need specialised compute environments (e.g. GPUs, large RAM)
- you are running repeated or batch jobs

---

## What HPC is (at UCT)

UCT’s HPC is a shared computing cluster made up of:

- a **head node** (where you log in)
- multiple **worker nodes** (where your jobs run)
- shared storage systems (e.g. `/home`, `/scratch`)

You do **not** run analysis directly on the login node.  
Instead, you submit jobs to a scheduler, which runs them on available compute resources. :contentReference[oaicite:0]{index=0}  

Jobs are managed through a scheduling system (e.g. SLURM), which:
- queues jobs
- allocates CPUs, memory, or GPUs
- ensures fair use across researchers :contentReference[oaicite:1]{index=1}  

---

## Your main options at UCT

### HPC (High Performance Computing)

Best for:
- large-scale or compute-intensive analysis
- parallel processing
- long-running jobs
- GPU workloads

Key characteristics:
- Linux-based environment
- command-line driven
- shared infrastructure across researchers
- job-based execution (not interactive by default)

→ See: Services → HPC

---

## Storage and HPC (critical decision)

HPC does not replace storage — it works with it.

### Use HPC storage for:
- temporary data during computation (`/scratch`)
- intermediate files during jobs

⚠️ `/scratch` is **not backed up** and is not for long-term storage :contentReference[oaicite:2]{index=2}  

---

### Use RDS with HPC when:
- your data is large or persistent
- you need reliable storage between jobs
- you exceed default HPC storage limits

RDS can be mounted on HPC and behaves like a shared drive with high performance.

→ See: Tasks → Store and share research data

---

## How work is done on HPC

The workflow is different from a normal computer:

1. **Login to the cluster**
   - via SSH to `hpc.uct.ac.za` :contentReference[oaicite:3]{index=3}  

2. **Prepare your job**
   - create a script describing:
     - resources needed (CPU, memory, time)
     - the program to run

3. **Submit your job**
   - using the scheduler (e.g. `sbatch`)
   - the system queues and runs it when resources are available :contentReference[oaicite:4]{index=4}  

4. **Monitor results**
   - outputs are written to files
   - jobs run independently of your session

---

## Important constraints (read this carefully)

- Do **not** run heavy computations on the login node  
  → this affects all users and may result in account suspension :contentReference[oaicite:5]{index=5}  

- HPC requires:
  - familiarity with Linux command line
  - structured workflows (scripts, not clicking)

- Resource requests matter:
  - requesting too many cores wastes shared resources
  - requesting too few may slow your job

- Software installation must be done via jobs, not directly on login nodes :contentReference[oaicite:6]{index=6}  

---

## Common combinations

In practice, HPC is used together with other services:

- **HPC + RDS**  
  Run large analyses on HPC using data stored on RDS  

- **HPC + GitLab**  
  Manage code in GitLab and run it on HPC  

- **HPC + data transfer tools**  
  Move data to/from HPC using Globus or similar tools  

---

## What to do next

- Learn about the system:
  - → [HPC service](../services/hpc/index.md)

- Get started:
  - → [Log into HPC](../how-to/hpc/log-into-hpc.md)
  - → [Submit your first job](../how-to/hpc/submit-your-first-job.md)

- Prepare your data:
  - → [Store and share research data](store-and-share-research-data.md)

---

## Good practice

To use HPC effectively:

- separate compute and storage (HPC + RDS)
- keep scripts reproducible and version-controlled
- test jobs on small datasets before scaling up
- request only the resources you need
- plan your workflow before submitting large jobs

---

## Need help?

If you are unsure whether HPC is right for your workflow:

- → [Choose the right service](../start-here/choose-the-right-service.md)
- → [Support](../support/index.md)