# Store and share research data

## When to use this

You want to:
- store research data during a project
- share data with collaborators
- prepare data for publication or archiving

---

## What you need to decide first

1. **Is this active or long-term data?**
   - active → use HPC or working storage
   - long-term → use RDS or managed storage

2. **Where is your data currently located?**
   - local machine
   - HPC
   - institutional storage

3. **Who needs access?**
   - only you
   - internal collaborators
   - external collaborators

---

## Recommended path

1. Store active data appropriately  
   → Service: Research data storage  
   → Reference: Storage and file systems

2. Move data between systems  
   → Service: Data transfer  
   → Reference: Data transfer and movement

3. Manage access and sharing  
   → Use appropriate access controls or transfer tools

---

## Common mistakes

- storing long-term data on HPC `/scratch`  
- duplicating large datasets unnecessarily  
- transferring data repeatedly instead of synchronising  
- not planning where final data will live  

---

## If your situation is different

- **Large datasets (100GB+)**  
  → use efficient transfer tools (e.g. rsync, Globus)

- **Sensitive or restricted data**  
  → confirm storage and sharing requirements before transfer

---

## Next steps

- document where your data is stored  
- clean up unused or duplicate data  
- prepare datasets for reuse or publication