---
layout: default
title: Troubleshooting
nav_order: 999
---

## Troubleshooting
[My desktop won't start](./troubleshoot.html#My-desktop-won't-start)
[I cannot see R: drive](./troubleshoot.html#I-cannot-see-R:-drive)


### My desktop won't start

![cannot_start_desktop.png](./images/troubleshoot/cannot_start_desktop.png)

Chances are good that another member of your team is currently logged in to that specific virtual machine.

A VM will remain 'occupied' even if the user has disconnected. 

Simply closing the window ('X'ing out) will disconnect the user from the session. When disconnected the session remains active and running; users will need to log off or shut down to vacate the machine so that someone else can log on.

### I cannot see R: drive

You may need to manually map the R: drive to your machine.
- Open File Explorer and right click on Network  
	![network_context_menu.png](./images/troubleshoot/network_context_menu.png)
- Select 'Map network drive'
- Drive = R: 
- Folder = \\azlrdprepos.file.core.windows.net\r-repo
	![map_r_drive.png](./images/troubleshoot/map_r_drive.png)
- Click finish 

You should now see the R miniCRAN repository mapped to R: drive.

