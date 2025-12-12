---
layout: default
title: LASER Dashboard
parent: LASER Configurables
has_children: false
---

# LASER Dashboard 

Used to provide activity and cost to researchers who are using LASER.  

[Power BI App](#power-bi-app)  
[Refresh](#refresh)  
[Data Sources](#data-sources)  
[Data Pipeline](#data-pipeline)  

## Power BI App
Any changes to the Laser Dashboard Power BI report need to be propagated through to the App.  

After publishing a change to the report to the LASER Power BI Workspace, one must navigate to the Workspace and click on the 'Update App' button at the top of the page.  

If you're not swapping reports it is enough to just click 'Update app' in the bottom right of the next screen.  

If changing reports (eg from v2.0 to v2.1) then you need to:
- add the new report to the app:  
    1. Content --> Add Content
    2. Select new report --> Add
    3. Click ellipses of old report and Delete
    4. Audience --> Make new report visible to the audience by clicking the eye icon
    5. 'Update app'
- re-add groups to RLS (see [Row Level Security](#row-level-security) below)  

### Granting access to App  
Researchers should be sent a link to the App to view the Dashboard reports, not directly to the reports themselves.  

This is the URL for the App:
[https://app.powerbi.com/Redirect?action=OpenApp&appId=38c333ec-3a1d-4b9f-8fdc-3b719c3f0055&ctid=bdeaeda8-c81d-45ce-863e-5232a535b7cb](https://app.powerbi.com/Redirect?action=OpenApp&appId=38c333ec-3a1d-4b9f-8fdc-3b719c3f0055&ctid=bdeaeda8-c81d-45ce-863e-5232a535b7cb)

Permission to both the App and the underlying dataset is granted to all LASER users who are members of these AD Groups, (see [Row Level Security](#row-level-security) below):
- LRDP-All-Citrix-Users
- LRDP-All-Citrix-Saferoom-Users

### Row Level Security  
Uses Row Level Security to filter visible projects to just those that the viewer is a member of. Workspace members assigned Admin, Member, or Contributor have edit permission for the dataset and, therefore, RLS doesn’t apply to them.  

`DashboardUsers` role has been created in the Power BI report (Modelling --> Manage roles), with a filter on data source `vw_LaserActiveGroupMembers` of `[UserPrincipalName] = userprincipalname()`.  

Many:many relationship established in report model between vw_LaserActiveGroupMembers and vw_LaserUsageCosts on Projectnumber, with 'Apply security filter in both directions' checked.  

AAD Groups `LRDP-All-Citrix-SafeRoom-Users` and `LRDP-All-Citrix-Users` added as members of the `DashboardUsers` role from Power BI workspace (Semantic model --> Elipses --> Security).  

In this way all LASER users (ie members of `LRDP-All-Citrix-SafeRoom-Users` and `LRDP-All-Citrix-Users`) can access the Dashboard as members of the `DashboardUser` role, and the content is filtered to projects they are a member of.  

## Refresh
Set to automatically refresh from Power BI Workspace three times a day; 09:00, 13:00 & 17:00.

Uses SQL Server Authentication against Prism database. the contained user has been made a member of the db_datareader role. The details are in DAT's KeePass.

## Datasources  
As a first design principle, views are created on the SQL Database to use as data sources within the report. In this way data can be pre-processed outside of the report and within the database.  

### DimDate  
Used because "dates are hard". Provides mapping for dates stored in various formats. Useful when date hierarchies are required.  

Relationships created in Power BI to join to date fields in other data sources.  

### vw_LaserUsageCosts  
Uses `[dbo].[tblLaserUsageCosts]` as a primary source table.  

Left joins to `[dbo].[vw_AllProjects]` on ProjectNumber, which is extracted as a substring from `[ResourceGroup]` using the following logic:  
```sql
-- most resource groups follow standard naming convention that includes project number. There are a couple of exceptions...
, case when substring([ResourceGroup], 14, 7) = 'picanet'
        then 'p0001'
    when substring([ResourceGroup], 14, 8) = 'picnetv2'
        then 'p0001'
    else substring([ResourceGroup], 14, 5)
    end as [Projectnumber]
```
All records with a Resource Group that doesn't contain a ProjectNumber on the Prism record (as extracted above) are flagged as 'Infra' in the field `[Project]`, which otherwise is a concatenation of ProjectNumber & ProjectName. 

`[ResourceName]` is taken from `[ResourceId]` as the last token in the string.  

`[ResourceType]` & `[ResourceCategory]` are taken as substrings from the source field `[ResourceType]`. Eg:  
> Source ResourceType = microsoft.compute/virtualmachines  
> View ResourceType = virtualmachines  
> View Resource Category = compute  

### vw_LaserActiveGroupMembers  
Uses `[dbo].[tblLaserAADGroupMembers]` as a primary source table.

Left joins to `[dbo].[vw_AllProjects]` on ProjectNumber, which is extracted as a substring from `[GroupDisplayName]` using the following logic:  
```sql
-- most AD group names follow standard naming convention that includes project number. The are a couple of exceptions...
, case when [GroupDisplayName] like '%picanet%'
        then 'p0001'
    when [GroupDisplayName] like '%picnetv2%'
        then 'p0001'
    else substring([GroupDisplayName], 5, 5)
    end as [Projectnumber]
```
`[UserPrincipalName]` is used in the Row Level Security filter to determine which `[ProjectNumber]` the viewer is a member of and therefore which project details should be permitted for viewing.

### vw_LaserActiveResources
Uses `[dbo].[tblLaserResources]` as a primary source table.  

Left joins to `[dbo].[vw_AllProjects]` on ProjectNumber, which is extracted as a substring from `[ResourceGroup]` using the following logic:  
```sql
-- most resource groups follow standard naming convention that includes project number. The are a couple of exceptions...
, case when substring([ResourceGroup], 14, 7) = 'picanet'
	then 'p0001'
	when substring([ResourceGroup], 14, 8) = 'picnetv2'
		then 'p0001'
	else substring([ResourceGroup], 14, 5)
	end as [ProjectNumber]
```
All records with a Resource Group that doesn't contain a ProjectNumber on the Prism record (as extracted above) are flagged as 'Infra' in the field `[Project]`, which otherwise is a concatenation of ProjectNumber & ProjectName.  

## Data Pipeline

Details of the azure function app can be found in the README.md of the Github repository:
[https://github.com/LIDA-Data-Analytics-Team/laser-activity](https://github.com/LIDA-Data-Analytics-Team/laser-activity)

### Key azure resources:
- Resource group = "UoL-uks-LRDP-dashboard-prod-rg"
- App registration = "LASER Dashboard Prod"
- keyVaultName = "UoL-uks-LRDP-Ops-Prod-kv"
	- secretName = "LASERDashboardProd"

### Client Secret Expiry:  
The function laser_users authenticates against the Microsoft Graph API via App Registration secret.  

The secret has an expiry and will need renewing each year. There is a calendar entry in the DAT calendar to remind us when to do this.  

DAT should all be Owners of the necessary resources but should there be any issues contact IT Services (Cloud Team) for support.  

From the Azure Portal:
- **EntraID** --> **App registrations**  
- Search for and select _'LASER Dashboard Prod'_  
- **Certificates & secrets**  
- **+ New Client Secret**  
	- Description = "LASER Dashboard Prod"
	- Expires = 12 months
- Copy generated `Value`  

- **Key Vaults** --> **UoL-uks-LRDP-dashboard** --> **Secrets** --> **LASERDashboardProd**  
- **+ New Version**  
	- Upload options = Manual
	- Secret value = paste `Value` from new client secret generated above  
	- Set activation date = now
	- Set expiration date = 12 months from now (matching expiration of new client secret generated above)
	- Enabled = Yes
- Ensure any existing **Older Versions** are _Disabled_  

- When satisfied new secret is functional, by testing the Dashboard _laser_users_ function, delete the old expired/expiring Client Secret from the _'LASER Dashboard Prod'_ App registration
