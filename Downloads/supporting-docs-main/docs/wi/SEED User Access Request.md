---
layout: default
title: New User (SEED)
parent: Work Instruction
has_children: false
---

# How to enable SEED user access

If you've not already got Active Directory Users and Computers installed on the machine where you access SEED, submit an IT request to have it installed, citing SEED admin as the reason.

### Prepare UAR

1. Get SEED User Access Request (UAR) form, signed by PI and referencing what they need access to, e.g. S: folder, part of project, SEED DB, web app, and edit/read level of access. Save the signed form to: <br>`N:\Academic-Services\ISS\IRC-Data-Services\SEED\Projects\<project-folder>\UAR\`
1. Get SEED Confidentiality Agreement signed by user and save to: <br>`N:\Academic-Services\ISS\IRC-Data-Services\SEED\IG\ConfidentialityAgreements\`<br>Follow the file naming convention used in the folder.
1. Check the project record in Prism to make sure any resources mentioned in the UAR are recorded in the project's platform details.
1. Connect to S:\ using Pulse Secure VPN on a campus machine

### Enable SEED access

1. Open Active Directory Users and Computers
1. In the navigation tree, go to ds.leeds.ac.uk > Resources > MDPH > Secure - Faculty > Secure-Storage-Admin-Groups
1. In the list of AD groups that appears, double click on VPN-Medics-Access to open its properties window
1. Select Member tab then click Add... button
1. Type the user's username in the text box and click Check Names.
1. If the username resolves to the correct user, click OK.
1. Check the user is in the members list, then click Apply and OK.

### Add user to S:\ folder group

1. Right-click on the folder and go to Properties > Security tab
1. In the box containing group names, look for ones that appear custom (i.e., not things like SYSTEM, CREATOR OWNER, Administrators, etc.). The SEED AD group names will contain prefixes like FMH-, FMHS-, or SEED-. (AD groups created recently will always use the SEED- prefix.)
1. Check the AD group has the correct level of permissions for this user (based on what was requested in the form).
1. Open Active Directory Users and Computers
1. In the navigation tree, go to  ds.leeds.ac.uk > Resources> MDPH > Medicine > Secure
1. This folder contains two subfolders: PEG and Research-Projects. The group you need to modify will be in one of the two depending on where on S:\ the project is stored. In both cases, all groups will be in a further subfolder called Groups, so go there.
1. If the project is old, there may be two nested groups: A group containing FLD keyword within the group name, which will have only one member. That member being a group with the same name, except with GRP keyword instead of FLD. You'll add the user to the GRP one, which you can find by either searching for it specifically or by navigating to it via the FLD group.
1. If an AD group with the correct permissions for the research project doesn't exist yet, [create a new AD group](#create-new-ad-group).
1. By now you should have identified the AD group containing project users, to which you can add the new user.
1. Double click the relevant AD group in Active Directory Users and Computers to open its properties window, then go to Members tab.
1. Click Add... then type the user's username in the text box and click Check Names.
1. If the username resolves to the correct user, click OK.
1. You should now see the user in the list of members. Select Apply then OK to complete the user access for the S drive folder.

### Add user to SEED SQL group
1. On VPN
1. Open SSMS and connect to SEED SQL
    1. Server type: Database engine
    1. Server name: SEEDSQL1
    1. Windows authentication
1. Find their database in the navigation tree then go to Security > Users folder
1. Look for user AD group in list that would give correct permissions as defined in the UAR form
1. Double click group to open properties and go to Membership page to check the DB roles assigned to that AD group are the right ones.
1. If the assigned DB role is custom, you may need to open the role's properties and check what SQL operations are permitted (go to Roles folder in database, then double click on the role and go to Securables page). 
1. Once you've identified the right AD group, follow same process as S:\ folder for adding or creating AD group.
1. DB access also controls web app

### Create new AD group

1. Open Active Directory Users & Computers and, using the navigation tree, go to the folder where you will want to store the AD group (either `ds.leeds.ac.uk\Resources\MDPH\Medicine\Secure\PEG\Groups\` or `ds.leeds.ac.uk\Resources\MDPH\Medicine\Secure\Research-Projects\Groups\`
1. Click the create new group button in the menu bar.
1. Name the AD group using the same convention used for other AD groups in the same project (see details on naming above).
1. If you need to create an "FLD" AD group, use Domain local group scope. If you need to create a "GRP" or "SEED" AD group, use Universal group scope.
1. Then in File Explorer, go to the project folder, right click and open properties, then select Security tab.
1. Click Edit button, then Add... and add the AD group to the folder in the same way you'd add a user to an AD group.
1. Once you've added the AD group, select the group and update the permissions by allowing or deny each.
1. Click Apply then OK to finish.
