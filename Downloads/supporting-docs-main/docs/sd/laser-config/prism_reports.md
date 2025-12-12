---
layout: default
title: Prism Reports
parent: LASER Configurables
has_children: false
---

# Prism Reports  
[Link to report in Power BI Workspace](https://app.powerbi.com/groups/ce9a9888-7adc-465a-9c09-52f07991f744/reports/4160b3a0-b920-4a93-855b-86e70e83fb24?ctid=bdeaeda8-c81d-45ce-863e-5232a535b7cb&pbi_source=linkShare)

Power BI *.pbix files in GitHub repo; [https://github.com/LIDA-Data-Analytics-Team/DAT-Reports](https://github.com/LIDA-Data-Analytics-Team/DAT-Reports).  
Published to LASER Power BI Workspace.


## Data Sources
- Prism database  
	- server = lida-dat-cms.database.windows.net
	- database = lida_dat_cms
- Paul's KliqView report 
	- saved to Teams: DST --> General --> LRDP --> LASER Budget & Finance --> LIDA Grant reporting November 2022.xlsx
- Adeel's Budget report
	- saved to Teams: DST --> General --> LRDP --> LASER Budget & Finance --> LASER Project budget reporting template v7.xlsx

All sources are direct query.

## Reports  

### Project Stages  
An early demonstration piece with two visualisations that pull data from a single source:
1. Prism database (_vw_LaserProjects_Stage_x_Time_)


### LASER Activity  
This report consists of five visualisations pulling from three data sources:  
1. Prism database (_dbo.vw_LaserProjectsActive_) 
2. Paul's QlikView report  
3. Prism database (Project_x_Grant is an embedded query)

Relationships in the Power BI model map Projects to Grants via a junction table:  
-- Pauls QlikView (Grant) --> Project_x_Grant (KristalRef)
- Project_x_Grant (Projectnumber) --> vw_LaserProjectsActive (ProjectNumber)

**Visualisations**  
All visualisations show projects in Prism currently in an Active stage and on LASER.  
- Active Projects on LASER (Table)  
	- Pulls data from both **1** & **2**  
	- %FTE DAT Support can change over life of a project, values displayed here are for today's requirements in Prism.  
	- Worth noting that as some grants fund multiple projects in LASER, those grant values will appear more than once in the table. The way the data is sourced means that they are only counted once in the total.
- Count of Projects by Faculty and Classification (Stacked bar chart)  
	- Pulls data from **1** only  
- Count of Projects by Classification (Donut chart)
	- Pulls data from **1** only  
- Value of Projects by Faculty and Classification (Stacked bar chart)
	- Pulls data from both **1** & **2**  
- Value of Projects by Classification (Donut chart)
	- Pulls data from both **1** & **2**  


### Budget & Spend  
This report consists of two visualisations each pulling from a worksheet in Adeel's Budget report:  
1. LASER Migration Fund Budget  
2. LASER New projects

**LASER Migration Funding (Table)**  
Pulls data from **1**  

|Field|Column|Column name|
|---|---|---|
|2 year budget|K|2 year Azure budget inc. VAT (Final Azure cost)|
|Budget to date|R|Azure Budget (YTD inc VAT) - updated to 730 days|
|Spend to date|T|Dashboard - Incl VAT|
|Variance to date|AA|Variance YTD (inc VAT)|
|Forecast variance|AP|2 year Forecast Variance (annual forecast v 2 year azure budget)|

**Non-migrating LASER Projects (Table)**  
Pulls data from **2**  

|Field|Column|Column name|
|---|---|---|
|Total budget|H|Total LASER budget (incl. VAT)|
|Budget to date|M|Azure Budget (YTD inc VAT)|
|Spend to date|P|Actual cost (YTD inc VAT)|
|Variance to date|R|Variance YTD (inc VAT)|
|Forecast variance|AC|Project Forecast Variance (Project forecast v Total azure budget)|


### RIDM  
This report consists of three visualisations all pulling from a single data source:
1. Direct query to Prism database (_vw_AllProjects_x_AllGrants_x_AllPublications_)

The single view (a complex set of outer joins) should probably be replaced with three separate queries and relationships between the three data sources added in the Power BI report...  

Each table displays a selection of fields from the single query, and relationships between projects, grants and publications are maintained by virtue of existing on the same record.
