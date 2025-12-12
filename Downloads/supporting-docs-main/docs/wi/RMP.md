---
layout: default
title: RMP as Doc
nav_exclude: true
---

## Research Management Process (RMP)
---

## Stages of the RMP 

|Stage Number|Stage Name|Description|
|---|---|---|
|1.0|[Proposal](#proposal)|Complete project proposal form|
|2.0|[Pre-grant](#pre-grant)|Complete a cost estimate of project requirements|
|3.0|[Pre-approval](#pre-approval)|Grant application submitted and waiting for approval|
|4.0|[Setup](#setup)|Funding in place, completes DMP/DPIA, DSAs finalised & signed, resulting in VRE build request|
|5.0|[Active](#active)|VRE built, data imported, researchers inducted|
|6.1|[Store](#store)|Data archived and VRE destroyed|
|6.2|[Destroy](#destroy)|Project is no more, data and VRE destroyed|
|7.0|[Discontinued](#discontinued)|Project have let us know they will not be progressing with us|

--- 

### Proposal 

In the proposal stage we help the project team to develop and finalise a LASER project proposal form.

In most cases project teams contact us to discuss their proposal. If initial conversations suggest the project may need support from DAT or LASER, we send them a proposal form to capture project requirements. If they don't need support from DAT or LASER in any way, they're unlikely to sit within our scope of support and so they won't progress in our RMP.

Project proposals are developed in an iterative way as part of an ongoing conversation with the project team. Project teams are responsible for filling out the form, but we help them to do this and can add details to the form where it helps. At any point in this process it may become clear that the project doesn't need DAT or LASER support, in which case the project wouldn't progress in our RMP.

The proposal form is designed to gather all the project requirements that we need. See the [project proposal](../../RMP/project_proposal.md) work instruction for steps needed to document the project requirements.

The proposal stage of the RMP is complete when we have a finalised version of a proposal form that documents the project's requirements.

### Pre-grant  

After finalising the proposal form at the end of the Proposal RMP stage, the next step is to get a costing estimate for any required LASER infrastructure and/or DAT support.

IT Services generate the costing. We just need to tell IT what the project requirements are, as documented in the proposal form, by submitting a costing request in ServiceNow. When IT return the costing, we present a summary of the costing to the project team and check they're happy to continue through the RMP on the basis that they'll fund the costs we've quoted.

For steps on how make the LASER costing request and present it to the project team, see the [LASER costing](../RMP/laser_costing.md) work instruction.

The Pre-grant RMP stage is complete when the project team has approved the LASER costing we have presented.

### Pre-approval

At this stage the project will have an approved costing, which can then be included into a grant proposals to secure the funding they will need for the agreed LASER and/or DAT support.

The researchers submit their grant proposal including the agreed costs. We ask that they send a copy of the submitted application to the LIDA Research and Innovation Development Manager (RIDM). Paul Evans is the LIDA RIDM.

The project will remain in Pre-approval stage while we await a funding outcome. If sufficient funding is secured, the project will progress to Setup stage.

If their funding bid is not successful, the project stage may move to Destroy if the team choose not to continue with the project. If the project team choose to seek funding elsewhere for the same application, we may keep the project in Pre-approval stage. If the project team decide to revise their proposal before submitting a new application, the project may need to move back to Proposal stage, so that we can gather new requirements and produce another costing.

If the project secured funding before approaching LIDA, we may skip the Pre-approval stage entirely.

Once the project team confirm they have successfully secured funding, congratulate the researchers and update the RMP stage in Prism to Setup.

### Setup 

Once project funding has been secured we can start to collect the rest of the project documentation. Project documentation consists of:
- Project proposal form
- Data management plan
- Data Protection Impact Assessment (incl. privacy notice)
- Risk assessment
- Contracts, such as data sharing agreement(s) (DSAs)

We created the project proposal form during the Proposal stage, so the next step is to complete the data management plan (DMP).

It's the project team's responsibility to complete this form, but we can help them. For details on how to help project team's complete a DMP, see our [DMP](../RMP/dmp_dpia.md) work instruction.

The University Library services also has helpful information on [data management](https://library.leeds.ac.uk/info/14062/research_data_management/61/research_data_management_explained), which the project team can use to help them complete their documentation.  

Data Sharing Agreements must be signed by all parties.  
We cannot receive data without a legal right to do so, which the DSA captures and contractualises.  

Tiering assessments will be informed by the DSA and [LASER Data Risk Tiering](https://lida-data-analytics-team.github.io/laserdocs/docs/laser_info/tiering.html); whichever comes out higher.  

 ### Add Data Flow Diagram

Some projects have complex data flows, with data coming from multiple sources and using various data transfer methods, and also requiring data or outputs to be sent to multiple recipeints.   
Some projects will have included a data flow diagram in their DMP, for others, we may need to either ask the project to provide a DMP or work with them to draw up one. 

When we have a data flow diagram, it should be published in the LASER Dashboard by following these steps:

1. Add the data flow diagram in the [Data Flow Diagram GitHub repo](https://github.com/LIDA-Data-Analytics-Team/data_flow_diagrams/tree/main)
2. The data flow diagram image to be uploaded in the GitHub repo above should follow this naming convention:
 - `p0###_data_flow_diagram.png` or 
 - `p0###_<t3/t4>_data_flow_diagram.png` if the project has different data flows for Tier 3 and Tier 4 TREs
 - `p0###_<a/b/c>_data_flow_diagram.png` if the project has multiple data flow diagrams.
 3. Copy the image URL from the GitHub website `https://lida-data-analytics-team.github.io/data_flow_diagrams/images/<image name as it appears in the GitHub>`
 4. Save the image URL on the project's Prism record:
 - on the Platfrom Details, click add and chose Data FLow Diagram
 - Paste the image URL, space || Description of the image e.g
 `https://lida-data-analytics-team.github.io/data_flow_diagrams/images/p0###_data_flow_diagram.png || Tier 3 Data FLow Diagram>`
 5. Check the LASER Dashboard to confirm that the image is well rendered.
   
[Complete Risk Assessment](../RMP/risk_assessment.md).  

Once the design of the VRE is finalised, captured in the project documentation and all costs agreed we can request IT Services build the VRE.  
You will need an account code from the research team so that the costs can be reclaimed from the project.
Use this [Service Now webform](https://leeds.service-now.com/it?id=sc_cat_item&sys_id=78ee5068db46d8507189ae994b9619e4) to make the request.  
You will receive an email confirmation that the ticket has been created and another when the VRE has been created.

Once the VRE has been created, add a project record to the latest version of the "LASER Project budget reporting" spreadsheet on Teams at:<br>
 `TEAM - LIDA Data Services Team - General\LRDP\LASER Budget & Finance\`  
Complete the columns with green headers. The Orange headers are the finance team to complete.  

[Log in](https://lida-data-analytics-team.github.io/laserdocs/docs/laser_how_to/laser_login.html) to the VRE and check that:
- all drives are mapped.
- Software Centre opens and displays available software correctly.
	- If apps are missing try forcing SCCM update by opening Control Panel > Configuration Manager > Actions tab > run "Application Deployment Evaluation Cycle" and "Machine Policy Retrieval & Evaluation Cycle" actions.
- You are able to navigate to Artifactory (http://artifactory:8082).

If successful update Prism record to 'Active'.


### Active 

Now the VRE is built, tested and research can commence!  

Notify the research team of the good news.  

	New LASER user induction.oft
	General - TEAM - LIDA Data Services Team\LASER\Comms and Presentations\Email templates

> Note that access cannot be granted to any individual until all User Documentation has been submitted to us by them.  

Several activities are required during the active stage of a project on LASER, some just once and others more frequently. Here are some links to work instructions for common activities:  

- [Adding users to a VRE](../RMP/new_vre_user.md)
- [Adding users to Azure SQL DB (PaaS)](../RMP/azure_sql_database.md)
- [Data Transfer (import and export)](../RMP/data_transfer.md)  
- [Restrict access to a directory within a VRE](../RMP/restrict_laser_folder.md)	 
- [Set up a GPU within a VRE](../RMP/gpu_vre_setup.md)

We record a project's projected end date in Prism. This date is when the active stage of the project ends. In the months leading up to the projected end date, we speak with the project team to check whether their plans have changed.

If they have funding and a lawful basis to extend the project we can update the projected end date and the project will remain active.

If the project plan involves a period of data retention the project would transition to the [Store stage](#store) of the RMP. Once all active and data retention periods are complete the project will be destroyed (see [Destroy stage](#destroy)).

### Store 

Projects in the Store stage have "mothballed" VREs. VREs that have mothballed retain the project data and nothing else. The data is put in cheap, inaccessible storage for a minimum of six months. After six months, the data can be brought back into active storage at extra cost - if this happens the project would return to the active RMP stage.

The VRE still exists in LASER and contains one blob storage account with the data held in one archive tier blob container. All other resources in the VRE, such as VMs and databases, are destroyed during the mothballing process. These changes are what makes the VRE cheaper than an active VRE, but render it inaccessible.

Data in a mothballed VRE is still being stored and processed, meaning that it is still governed by any terms and conditions of contracts that cover the project's use of the data, and if the contract expires the data must be destroyed.

See the [VRE mothball](../RMP/vre_mothball.md) work instruction for steps on how to mothball a project, moving it from Active to Store RMP stages.

If the project planned an active period to follow a mothballed period, we may have included costs for the extra active period during the LASER costing that was generated during the [Pre-grant stage](#pre-grant). But in most cases, projects do not know beforehand when they will need an extra active period or for how long. So typically we don't budget for an extra active period after a VRE is mothballed.

If a mothballed VRE needs to become active again, we first need to take the project back through all RMP stages. This is so that we can confirm the project's requirements are still understood and we can cost for the extra active period (unless this was already costed when the project began). The project may be fast tracked through the RMP stages if their requirements are unchanged, but we should at least confirm the project documentation is still valid.

If a mothballed VRE doesn't need to become active again, this stage will complete when the VRE is destroyed.

### Destroy 

In this RMP stage we permanently destroy the VRE and its contents. See the [VRE destruction](../RMP/vre_destroy.md) work instruction for steps on how to destroy a VRE. Before we destroy a VRE we need written confirmation that the PI understands that all data is permanently deleted with no chance of recovery. Once the VRE is destroyed update the RMP stage to Destroy in the project's Prism record.

### Discontinued 

The project have let us know that they will not be continuing with us before they reach 'Active' stage. This might be due to unsuccessful funding, changes to the data risk classification or any other reason. No need for LIDA, DAT or LASER.  

Update the Prism record with: 
- a note describing the reasons given 
- set the project stage to 'Discontinued'  

