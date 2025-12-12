---
layout: default
title: New TRE User
parent: RMP
has_children: false
---

# Adding a new user to LASER

Ensure that the request for adding a user to a project in LASER has come from (or has been confirmed by) the Principal Investigator for the project.

- Add the requested user to the Project record in Prism, creating a new User record if necessary.
- Add the requested user to `LIDA Leeds Institute for Data Analytics` Teams Team in Teams


## Collect documentation & evidence

- Prior to being granted access to LASER all users are required to provide  
	- Signed LASER User Agreement  
	- Evidence of passing scores (within last **12 months**) for:  
		- Data Protection training  
		- Information Security training  
		- NOTE : If the user is not a UoL staff member, they can take the Data Protection and Information Security assessments [here](https://lida-data-analytics-team.github.io/igtraining/)
	- Record the dates of completion on the User record in Prism  
	- Save documents to the Users folder in OneDrive


## Granting access to LASER 

- Set User record in Prism to 'Enabled'
- Open Active Directory Users and Computers

Platform access:  
- If not already a member, add the user to the platform AD group that grants the correct level/method of access.
	- The AD groups granting platform-level access are found in ds.leeds.ac.uk/Resources/LRDP/VRE/Groups/
		- Remote LASER access is granted by LRDP-All-Citrix-Users
		- Safe room access is granted by LRDP-All-Citrix-SafeRoom-Users

TRE access:  
- Find the TRE's AD group folder in ds.leeds.ac.uk/Resources/LRDP/VRE/Groups/
- Add users to the TRE AD group that gives them the correct level of permissions.
- If such a group doesn't exist, you may need to ask server team to create the group for you.

{: .note }
> Researchers using the **Safe Room** will need to be issued with **MFA Duo fobs**, as mobile devices are not permitted within the Safe Rooms. These can be requested from IT Services through Service Now. 
> 
> Simply create a new request and make note of the Ticket number. The researcher can then take this ticket number to IT Service Desk at their earliest convenience and a Duo fob will be assigned to them while they wait.  

## LASER induction
LASER induction usually takes about 30 – 45 min to complete.

During the induction, the user will share their screen as we take them through the LASER login process.

We usually cover these basic themes; depending on the user's experience using LASER

- How to log on to LASER and access the VMs and properly shut down (after use), to avoid accruing additional cost.
- How to shut down the VMs from Azure portal
- How to monitor TRE usage from the LASER dashboard and Azure portal
- Where project files are saved and how to access them
- The process of importing and exporting files from the TRE
- How to install software and set up Artifiactory (if you are using R/Python)

All the main things we cover during the Induction are on [our public website](https://lida-data-analytics-team.github.io/laserdocs/docs/laser_how_to/).
