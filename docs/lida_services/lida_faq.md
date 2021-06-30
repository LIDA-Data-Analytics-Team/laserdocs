---
layout: default
title: LIDA FAQ
parent: LIDA Services
nav_order: 5
---

## LIDA Frequently Asked Questions
{: .no_toc }

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }
1. TOC
{:toc}
</details>

### Do we need to cost the support from LIDA when applying for a grant? 
The costs of using LASER (Leeds Analytics Secure Environment for Research) compute and storage and associated support from the Data Analytics Team (DAT) needs to be factored into your grant. We advise you to approach the DAT directly as early as possible (please allow for at least 7 working days), who will help you to determine what LASER and DAT costs are required for your grant application and how much they will be. 

### Is the support mainly focused on quantitative data analysis (statistical) or both quantitative and qualitative (video-based data)? 
We do support qualitative as well as quantitative/statistical analysis. Our secure environment enables qualitative analysis of audio/video data that would otherwise not have been possible given the IG requirements of the data owner. We can support any analysis that requires LASER’s security controls (including ISO27001 and Data and Security Protection Toolkit).

### Does LASER have its own Data Protection Officer? 
LIDA has its own Information Governance Manager and we work very closely with  UoL IG/IT Assurance and UoL Data Protection Officer Alice Temple.

### What support is there for projects that would benefit from data analytics support but don’t need tier 3 or 4 environment? 
As with project with Tier 3 or 4 data, the DAT can support analysis work within your project and help set up storage space and provide the appropriate secure environment on our Tier 2 platform - SEED. DAT support costs will be dependent on the level of support required. LIDA do provide training courses for common research software such as GIS, R, Python etc. The DAT can provide advice & guidance as to how these are used within your project, regardless of security tier.

### Is Stata available? 
Yes, it is available in LASER. For a full list of available software please see [here](https://lida-data-analytics-team.github.io/laserdocs/docs/laser_info/software_list.html).

### Can we use ONS SRS data in LASER? 
LIDA has AOC (Assured Organisational Connectivity) status with Office of National Statistics (ONS), and our dedicated safe room (where required) and open plan office can be used by ONS approved researchers. Potentially you could import ONS data into your LASER Virtual Research Environment (VRE), subject to user approvals.

### If your project is already in progress and has to move to LASER, how are teams going to be supported to understand cost and implications for budgets they have already agreed with their funders? 
Please contact the DAT as soon as possible ([ircdst@leeds.ac.uk](mailto:ircdst@leeds.ac.uk)) who will work with you to determine the requirements and cost to your project of using LASER.

### What if a project is delayed or the analysis is more complicated than you thought and there is no more money? Does your data just get deleted? 
Azure will continue to charge for each moment a VRE is live. If a project overruns the funding then the VRE will necessarily need to be deallocated until funding can be found. LASER does provide an offline 'mothball' functionality that can take the data out of a VRE and into storage that costs a fraction of an active and fully functional VRE. This may be an option you choose whilst further funding is sought. In this scenario we would recommend you talk to the DAT to discuss options. 

### How long does it take for the system to be set up especially from the point that LIDA puts the request in to IT for access to be provided to LASER storage space? 
It depends somewhat on the complexity of the VRE, but a standard VRE with a few VMs and some storage shouldn't take more than a week to build from the point the request is made to IT. The real time is taken up prior to requesting the build, whilst we work with you to identify the technical, governance and support requirements for your project, as well as designing the VRE and generating a costing estimate. This is why we recommend early engagement with DAT as part of LIDA’s Research Management Process (RMP).

### What if your project is currently using SEED, which has no charge, and has to move to LASER and we have no budget allocated to LASER in the grant, as the grant has been running for a number of years? 
If it has to move to LASER as it involves Tier 3/4 data or requires DSPT and is already on SEED, please contact the DAT to discuss funding options ([ircdst@leeds.ac.uk](mailto:ircdst@leeds.ac.uk)).  Where your project is not already on the IRC or SEED and scheduled to be migrating to LASER, funding will need to be identified either through external funders or locally by the faculty, school or institute.

###	This seems very expensive compared to SEED. What sort of things should we cut out from our proposal budgets to pay for LASER? 
LASER is a much more secure and high performing data analytics platform than SEED, and the cost is the cost of this performance, security, and compliance with various essential standards E.g., NHS Digital DSPT, ISO27001, NHS Cloud Security. 
Our experience to date is that funders have not had concerns regarding the 	
inclusion of LASER costs in grant proposals. During engagement with a few projects we have seen LASER costs relative to more comparable secure	platforms, such as AIMES, and we have found LASER to be the cheaper option.
We recommend you speak to the DAT as early as possible, who will work with you to identify the technical, governance and support requirements for your project and how costs can be minimized.

###	What is cost of equivalent to single ARC GPU node? 
That is difficult to answer. Not only are we talking about very different services, but a lot of ARC costs are "hidden". We don't (and can't) separate out costs for staffing, power, cooling, estates and so on, but it's in the nature of cloud you pay for it all in one charge. Similarly, you don't get the security and support for sensitive data that LASER and DAT provide when you use ARC. It's not really comparing like-for-like. GPU costs are quite expensive and certainly more so than HPC. We would expect that LASER is used for the 'last step' that can't be performed anywhere else. Transfer Learning would be an example here.

###	Is the time-limit per Virtual Machine (VM)? So if the 104 hours per month limit is reached, that VM can no longer be used for that month? 
You can use your VM for as long as you want - and can afford.  Azure charges by the millisecond. The 104 hours is not a limit to use but an assumption of expected usage used for budgeting purposes. Using a VM during normal office hours, after considering weekends, public holidays, annual leave and sickness, would equate to around 104 hours a month. If different usage patterns are expected then they will be reflected in the cost estimate that DAT will assist with generating.

###	From a practical perspective, presumably there will be a time lag to ingress data into LASER via DAT? How long do you intend it to take to ingress and egress data from the initial request? 
That depends largely on the volume and complexity of the transfer request. As mentioned, part of the governance wrap around is that the files are checked for compliance, the time for which can vary greatly. Ingress/egress is being developed currently. The aim is to provide a platform for users to manage their own data movements where the data is of Tier 3 risk (reasonable pseudonymisation). ETA is sometime later in the summer/early autumn. Meanwhile DAT will manage data movements on your behalf (as now with IRC).

###	Does it tend to be academics themselves or external partners who share data who deem the scale/sensitivity of the data to require the level of security provided by LASER? Just wondering how/when academics or professional services staff supporting them would know when it's appropriate/when to recommend. 
Data providers often classify their data (e.g personally identifiable, pseudonymised, anonymous) and share it based on a set of firm requirements detailed in a ‘Data Sharing Agreement (DSA). That would set the minimum standards. LIDA and/or PI/researcher may have a view that is that the data is more sensitive and might want more assurance than the provider contractually requires. So, it would all depend on the risk profile. It comes down to an assessment of the data classification but also the associated risks. A link to the LASER Data Risk Tiering document is [here](https://lida-data-analytics-team.github.io/laserdocs/docs/laser_info/tiering.html).
The usual model is that the data provider you are working with will set out the terms and conditions of how the data should be processed, stored and shared. If its personally identifiable (Tier 4) or weakly psuedonymised (Tier 3) for example, the project would need to user LASER. The researcher/project is responsible for working with their data provider to establish and agree what data is needed and the basis on which it will be used, but the UoL IG , the DAT team/LIDA will work with you on this to confirm /advise on data security requirements as part of the Research Management Process (RMP).

###	In terms of a tier 3 VM, would it be possible to make the VM read only? So a researcher would only be able to read data in the VM rather than being able to write? And tied in with this - protecting documents so they can't be copied from the VM?
And regarding software provisioning - you mention software centre and python. Is there scope for installing different tools so researchers can analyse data in specific ways?
Within a VRE it is possible to add specific permissions to folders and files based on user accounts. Movements of data into and out of VRE’s is controlled. For Tier 4 (the highest risk) then this is done by DAT - as a 'belt and braces' approach. For Tier 3 we are developing an application to support researcher control of movement, justified by lower risk. All movements will be logged for audit purposes, and to support a GDPR-compliant asset register. One of the benefits of using the LASER platform. 
There is scope for extra software, the limitation only really being the ability to work within a secure non-internet facing environment and you having a license for them, it may even already be available.

In all cases great care is needed with the data payload as there may be hidden potential for disclosure. The DAT can advise on the methods needed to assess and handle these sort of issues.

###	On the point about movements of data into and out of tier 4 VREs, will sufficient resource be guaranteed from the DST to authorise and process data moving in and out? This would be a potential issue for projects like PICANet where there are many hospitals pushing data in regularly (e.g. daily) and PICANet back out again. Is there a plan to place the responsibility back onto the Project PIs eventually? 
This is a very important point and the aim is to balance IG controls with practicalities. There may be other ways to better facilitate Tier 4 data processing, through separation of datasets, or using more advanced secure systems. This would be something to discuss with DAT during project design. This is particular challenge for patient-facing research needs, like PICANet.  

###	Is it possible for the user to install additional R packages? Previously in the IRC this required a request to the DAT team.
Users can install their own R packages. Currently DAT make packages available for users to install, and if we haven't made one available yet, you'll need to request it. There is already lots available for to install. Very soon, we'll be making offline mirrors of CRAN, PyPI and conda chanels available inside LASER, meaning you'll be able to install R packages and Python modules at will.

###	Will there be adequate secure rooms for everyone with Tier 4 data?
Historically there have been enough safe rooms to go around, and we expect that to continue to be the case. Safe rooms are booked per session rather than a single room being allocated to a single project for its duration. This flexibility allows us to serve many more projects than we have safe rooms.

###	How are safe rooms booked?
Safe rooms can be booked by contacting Kim Wright ([k.l.wright1@leeds.ac.uk](k.l.wright1@leeds.ac.uk)) or Karen Fletcher ([k.mendes@leeds.ac.uk](mailto:k.mendes@leeds.ac.uk)) once your VRE has been set up and you have been inducted by the DAT.

### Can projects be costed for use of LASER if it would not be required until later in the project timeline?
Yes, LASER has a flexible costing model which can adapt to the lifecycle of individual projects. When not using the platform, you would be subject to the standard storage costs,  with analysis costs only coming into effect when LASER is used. You only pay for the component you are using at any one time.
