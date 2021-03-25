---
layout: default
title: Troubleshooting
parent: LASER How To
nav_order: 999
---

## Troubleshooting
{:.no_toc}

Here are the answers to some common issues. If you have a problem not covered here please get in touch with the Data Analytics Team at [ircdst@leeds.ac.uk](mailto:ircdst@leeds.ac.uk).

* seed list
{:toc}

### My desktop won't start

![cannot_start_desktop.png](../../images/troubleshoot/cannot_start_desktop.png)

Chances are good that another member of your team is currently logged in to that specific virtual machine. Try another VM if there is one available within the VRE, or check that no-one else is currently logged in.

A VM will remain 'occupied' even if the user has disconnected. 

Simply closing the window ('Xing out') will disconnect the user from the session. When disconnected the session remains active and running; users will need to log off or shut down to vacate the machine so that someone else can log on.

### I cannot see R: drive

You may need to manually map the R: drive to your machine.
- Open File Explorer and right click on Network  
	![network_context_menu.png](../../images/troubleshoot/network_context_menu.png)
- Select 'Map network drive'
- Drive = R: 
- Folder = \\\azlrdprepos.file.core.windows.net\r-repo
	![map_r_drive.png](../../images/troubleshoot/map_r_drive.png)
- Click finish 

You should now see the R miniCRAN repository mapped to R: drive.

### Anaconda Navigator slow (in online mode)

Anaconda Navigator may be slow to load initially. Follow steps in our [Python guide](./using_python.html#anaconda-navigator-offline-mode) to enable offline mode, which will improve performance.
