# GPU access and partitions

## Using GPUs on UCT HPC

Some HPC workloads require access to **Graphics Processing Units (GPUs)**, which provide accelerated computation for tasks such as machine learning, simulation, and data processing.

GPU resources on HPC are limited and managed separately from standard CPU resources.

---

## GPU access is not enabled by default

Access to GPU resources is **not automatically granted**.

You typically need to:
- request access
- provide a justification for your use case
- obtain approval before submitting GPU jobs

This ensures fair and appropriate use of specialised resources.

---

## What GPUs are used for

GPUs are suited to workloads such as:

- machine learning and deep learning  
- large-scale numerical simulations  
- image and signal processing  
- parallelisable data processing tasks  

Not all workloads benefit from GPUs. Many analyses run more efficiently on standard CPU resources.

---

## Partitions

HPC resources are organised into **partitions**, which group compute nodes with similar capabilities.

GPU-enabled nodes are typically accessed through a **specific GPU partition**.

To use GPUs, your job must:
- request GPU resources
- target the appropriate partition

---

## Requesting GPU resources

When submitting a job, GPU usage is specified in the job script.

This typically includes:
- selecting the GPU partition
- requesting one or more GPUs
- defining CPU, memory, and time requirements alongside GPU usage

→ See job submission details: `Reference > HPC > Scheduler and job submission`

---

## Resource constraints

GPU resources are:
- limited in number  
- shared across users  
- often in high demand  

This means:
- jobs may wait longer in the queue  
- over-requesting resources can delay scheduling  
- efficient usage is important  

---

## Good usage practices

- only request GPUs if your workload requires them  
- test your code on CPUs before scaling to GPUs  
- request the minimum number of GPUs needed  
- release resources promptly by ending jobs when complete  

---

## Common issues

### Job does not start

- GPU resources may not be available  
- check whether you are using the correct partition  
- verify that you have GPU access enabled  

---

### Poor performance

- not all code is GPU-optimised  
- ensure your software is configured to use GPUs  
- confirm that your workload benefits from parallel execution  

---

### Access denied

- GPU access has not been approved  
- contact support or follow the appropriate request process  

---

## Relationship to other resources

- **CPU-based jobs** → run on standard compute nodes  
- **GPU-based jobs** → run on specialised nodes in GPU partitions  
- **Storage** → both use the same `/home` and `/scratch` systems  

---

## Related pages

- HPC overview → `Services > HPC`
- Scheduler and job submission → `Reference > HPC > Scheduler and job submission`
- Storage → `Reference > HPC > Storage and file systems`
- Support → `Support`