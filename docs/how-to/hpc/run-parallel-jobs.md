# Run parallel jobs

Run jobs that use multiple CPU cores or nodes on the HPC system.

---

## When to use parallel jobs

Use parallel jobs when your software:

- can use multiple CPU cores  
- supports MPI or multithreading  
- benefits from distributed computation across nodes  

If your software is not parallel-aware, requesting more cores or nodes will not make it faster.

---

## Parallel job types

### Single-node parallel jobs

- use multiple cores on one node  
- suitable for multithreaded applications  

### Multi-node parallel jobs

- use cores across multiple nodes  
- require MPI or distributed computing support  

---

## Example: single-node parallel job

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --time=02:00:00
#SBATCH --nodes=1
#SBATCH --ntasks=8
#SBATCH --job-name="ParallelJob"

myprogram -n ${SLURM_NTASKS}
```

---

## Example: multi-node MPI job

```bash
#!/bin/sh
#SBATCH --account=myaccount
#SBATCH --partition=ada
#SBATCH --time=02:00:00
#SBATCH --nodes=2
#SBATCH --ntasks=8
#SBATCH --ntasks-per-node=4
#SBATCH --job-name="MPIJob"

module load mpi/openmpi

srun my_mpi_program
```

---

## Key directives

- `--nodes` → number of nodes  
- `--ntasks` → total number of cores  
- `--ntasks-per-node` → cores per node  

---

## Important notes

- Do not request multiple nodes unless your software supports it  
- More cores do not always mean faster performance  
- Jobs may run slower across nodes due to communication overhead  

---

## Using environment variables

Use SLURM variables to match your program to allocated resources:

- `${SLURM_NTASKS}` → total number of cores  
- `${SLURM_TASKS_PER_NODE}` → cores per node  

Example:

```bash
myprogram -n ${SLURM_NTASKS}
```

---

## OpenMP jobs

If your program uses OpenMP:

```bash
export OMP_NUM_THREADS=${SLURM_NTASKS}
```

---

## Troubleshooting

### Job does not scale

- software may not support parallel execution  
- try running on fewer cores  

### Poor performance

- avoid spreading jobs across nodes unless necessary  
- check CPU and memory usage  

---

## Next steps

- [Submit a job](submit-a-job.md)  
- [Check job status](check-job-status.md)  
- [Run interactive jobs](run-interactive-jobs.md)