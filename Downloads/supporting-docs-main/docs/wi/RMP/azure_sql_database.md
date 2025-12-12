---
layout: default
title: New SQL User
parent: RMP
has_children: false
---

# LASER & Azure SQL Database

## Managing access

A contained database user does not have a login in the master database, and maps to an identity in Azure AD that is associated with the database. The Azure AD identity can be either an individual user account or a group. 
[More info here](https://docs.microsoft.com/en-us/azure/azure-sql/database/authentication-aad-configure?tabs=azure-powershell#create-contained-users-mapped-to-azure-ad-identities). 

Access to databases within LASER is managed via Active Directory group membership.  
When granting access to new users, check for the existence of an AD group with the appropriate database role nomenclature.  
If it already exists, you can simply add users to that group to grant access to the database with that role membership.  
Otherwise, follow the steps below.  

### Create a new Active Directory Group 

- In Active Directory Users & Computers navigate to the VRE OU
	ds.leeds.ac.uk --> Resources --> LRDP --> VRE --> Groups --> [VRE Name]
  - 'Create a new group in the current container' 
	- Name the group 'VRE-p####v##-db-[db role]'
	- Group scope = Universal
	- Group type = Security
- Add 'LRDP-DAT-Admins' and all appropriate research users as members 
- Wait up to an hour before moving on for AD to sync with AAD

### Create an Azure AD-based contained database user

- Connect to the research database.
- Create the user on the database:
  ```TSQL
  CREATE USER [VRE-p####v##-db-<db role>] FROM EXTERNAL PROVIDER;
  ```
- Add the user to a database role:
  ```TSQL
  ALTER ROLE [db_owner] ADD MEMBER [VRE-p####v##-db-<db role>]
  ```
- Instruct researcher to change/specify database in connection string.
  - If using SSMS that can be done from the second tab after clicking the 'Options >>' button.
  - Connect to database = [database name]  
  - Otherwise:
    ```
    Server=tcp:<serverName>.database.windows.net;Database=<database name>;
    ```
  
![db role image](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/media/permissions-of-database-roles.png) 

[More info on database roles here](https://docs.microsoft.com/en-us/sql/relational-databases/security/authentication-access/database-level-roles).

## Uploading data to Azure SQL Database


Few applications currently support 'Azure Active Directory - Interactive' authentication, including the SQL Server Management Studio Import Wizard. The only driver that currently supports it is 'ODBC Driver 17 for SQL Server'. It must be installed on the machine that is running the upload.

The driver is available [here](https://docs.microsoft.com/en-us/sql/connect/odbc/download-odbc-driver-for-sql-server?view=sql-server-ver15).  

The following Python code snippet should be enough to get you started with a **single file**:
```PYTHON
# Database Tables must already exist.

import pandas as pd
from sqlalchemy import create_engine
import urllib

username = <username>@leeds.ac.uk
file = (r'<FILE PATH\FILE NAME>')
sql_server = '<SQL SERVER NAME>'
sql_database = '<DATABASE NAME>'
sql_schema = '<SCHEMA NAME>'
sql_table = '<TABLE NAME>'
chunksize = 100000

def csv_to_sql(username, file, sql_server, sql_database, sql_schema, sql_tablename): 
        conn = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:" + sql_server + ";DATABASE=" + sql_database + ";UID=" + username + ";Authentication=ActiveDirectoryInteractive")
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn, fast_executemany=True)
        for chunk in pd.read_csv(file, chunksize=chunksize):
            df = pd.DataFrame(chunk)
            df.rename(columns=df.iloc[0])
            df.to_sql(sql_tablename, con = engine, if_exists = "append", schema = sql_schema, index = False)
```

The following Python code snippet should be enough to get you started iterating through **multiple files**:
```PYTHON
# Database Tables must already exist.

import pandas as pd
from sqlalchemy import create_engine
import urllib
import os

username = <username>@leeds.ac.uk
filepath = (r'<FILE PATH TO TARGET DIRECTORY>')
sql_server = '<SQL SERVER NAME>'
sql_database = '<DATABASE NAME>'
sql_schema = '<SCHEMA NAME>'
sql_table = '<TABLE NAME>'
chunksize = 100000

def csv_to_sql(username, directory, file, sql_server, sql_database, sql_schema, sql_tablename): 
    name, ext = os.path.splitext(file)
    if ext == '.csv': 
        conn = urllib.parse.quote_plus("DRIVER={ODBC Driver 17 for SQL Server};SERVER=tcp:" + sql_server + ";DATABASE=" + sql_database + ";UID=" + username + ";Authentication=ActiveDirectoryInteractive")
        engine = create_engine("mssql+pyodbc:///?odbc_connect=%s" % conn, fast_executemany=True)
        for chunk in pd.read_csv(os.path.join(directory,file), chunksize=chunksize):        
            df = pd.DataFrame(chunk)
            df.rename(columns=df.iloc[0])
            df.to_sql(sql_tablename, con = engine, if_exists = "append", schema = sql_schema, index = False)

for directory, subdirectories, files in os.walk(filepath):
    for file in files: 
        csv_to_sql(username, directory, file, sql_server, sql_database, sql_schema, sql_tablename)
```

	
## Connection troubles
	
### Requested tenant identifier is not valid. Tenant identifiers may not be an empty GUID
	
This error indicates that the Active Directory admin is not configured. Go to the SQL Server page in the Azure Portal and check whether Active Directory admin is showing as not configured. If so, inform server team. They need to set LRDP-SQL-Admins as the Active Directory admin.
