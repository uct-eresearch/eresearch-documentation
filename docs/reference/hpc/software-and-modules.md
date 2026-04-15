# Software and modules

## Software environments on UCT HPC

UCT HPC provides a shared software environment for research computing. Many applications, compilers, interpreters, and scientific tools are installed centrally and made available through the **module system**.

This page explains how software is organised, how modules work, and what to keep in mind when using or extending software environments on the cluster.

---

## Overview

Software on HPC is typically provided in one of two ways:

- as part of the base operating system
- as centrally installed research software made available through modules

In practice, most research software is accessed through the module system.

Modules allow the system to:

- provide multiple versions of the same software
- configure the correct executable paths and libraries
- reduce conflicts between tools and environments
- let users switch between software versions as needed

---

## Where software lives

Many centrally installed research applications are stored in a shared location on the cluster.

Typical characteristics of centrally installed software:

- available to all relevant users on the system
- maintained by the HPC team
- often exposed through a module rather than used via a direct path
- may include multiple versions of the same tool

You may occasionally see software referenced directly by path, but in most cases the preferred access method is through modules.

---

## What a module does

A module changes your shell environment so that a specific software package becomes available for use.

When you load a module, it may:

- add a program to your PATH
- configure library paths
- set software-specific environment variables
- load supporting dependencies automatically

This means that loading a module is often required even when software is already installed on the system.

---

## Core module commands

```bash
module avail
module load <module-name>
module list
module unload <module-name>
module purge
```

- `module avail` — list available modules
- `module load` — load a module
- `module list` — show loaded modules
- `module unload` — unload a module
- `module purge` — clear all modules

---

## Typical usage pattern

```bash
module avail
module load python/miniconda3-py3.12
python --version
```

For batch jobs:

```bash
#!/bin/bash
#SBATCH --job-name=test
#SBATCH --partition=ada
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --time=01:00:00

module purge
module load python/miniconda3-py3.12

python myscript.py
```

---

## Use modules inside jobs

Always load modules inside job scripts. Interactive sessions do not carry over into batch jobs.

---

## Python on HPC

```bash
module load python/miniconda3-py3.12
```

Use HPC-provided Python modules to ensure consistent environments.

---

## R on HPC

```bash
module load R/R-4.3.3
R
```

---

## Installing your own packages

Do not install heavy software on login nodes. Use an interactive job.

### Python

```bash
module load python/miniconda3-py3.12
pip install --user package-name
```

### R

```bash
module load R/R-4.3.3
R
```

```r
install.packages("PACKAGE_NAME")
```

---

## Conda environments

```bash
module load python/miniconda3-py3.12
conda create -y -n myenv
source activate myenv
```

---

## Common issues

### Command not found

```bash
module list
which <command>
```

### Wrong version

```bash
module list
python --version
```

### Clean environment

```bash
module purge
```

---

## Good practice

- load modules explicitly in jobs
- use one environment per project
- avoid installing on login nodes
- document software versions