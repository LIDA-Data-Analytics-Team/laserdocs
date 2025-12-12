---
nav_exclude: true
---
## LASER and miniCRAN

VREs within LASER lack internet connectivity by design, so R packages cannot be installed from CRAN.

Instead, they can be made available to a shared file store (R: drive) to which all VREs/researchers will have read access to.

Members of the DAT can make packages available to be installed to a VRE from this repository instead of CRAN.

More detailed information can be found [here](https://cran.r-project.org/web/packages/miniCRAN/vignettes/miniCRAN-introduction.html).

### Making packages available
Before a researcher can install a package to their VRE from miniCRAN it must first be made available.

DAT have read/write access to R: drive only from the DAT - Data Transfer Server. The R: drive can be navigated to via the file path: [\\\\azlrdprepos.file.core.windows.net\\r-repo\\miniCRAN](\\\\azlrdprepos.file.core.windows.net/r-repo/miniCRAN)

Add package name(s) to pkg and run to add the package(s) and dependencies to the LASER miniCRAN repository:

```R
# Set variable values
pkg <- c() # Add package names to this vector
pth <- "\\\\azlrdprepos.file.core.windows.net/r-repo/miniCRAN"
rep <- c(CRAN = "https://cran.rstudio.com/")

# Load package files from CRAN to miniCRAN
library("miniCRAN")
addPackage(pkg, path = pth, repos = rep, type = c("win.binary", "source"))
```

### Installing packages
Once a package has been made available to R: drive it can be installed to a library within a VRE.

All researchers should have read access to R: drive from all VREs.

The method is the same as usual, we just need to point to the miniCRAN repository on R: drive.

Add package name(s) to pkg and run to install package(s) and dependencies from the LASER miniCRAN repository:

```R
# Set variable values
pkg <- c()
pth <- "file:///R:/miniCRAN"

# Install package(s) from LASER miniCRAN
install.packages(pkg, repos = pth)
```

