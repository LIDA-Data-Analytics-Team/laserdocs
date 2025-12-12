---
layout: default
title: Supporting Stata in LASER
parent: Work Instruction
has_children: false
---

# Supporting Stata in LASER

## Add packages to Stata library

Users cannot install packages without an internet connection. We have a library of pre-installed packages at `R:\Stata\ado\plus\`, which users can add to their adopath in Stata. The full path for R: drive is `\\azlrdprepos.file.core.windows.net\r-repo`.

If users need a package that hasn't been added to the library yet, they email us to request it. The email request should include the URL for the package so we know where to find it, and if needed additional details on how to install it.

We must install the package outside of LASER and copy the installed files into LASER's Stata library.

Open Stata outside of LASER, using the same version as what's available in LASER.

Install the package using the relevant instructions for the package. The installation will most likely tell you where the files have been installed to, which is most likely in your PLUS folder, `C:\Users\<username>\ado\plus\`.

Transfer the newly installed files for the relevant packages into LASER.

Once you have copies in LASER, if you don't use Stata regularly it's a good idea to clear the folder where the packages were installed, so that when you deal with the next Stata request you'll have a clean folder that files will be put into.

Once in LASER, move the files into the Stata library. The library follows Stata's convention of placing files in subfolders named with the first character of the file name. So you need to move the files into their alphabetised group.

The package has been added to the Stata library. Let the user know it's ready to use.
