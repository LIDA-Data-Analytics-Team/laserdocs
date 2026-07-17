---
layout: default
title: SPSS and SQL Database
parent: Install & Use Software
grand_parent: LASER How To
nav_order: 6
---

# SPSS Statistics & Azure SQL Database

From Software Centre ensure that first **IBM SPSS** and then **IBM Data Access** are installed to the VM.  

IBM Data Access installs drivers required for SPSS Statistics to connect to  Azure SQL Databases.  

The 'SQL Server Wire Protocol' driver you'll be using only supports _Windows Authentication_ and _SQL Authentication_. Azure SQL Databases do not support _Windows Authentication_ however.  

**The DAT can help set you up with a SQL Authentication login if required**.  

{: .important }
> During installation of IBM Data Access you will be asked to select file paths and settings; just accept all defaults and hit 'Next' until completion.  
>  
> There are 3 installations to go through; be aware some windows may open behind others, so be prepared to use Alt+Tab to bring windows to the front.  

## Querying an Azure SQL Database from SPSS Statistics  
1. From SPSS Statistics Data Editor, go to File --> Import Data --> Database --> New Query  
1. In the Database Wizard select the required ODBC Data Source  
    - If the source list is empty:  
        - Click 'Add ODBC Data Source' to open the 'ODBC Data Source Administrator'.  
        - Select the 'System DSN' tab  
        - Click 'Add'
        - Find and select 'IBM SPSS OEM 7.1 SQL Server Wire Protocol' --> Finish  
        - On the 'ODBC SQL Server Wire Protocol Driver Setup' window:  
            - General Tab  
            `Data Source Name` = Something to identify the data source, eg. "SQL Wire"  
            `Host Name` = \<ServerName>.database.windows.net  
            `Port number` = 1433  
            `Database` = \<Database Name>  
            - Security tab:  
            `Authentication Method` = 1 - Encrypted Password  
            `Encryption Method` = 1 - SSL  
            `Validate Server Certificate` = Unchecked  
            - Click 'Test Connect' and enter your SQL credentials --> OK  
            - If "Connection established!" --> OK to close all windows and return to the Database Wizard, else check settings and try again.  
1. Make the appropriate table type selections and click Next  
1. Enter your SQL Server login credentials --> OK  
1. Connection made! Continue with the onscreen instruction to import your data.  

