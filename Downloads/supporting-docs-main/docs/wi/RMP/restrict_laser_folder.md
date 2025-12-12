---
layout: default
title: Restrict a folder
parent: RMP
has_children: false
---
# Create folders with restricted access in LASER VREs

Some projects may require role-based access controls within the VRE to limit which team members can access certain files and data assets. DAT can perform all of the below steps themselves.

### AD setup

1. Open Active Directory Users and Computers and navigate to the VRE's folder in the AD directory tree
1. Create an AD group that will be used to define access to the VRE's restricted folder:
    - Group scope: Universal
    - Group naming convention: `VRE-<vre-id>-<folder-name>-<access-rights>`
    - E.g. to restrict access to a folder called LTHT inside VRE p0001v01, giving permitted users Modify rights: `VRE-p0001v01-LTHT-Modify`
1. Assign permitted users to the new AD group.

### VRE N drive setup

1. Connect to the VRE's project file share
1. Create the folder that will have restricted access on the N: drive root
1. Right click the folder > Properties > Security tab, then click the Advanced button
1. Check the box to "Replace all child object permission entries with inheritable permission entries for this object"
1. Select Disable inheritance
1. When the dialog box appears asking what to do with current inherited permissions, select "Convert inherited permissions into explicit permissions on this object."
1. Click Apply
1. Add the AD group you created for this folder and give it the required access rights
1. Add LRDP-DAT-Admins AD group and give it Full Control rights
1. Add LRDP-Project-Admins AD group and give it Full Control rights
1. Remove Users (<vre-name>\Users) principal
1. Remove Authenticated Users principal
1. Click Apply
1. If any files that need restriction already exist on N: drive, move them into the new folder (these will inherit permissions from the restricted folder)
1. Ask the users to test the permissions settings have worked as intended
