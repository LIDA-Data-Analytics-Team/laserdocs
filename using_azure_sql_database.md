---
layout: default
title: Using Azure SQL Server
nav_order: 6
---

## Connect to database via SSMS

When SSMS opens you will be prompted for the connection details.  
	![ssms_connect_to_server_1.png](./images/using_azure_sql_database/ssms_connect_to_server_1.png)

Enter the following:
- Server type = `Database Engine`
- Server name = `<ServerName>.database.windows.net`
- Authentication = `Azure Active Directory - Integrated`

Click 'Options >>' and go to the second tab 'Connection Properties'.  			!		
	![ssms_connect_to_server_2.png](./images/using_azure_sql_database/ssms_connect_to_server_2.png)

Change 'Connect to database' from \<default> to `<database name>`.

## Connect to database via research software

Your connection string will need to include at least the server name, database name, driver name and authentication type. 

Azure SQL Database server names take the form `<ServerName>.database.windows.net`.

LASER uses 'Azure Active Directory - Integrated' authentication to enable Contained Users to connect to Azure SQL Databases.

Few ODBC drivers currently support 'Azure Active Directory - Integrated' authentication, including 'SQL Server Native Client 11.0'. A driver that does support it is '**ODBC Driver 17 For SQL Server**', so this must be specified in your connection string.

Example connection string: `con = "DRIVER={ODBC Driver 17 for SQL Server}; SERVER=tcp:<Server Name>.database.windows.net; DATABASE=<Database Name>; AUTHENTICATION=ActiveDirectoryIntegrated"`
