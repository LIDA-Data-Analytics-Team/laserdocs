---
layout: default
title: Project Storage
nav_order: 3
---

## Where is my project data?

If you open up File Explorer and click on the computer name on the left, you will see a list of drives (C:, M: etc.)

Your shared project storage can be found on the N: drive, as highlighted in the image below.

N: drive is shared across all VMs in your VRE.

We recommend saving all of your documents to the N: drive so that they benefit from the higher level backup schedule and remain available to the rest of your team. 

![N: drive](./images/storage_drives/laser_drives_shared_highlight.png)

### Other drives 
The C: drive is the operating system storage and does not benefit from the same backup retention schedule as project storage. Please refrain from saving any files here.

M: drive contains the user directories that contain the default _'Quick access'_ folders. It is similarly existant on the virtual machine only and we recommend the use of **M: (incl. Documents, Downloads, etc.) is avoided**.  
Files saved to user directories on M: (Documents, Downloads etc.) will not be available across the VRE, only on the VM you are currently connected to. They also do not benefit from the same backup retention schedule as project storage on N: drive.

R: and P: drives relate to package repositories that you will only have read access to.

'staging' is used for data transfers to and from the VRE.
