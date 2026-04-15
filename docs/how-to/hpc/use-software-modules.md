# Use Software Modules

## Overview

Load and manage software in the HPC environment using the modules system.

---

## Before you begin

Make sure:

- you can log into the HPC system  
  (see: [Log into HPC](log-into-hpc.md))
- you know which software you want to use
- you have access to the environment where modules are available

---

## Steps

### 1. Log into HPC

```bash
ssh <username>@hpc.uct.ac.za
```

---

### 2. Check which modules are currently loaded

```bash
module list
```

This shows the software modules currently active in your shell session.

---

### 3. Search for available software

To search for a package or software family:

```bash
module avail
```

If the module system supports filtered search, you can also use:

```bash
module avail <software-name>
```

Replace `<software-name>` with the name of the software you want.

---

### 4. Load a module

Load the required software module:

```bash
module load <module-name>
```

Replace `<module-name>` with the full module name shown by `module avail`.

Example:

```bash
module load <software-name>/<version>
```

---

### 5. Confirm that the module is loaded

```bash
module list
```

You should now see the module in the list of active modules.

If the software provides a command-line executable, you can also verify it directly:

```bash
which <command-name>
```

Replace `<command-name>` with the command you expect to run.

---

### 6. Run your software

Once the module is loaded, run your command as needed.

Example pattern:

```bash
<command-name> --help
```

This is a simple way to confirm that the software is available in your current session.

---

### 7. Unload a module when no longer needed

To remove a module from your current session:

```bash
module unload <module-name>
```

---

### 8. Reset your module environment if needed

To clear all currently loaded modules:

```bash
module purge
```

Use this if:
- you want a clean environment
- you need to avoid conflicts between loaded modules

---

## Verify

Check that:

- the required module appears in `module list`
- the software command is available with `which <command-name>`
- the software runs successfully in your session or job script

---

## Troubleshooting

### Module not found

Possible causes:

- the module name is incorrect
- the software is not available on the system
- the version name is incorrect

Check again with:

```bash
module avail
```

---

### Software command still not available after loading

Possible causes:

- the wrong module was loaded
- the executable name differs from the module name
- the module did not load correctly

Check:

```bash
module list
which <command-name>
```

---

### Module conflicts with another module

Possible cause:

- an incompatible module is already loaded

Try:

```bash
module purge
module load <module-name>
```

---

## Related pages

- [Log into HPC](log-into-hpc.md)
- [Submit a job](submit-a-job.md)
- [Use GPUs](use-gpus.md)