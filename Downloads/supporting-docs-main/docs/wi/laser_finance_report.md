---
layout: default
title: Budget Report
parent: Work Instruction
has_children: false
---

# LASER Finance Report

Each fortnight, ahead of Project Board, we need to update the LASER budget report:  

LASER Project budget reporting template v6 yyyy-mm-dd.xlsx
N:\Academic-Services\ISS\IRC-Data-Services\Service Management\LASER Finance

Copy last report, move to /Old and rename copy with today's date.  
Open the new workbook and 'Refresh all'.  

In portal, download to *.csv '[All Resources](https://portal.azure.com/#blade/HubsExtension/BrowseAll)'

Extract budget Codes to new column using below formula, where cell reference $AX2 is the 'TAGS' field
```
=IFERROR(LEFT(MID($AX2,FIND("Budget Code",$AX2,1)+14,50),FIND(",",MID($AX2,FIND("Budget Code",$AX2,1)+14,50),1)-2),LEFT(MID($AX2,FIND("Budget Code",$AX2,1)+14,50),FIND("}",MID($AX2,FIND("Budget Code",$AX2,1)+14,50),1)-2))
```
Copy columns 'RESOURCE GROUP' and new 'Budget Code' to new work sheet.

Extract project numbers from 'RESOURCE GROUP' using formula
```
=MID($A2,14,5)
```

Remove duplicates, and any non-project resources (ie project number not in format p#### or s####)

Confirm all projects are listed in report, either in Migration or New Projects worksheet. The formulas in the table below should help with this.  

|Column Name|Formula|
|---|---|
|RESOURCE GROUP||
|BUDGET CODE||
|pNum|=MID(A2,14,5)|
|VRE/Account code Count|=COUNTIF(C:C,C2)|
|In Migration|=COUNTIF('[LASER Project budget reporting template v6 yyyy-mm-dd.xlsx]LASER Migration Fund Budget '!$B:$B,C2)|
|In New|=COUNTIF('[LASER Project budget reporting template v6 yyyy-mm-dd.xlsx]LASER project budget'!$A:$A,C2)|
|Sum In|=SUM(E2,F2)|

Make a note of any that are present in list twice due to multiple 'Budget Codes' and include them in the email to Adeel.  
Any in the list due to the same project having multiple VREs but on the same budget codes do not need to be called out.  

Email Adeel Hussain to let him know the report has been updated, eg:

```
Hello Adeel,

I’ve updated the LASER project budget/spend spreadsheet for this week and saved to the usual spot. 

N:\Academic-Services\ISS\IRC-Data-Services\Service Management\LASER Finance
LASER Project budget reporting template v6 2022-02-04.xlsx

The projects that need to be split across the two work sheets (on different account codes) are:
- On migration & project funding:
    - p0171
    - p0225
    - p0226
- Now on migration fund only:
    - p0073

If you have any questions please do let me know.

Many thanks,
```


