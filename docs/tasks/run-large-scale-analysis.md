# Run large-scale analysis

## When to use this

You want to:
- run analyses that take hours or days
- process large datasets
- scale work across CPUs or GPUs

---

## What you need to decide first

1. **Does your job fit on a single machine?**
   - yes → use a single-node job
   - no → you may need parallel or distributed computing

2. **Does your workload need GPUs?**
   - yes → request GPU access and use a GPU partition
   - no → use CPU partitions

3. **Where will your data live during computation?**
   - large data → `/scratch`
   - small inputs → `/home`

---

## Recommended path

1. Prepare your working directory  
   → How-to: Manage files and storage

2. Load required software  
   → How-to: Use software modules

3. Create a job script  
   → How-to: Submit a job

4. If needed, configure GPU usage  
   → How-to: Use GPUs

---

## Common mistakes

- running work on the login node instead of submitting jobs  
- writing large data to `/home` instead of `/scratch`  
- requesting more resources than needed, leading to long queue times  
- skipping small test runs before scaling  

---

## If your situation is different

- **Interactive or exploratory work**  
  → Use Open OnDemand or interactive jobs

- **Workflow automation or pipelines**  
  → Structure jobs as repeatable scripts

---

## Next steps

- Monitor job progress  
- Review output and logs  
- Move results to persistent storage