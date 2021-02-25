---
layout: default
title: Backup & Retention
nav_order: 8
---

## LASER Backups 
 
‘Microsoft’s Azure Backup Service’ is a service that allows one to backup and restore data from the Azure cloud. This service will be utilised to protect and support the research projects hosted by the Azure platform underpinned by a backup policy and data retention requirements for any given VRE project.  

The Azure Backup Service is based upon the Microsoft Azure Recovery Services (MARS) agent and uses a Backup Service Vault, connected to Azure storage services. These agents will be utilised within the VRE environment, consisting of various Azure resources, such as VMs and File Shared Storage, SQL databases, Web App services and many more.  

## Backup Retention 

To develop both a consistent cost and support model an evolving set of standard expectations have been agreed and applied to the backup policies and data retention requirements across various VRE projects developed within the LASER service.  

By default, this will be a retention period based upon the backup policy schedule defined below of Daily VM backup and Storage backup at 7pm and 6:30pm respectively (UTC).  

Due to the agreed backup policies applied to each resource, restoration of services may take longer than expected. The following table describes the backup retention policy.  
 
|Backups/Snapshot |VM OS |Shared File Storage |
|---|---|---|
|Daily |7 days |28 days |
|Weekly |0 weeks |4 weeks |
|Monthly |0 months |12 months |
|Yearly |0 years |1 years |
 
A request must be made via the normal the ITS web form to recover data backed up by the Azure Backup Service.

