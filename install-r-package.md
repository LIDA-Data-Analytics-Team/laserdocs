---
layout: default
title: "Installing R Packages"
nav_order: 2
---
## R Packages in LASER

VREs within LASER lack internet connectivity by design, so R packages cannot be installed from CRAN.

Instead, they can be made available to a shared file store (R: drive) to which all VREs/researchers will have read access to.

Members of the DAT can make packages available to be installed to a VRE from this repository instead of CRAN.

### Installing packages
Once a package has been made available to R: drive it can be installed to a library within a VRE.

All researchers should have read access to R: drive from all VREs.

The method is the same as usual, we just need to point to the miniCRAN repository on R: drive.

Add package name(s) to pkg and run to install package(s) and dependencies from the LASER miniCRAN repository:
```markdown
# Set variable values
pkg <- c()
pth <- "file:///R:/miniCRAN"

# Install package(s) from LASER miniCRAN
install.packages(pkg, repos = pth)
```

If a required package is not currently available please contact a member of the DAT at [ircdst@leeds.ac.uk](mailto:ircdst@leeds.ac.uk)
