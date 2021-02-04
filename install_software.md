---
layout: page
title: Install Software
nav_order: 4
---

## Install Software via Software Center

Optional software in LASER VREs are provided via an app called Software Center. If your VRE doesn't include software that you need, first check it can be installed in Software Center.

Open Software Center by typing its name in the taskbar search and selecting Software Center from the results.

![](./images/install_software/01_open_sccm.PNG)
{: .mx-auto }

When Software Center opens, you'll see a grid of all the software that can be installed in LASER VREs. Each item in the grid also shows the software version - multiple versions of a software may be provided. Search for the app you want to install and select it.

![](./images/install_software/02_find_app.PNG)
{: .mx-auto }

The window for your chosen app will open, showing some information about the install status, download size, etc. Select the Install button to install the app.

![](./images/install_software/03_app_pane.PNG)
{: .mx-auto }

The status shown will change to "Installing". If it's a large installation, you may see the estimated time remaining for the installation to complete.

Once the installation is complete, the status will change to "Installed". Where previously there was an Install button will now be an Uninstall button, for when you need to uninstall the software. You should now be able to find the software by looking in your Start menu or searching in the taskbar search.

You can install multiple versions of software at the same time, for example multiple versions of R available in Software Center.

Your new software will be installed to the Virtual Machine (VM) you're using, in the C:\ drive. If any other users also have access to this VM, they'll see the installed software too. If you open a different VM in the same Virtual Research Environment (VRE), you won't find the software unless you also install it there. Equally, any configurations made to installed software will be specific to VMs, not VREs. For more details on LASER's VRE architecture, see the [Home page](index.html).

If you need to install software that you can't find in Software Center, contact the [LIDA Data Analytics Team](mailto:ircdst@leeds.ac.uk) to make a software request. Your request will then be reviewed and added to the pipeline of new software.
