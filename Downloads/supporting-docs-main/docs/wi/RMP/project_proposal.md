---
layout: default
title: Project proposal
parent: RMP
has_children: false
---

# Project proposal

The purpose of the proposal stage is to help the project team develop and finalise a LASER project proposal form. If initial conversations suggest the project may need support from DAT or LASER, send them a proposal form to capture project requirements.

A template of the proposal form can be found at: <br>
`N:\Academic-Services\ISS\IRC-Data-Services\Processes\ISMS\Work Instructions\supporting-docs\templates`

The template will be called T_01_Project_Proposal_v.X.Y.docx, where X.Y is the template version (e.g. T_01_Project_Proposal_v.1.4.docx). Send the project team the latest template version.

***

Once the project team have returned the form, create a new project record in Prism.

Forward the proposal form to LIDA's Research and Innovation Development Manager (RIDM), Paul Evans. If the form contains a KRISTAL reference, the RIDM will add it to Prism and link it with the project record you've created.

The Prism record will assign the project an ID, a.k.a. project number. All projects have a folder on N: drive at <br>
`N:\Shared\Academic-Services\ISS\IRC-Data-Services\Projects\`.<br>
These folders are where we store the project's documents, including the proposal form you've received.

You'll need to create a folder for the new project, by making a copy of the template folder at<br>
`N:\Academic-Services\ISS\IRC-Data-Services\Projects\P____ - Project folder template [Make a copy]\`

The template contains subfolders for all the key documents we collect through the RMP. Save the proposal form in the subfolder called `1_proposal_form\`. Rename the file if needed so that the project and form version is clear, e.g. `P0000_ Project Proposal v1.docx`.

Then open the project record in Prism and update the proposal form version history. To update the proposal form version history, click the "IRC Proposal" button in the "Project Documents" section.

***

Check the proposal form to see what requirements have been documented. You'll probably need to continue the discussion with the project team, creating multiple versions of the form until all requirements are sufficiently documented.

With each new version of the proposal form, update the version history in Prism and save a copy to the project folder, making sure to update the version number in the file name.

As you go through this process, you may want to add notes to the Prism record, in the notes section. Notes are useful to help someone else, or your future self, understand the project, its context and status. You might make a note to summarise the project's research purpose, explain decisions regarding project requirements, log RMP progress and actions required from other teams, and more.

***

The project requirements we gather in the proposal form can be grouped into two types: technical and information governance (IG).

The information governance requirements are needed to classify the risk of the project's data according to [our risk tiering system](https://lida-data-analytics-team.github.io/laserdocs/docs/laser_info/tiering.html). This classification determines whether the project needs to be hosted in LASER, and what security controls are required.

To classify the project's risk we assess:
- How identifiable is the data? If it's personal data, are individuals directly identifiable or pseudonymised? How robust is the pseudonymisation? Will they combine data sources in ways that could reveal identity?
- How sensitive is the data? What variables will they have? Any GDPR special category data?
- Who owns the data? How was it collected? How will it be transferred to us?
- What will they be doing with the data? Will the research outputs and insights be sensitive?
- What would be the reputational risk of unauthorised data disclosure?
- Do they need to comply with any security standards? If they need ISO27001 or NHS DSPT accreditation, they'll need to host the data in LASER.

If you're not sure how to classify a project, it's always worth discussing with colleagues and asking the LIDA IG Manager for advice.

The technical requirements documented in the proposal form will determine what resources they need in their LASER VRE:
- What volume of data will they be working with, and therefore, how much storage will they need?
- How will they analyse the data? This and the data volume will help determine what type of VM(s) they need.
- How many people will be working on the project and how many will need to work _at the same time_. The latter will determine how many VMs they need.
- How regularly will the VMs be used? We have to assume how many hours per month each VM will be used.
- For how long will the project be in an "active" research phase? For how long will they need data retention storage if at all?
- Will they need a database?
- Are there any other bespoke requirements, such as needing some level of internet connection. If so, engage with IT asap to establish requirements.

The project team may not be able to answer everything described above and we often need to advise them based on what they can tell us. But we need enough information to classify their project risk and establish what VRE resources they need.

Once we understand their requirements and the proposal form is finalised, open Prism to record the document version history as "accepted". Then move to the next RMP stage (and update the RMP stage in the Prism record).
