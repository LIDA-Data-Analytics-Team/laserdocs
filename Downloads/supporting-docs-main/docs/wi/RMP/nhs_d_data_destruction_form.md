---
layout: default
title: NHS Digital Destruction Form
parent: RMP
has_children: false
---

## NHS Digital Data Destruction form and VRE Destruction Certificate

Projects which use NHS Digital data will be required to complete and submit an NHS DIgital [data destruction form](https://digital.nhs.uk/about-nhs-digital/corporate-information-and-documents/records-and-document-management-policy/retention-and-disposal-form-and-destruction-certificate)  



This form is to be completed by the VRE user and the DAT team and signed off by the DAT team member involved with the data/VRE destruction task.  

### For the NHS D data destruction form  
**‘Details of the Media used to store the Data that is subject to Destruction’**   
o	Media Type = Azure Storage Account (StorageV2 (general purpose v2))  
o	Asset Number(s) = FileIDs from [dbo].[tblAssetsRegister] in Prism - This can be queried on the database as thus:
> ***select *  
from [dbo].[tblAssetsRegister]  
where Project = 'ProjectID'

o	All else n/a  
**‘DESTRUCTION DETAILS’**  
o	Method of Destruction = Deleted from Azure File Store subject to [Microsoft Azure Data Protection Policy](https://www.microsoft.com/en-gb/trust-center/privacy/data-management?rtc=1#:~:text=Data%20deletion%E2%80%9D%20is%20discussed%20on%20page%2021%20in%20the%20Data%20Protection%20in%20Azure%20document.)   
o	All else n/a  
**‘DETAILS OF ALL DATA BACK UPS’**  
o	Confirm your Backup Retention Period(s) = See ‘Shared File Storage’ here: https://lida-data-analytics-team.github.io/laserdocs/docs/laser_info/backups.html   
o	Have all Backups, Disaster Recovery and Shadow copies been destroyed = No  
o	If you answered no to the above question what is your approach to the destruction of the data on your backups? = Allowed to cycle out of the retention schedule  

### For the VRE Destruction Certificate
o The form template can be found at:
> N:\Academic-Services\ISS\IRC-Data-Services\Processes\ISMS\Work Instructions\supporting-docs\templates

(VRE destructions are authorised by PIs signing a project closure form.)  
o Save the Project Closure Form as pdf when when the form is completed as signed as below P***_Project Closure form vX.Y.docx. where X.Y is the document version. File a signed copy in the project's records folder on N: drive.

o Provide the Project ID, Project Name and VRE ID    
o Send the document to the PI/Lead Researcher to sign  
o Send the signed copy to DAT IG manager to sign  
o DAT team member to sign and save document as pdf and send to user/PI/Lead applicant.   
    o The fully signed PDF copy of the VRE destruction certificate to be attached to the NHS D data destruction form and sent to the enquiries@nhsdigital.nhs.uk by user/PI/Lead applicant quoting “HSCIC agreements expiry and data destruction” in the subject:


Proceed as usual with other processes of [VRE Destruction](vre_destroy.md).
