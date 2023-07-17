---
layout: default
title: LASER Dashboard
parent: LASER How To
nav_order: 4
---

# LASER Dashboard
{:.no_toc}

The LASER Dashboard has been created to assist with managing and monitoring costs and activity in LASER.  

You can navigate to the LASER Dashboard by following this link and logging in using your University of Leeds credentials:  
[LASER Dashboard](https://app.powerbi.com/Redirect?action=OpenApp&appId=38c333ec-3a1d-4b9f-8fdc-3b719c3f0055&ctid=bdeaeda8-c81d-45ce-863e-5232a535b7cb)  

Information on each report can be found below.  

* seed list
{:toc}

The underlying **data is refreshed each morning starting at 07:00** and the Power BI report pulls this data into the LASER Dashboard model at 09:00 each morning. 

If you receive the below message please [request a PowerBI licence](https://it.leeds.ac.uk/it?id=sc_cat_item&sys_id=8a89d8031b2ff010d530eb53b24bcbc9) from IT Services:  

	"Your IT department has turned off signup for Microsoft Power BI. Contact them to complete signup"  

## Power BI Reports

Row Level Security is in place to ensure LASER users can only see the details of projects they are currently members of. 

Common across all reports are a set of slicers at the top of the page that allow filtering to Project, Resource Group and/or Budget Code (where appropriate). 
- **Project**: The project on LASER under which the VRE(s) are logically organised  
- **Resource Group**: Each VRE exists within a _Resource Group_ in Azure. If you have multiple VREs under the same project (eg a Tier 4 and a Tier 3 VRE) they will each exist within a _Resource Group_ with a distinct name. You can find out the names of your VRE _Resource Groups_ from the LASER Storefront under the Description of each VM or by asking a member of the DAT  
- **Budget Code**: Each _Resource_ is tagged with a budget code, against which the costs of that resource will be charged. Some VREs may have multiple Budget Codes, though a single resource can only be tagged by a single Budget Code  

**Filters** can be applied or removed by clicking on an chart or table within a report and looking to the 'Filters' blade that appears to the right of the report.  

Table **columns can be expanded** by selecting _'Drill on: Columns'_ and then _'Expand all down one level in the hierarchy'_ from the header icons that appear when hovering the mouse over the table.  

Tables can be **sorted** by any column. Multiple columns can be chosen for sorting by holding Shift when you click.  

All changes made to filters, slicers, drill downs, sorts etc. can be reset to default by clicking on the **'Reset'** button at the top right of the report.  

The LASER Dashboard consists of the following suite of reports:  

### Project Costs  
This report constists of two elements:
- Chart: Costs accrued over time by project as stacked columns with a budget line on a secondary axis  
- Table: Breakdown of costs over time by project. Can drill down from yearly to daily costs by _Resource Group_ and then by _Budget Code_  

### Resoure costs  
This report constists of two elements:
- Chart: Costs accrued over time by _Resource Category_ as stacked columns
- Table: Breakdown of costs over time by project. You can drill down from yearly to daily costs by:  
    - _Resource Group_
    - _Resource Category_
    - _Resource Type_
    - _Resource Name_
    - _Meter Category_
    - _Meter Subcategory_
    - _Meter_

### Resources  
Here all resources currently active in LASER can be found. By default, just the following _Resource Types_ are displayed:  
- Virtual Machines
- Storage Accounts
- SQL Servers & Databases
The Filters blade will allow you to include or exclude additional items.  

The resources are grouped by _Project_ and _Resource Group_ and some essential information is included in the list such as:  
- VM size  
- current budget code  
- total cost accrued by that specific resource to date  

### VM Activity  
Here you can see a list of Virtual Machine start & stop times as well as run durrations.  

By default this page displays activity from teh last 30 days but this can be changed with filters.  

It is not possible to show who started a Virtual Machine if it was done so via the Citrix Storefront. This activity will display with a _StartedBy_ of 'Citrix User'. Only VMs that were started from the Azure Portal will have a user name associated with that activity.  

VMs that were running at the time of data refresh will not have a _VmStopped_ time and will be higlighted in blue.  

VM sessions that had lasted for longer than 24 hours will be highlighted in red.  

### User Information  
All users who have access to some element of your project in LASER are listed here, next to the project they are able to access.  
