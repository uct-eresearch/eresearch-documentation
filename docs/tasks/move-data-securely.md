# Move data securely

## When to use this

You want to:
- transfer data between systems
- move data to or from HPC
- share data with collaborators

---

## What you need to decide first

1. **Where is your data now?**
   - local machine
   - HPC
   - institutional storage

2. **How large is the dataset?**
   - small (<1GB) → simple tools are sufficient  
   - large (10GB+) → use efficient transfer methods  

3. **Is this a one-time transfer or ongoing sync?**
   - one-time → direct copy  
   - repeated → use tools like `rsync`  

---

## Recommended path

1. Choose a transfer method  
   → Service: Data transfer  

2. Understand constraints  
   → Reference: Data transfer and movement  

3. Execute transfer using appropriate tool  
   (scp, rsync, or managed service)

---

## Common mistakes

- transferring large datasets through login nodes  
- copying the same data repeatedly instead of syncing  
- working with many small files without grouping them  
- interrupting transfers without using resumable tools  

---

## If your situation is different

- **Very large datasets (100GB+)**  
  → use managed transfer tools (e.g. Globus)

- **Frequent updates**  
  → use `rsync` to avoid re-copying unchanged data  

---

## Next steps

- verify transferred data  
- organise data in target location  
- clean up unnecessary copies