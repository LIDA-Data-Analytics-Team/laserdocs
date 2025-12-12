---
layout: default
title: VRE Destroy
parent: RMP
has_children: false
---

# VRE Destroy

Before we destroy a VRE, get authorisation from the project PI that their project can be irreversibly destroyed. All data and backups will be gone forever. Give projects a chance to export data to suitably secure locations outside LASER before their VRE is destroyed.

VRE destructions are authorised by PIs signing a project closure form. The form template can be found at:<br>
`N:\Academic-Services\ISS\IRC-Data-Services\Processes\ISMS\Work Instructions\supporting-docs\templates`

The template file name is `T-05 Project Closure form vX.Y.docx` where X.Y is the document version. Use the latest version. Send a copy to the PI and ask them to return a signed copy. File a signed copy in the project's records folder on N: drive.

***

Once we've documented the PI's authorisation we can delete the project data, at a scheduled time if need be. Log on to DAT02 server and locate all of the project's storage.

Most of the project's files will be located on the VRE's N: drive, a.k.a. their project file share [\\azlrdp#####v0#.file.core.windows.net\project]. But we'll also need to delete any project files stored elsewhere, particularly those not stored in the VRE itself, such as storage used by DAT or the Data Transfer App during file transfers.

Here's a thorough but potentially incomplete list of places to check:

1. VRE's project share, e.g. `\\azlrdpp0000v01.file.core.windows.net\project`
1. VRE's staging share, e.g. `\\azlrdpp0000v01.file.core.windows.net\staging`
1. VRE's database if it has one
1. DAT's file transfer incoming share `\\datstagingdata.file.core.windows.net\incoming`
1. DAT's file transfer outgoing share `\\datstagingdata.file.core.windows.net\outgoing`
1. VRE folder on DTA's export approved share e.g. `\\azlrdpdataexport.file.core.windows.net\exportapproved\az-lrdp-p0000v01\` (Files in this folder will probably be deleted on a regular basis, but can't hurt to check)

Communicate with the project PI throughout this process.

***

Now that the data has been deleted, we need to destroy the VRE. Go to the [LASER requests catalogue](https://it.leeds.ac.uk/it?id=sc_category&sys_id=be3bfcb0db3a18d0cd2a449e3b96195c&catalog_id=e0d08b13c3330100c8b837659bba8fb4) in ServiceNow and open a Destroy Request.

Enter the project details into the form, confirm the data has been deleted, agree to the terms and conditions, then submit the request. The request will be "fulfilled" once the VRE has been destroyed by a colleague in IT.

Let the PI know that the project destruction is complete.

Archive the project's records on N: drive by moving the project folder into:<br>
`N:\Academic-Services\ISS\IRC-Data-Services\Projects\Closed Projects`

Archive project users' records if the user does not have any other active project: move the user folder to the disabled accounts folder:  `N:\Academic-Services\ISS\IRC-Data-Services\Users\0.Disabled accounts` 

Archive the project's email history in the DAT mailbox by moving the project inbox folder into the Projects > Archive folder.

Set the project Stage to Destroy in Prism (with notes to detail what you've done).
