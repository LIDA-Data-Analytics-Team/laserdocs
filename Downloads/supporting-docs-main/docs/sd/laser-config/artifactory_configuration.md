---
layout: default
title: Artifactory Configuration
parent: LASER Configurables
has_children: false
---

# Artifactory Config

The Artifactory administrator credentials are saved to KeePass. You will need to be logged in as an admin to configure Artifactory from within the web GUI.

Below are the configuration settings for the screens in the web GUI that have had the configuration changed from factory defaults. Changes to the backend database and storage account are not made within the web GUI. For these configurations please follow the JFrog Support articles:  
	[Point Artifactory to SQL Database](https://www.jfrog.com/confluence/display/JFROG/Microsoft+SQL+Server)  
	[Point Artifactory to Storage Account](https://www.jfrog.com/confluence/display/JFROG/Configuring+the+Filestore)  

Copying the below configuration values should mean that any LASER user can log in to Artifactory web GUI using their University of Leeds credentials and be able to set up and use any of the airgapped repositories. 

---  

[**Back End**](#back-end)  
[SQL Database](#sql-database)  
[File Share](#file-share)  
[Service](#artifactory-service)  
[**Front End**](#front-end)  
[Repositories](#repositories)  
[Identity and Access](#identity-and-access)  
[Security](#security)  
[Licenses](#licenses)  
[General](#general)  

---  

## Back end  

### SQL Database  
Artifactory uses a local 'Derby' database by default but that's not appropriate for production. We have an Azure SQL Database to use (_artifactory3-db_); to do so we need to:  
- add the connection details to `system.yaml` found in `C:/JFrog/artifactory/var/etc`
- ensure the drivers are available to the service


#### Edit system.yaml  
Make sure the following code snippet is included in the file:  

```yaml
shared:
    database:
        type: mssql
		driver: com.microsoft.sqlserver.jdbc.SQLServerDriver
		url: "jdbc:sqlserver://az-lrdp-artifactory-db.database.windows.net:1433;databaseName=artifactory3-db;sendStringParametersAsUnicode=false;applicationName=Artifactory Binary Repository"
		username: artifactory-user2
		password: <found in KeePass>
```  

On first run, the Artifactory service will encrypt the password within the `system.yaml` file. 

#### SQL Drivers
If there are no SQL.jar files in `C:/JFrog/artifactory/app/artifactory/tomcat/lib` they will need adding. 
- Download the [latest Microsoft JDBC SQL Drivers](https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server).  
- Extract and put the *.jar files directly in the folder above. Just chuck 'em all in.  

### File Share  
By defult Artifactory stores local copies of binaries to the C: drive of where it's installed. We need to point it at the File Share we have for this purpose instead, `azlrdpartifactory.file.core.windows.net/artifactory`. 

Ensure the following code snippet is included in the `binarystore.xml` file found at `C:/JFrog/artifactory/var/etc/artifactory`:  

```xml
<config version="1">
	<chain template="file-system"/>
	<provider id="file-system" type="file-system">
		<baseDataDir>\\azlrdpartifactory.file.core.windows.net/artifactory/binaries</baseDataDir>
		<fileStoreDir>/filestore</fileStoreDir>
		<tempDir>/temp</tempDir>
	</provider>
</config>
```

The account that the srvice runs as needs to be granted permissions over the storage account.  
Ensure user `zz_artifactory_srv` is a member of role `Storage File Data SMB Share Contributor`.  

### Artifactory Service

#### Service Log On As
The artifactory service will need to run as an administrator. 
There is a service account set up for artifactory, `zz_artifactory_srv`. 
The account used for the service to log on can be changed from DAT01:
- Start menu --> Services
- Find the Artifactory service, right click, properties
- Log On tab allows you to enter the service account credentials
	- password available in KeePass

#### Status 
The status of the Artifacory Service can only be checked from DAT01 (via DAT02 > Remote Desktop Connection > Computer: `az-lrdp-dat01`).

Check the status of the artifactory service by logging in to DAT01, opening cmd and run as an administrator  

```
sc query artifactory
```

#### Start/Stop
If the service is STOPPED it can be started with the command:  

```
sc start artifactory
```

If you need to stop the service run the command:  

```
sc stop artifactory
```

#### Stuck at STOPPING
If you stop the service and subsequent `query` commands show that the service has hung in a STOPPING state it is possible to kill the service. Note that it may take a while to stop fully, possibly because the Java instance has a large amount of memory allocated. You will need to be running cmd as an administrator.

First find the PID of the service by running the command  

```
sc queryex artifactory
```

Then run the following command, substituting [PID] with the value obtained from the above `queryex` command  

```
taskkill /f /pid [PID]	
```

After running `taskkill` check the processes running on dat01 using task manager to see whether there is an instance of OpenJDK Platform binary using a lot of memory, but whose CPU/memory values are unchanging. This may be a dead instance of Java that was not shut down when killing the artifactory task. Hit end task to kill the Java instance and free up the allocated memory before restarting artifactory.  

### extraJavaOpts  
Before starting Artifactory, edit C:\JFrog\artifactory\var\etc\system.yaml. In the shared configurations, uncomment extraJavaOpts and change the entity to increase Java's maximum heap size to 4 GB:<br>
`extraJavaOpts: "-Xms512m -Xmx4g"`

If extraJavaOpts key doesn't exist in system.yaml, copy and paste it from system.basic-template.yaml, making sure to paste it into the same section (using the right level of indentation in system.yaml).
	
Artifactory has documentation on [configuring system.yaml](https://www.jfrog.com/confluence/display/JFROG/System+YAML+Configuration+File) and [setting Java memory parameters](https://www.jfrog.com/confluence/display/JFROG/Installing+Artifactory#InstallingonWindows-SettingJavaMemoryParameters) specifically.
	
If you encounter the following error in access-service.log, you may need to further increase Java's max. heap size by increasing the number after the `-Xmx` option:
`Unexpected error occurred in scheduled task java.lang.OutOfMemoryError: Java heap space`
	
The errors reported via Artifactory UI when we first encountered this issue:
- Component: Access
	- Error: Get "http://localhost:8040/access/api/v1/system/ping": context deadline exceeded
- Component: Artifactory
	- Error: Get "http://localhost:8091/artifactory/api/system/ping?skipLicenseCheck=true": dial tcp 127.0.0.1:8091: connectex: No connection could be made because the target machine actively refused it.

These errors may come up for other underlying issues, but in any case if they occur check the log files for clues.

## Front end  

### Repositories   
#### Repositories  

Each airgapped repo consists of a local, remote and virtual repository in Artifactory. The local repository exists on the artifactory storage account within LASER; the remote is online and the virtual is what the users connect to. The virtual repo pulls together both local and remote, so that artifactory will only download from the internet if a copy of the desired package is currently unavailable locally. Once downloaded it will be available locally for future installations. 

To create a new repository in Artifactory you must create one of each local, remote and virtual:
- Create Local
	- '+ Add Repositories'
	- 'Local Repository'
	- Repository Key = LASER\_[repo]_local	
	- All else default values
- Create Remote
	- '+ Add Repositories'
	- 'Remote Repository'
	- Repository Key = LASER\_[repo]_remote
	- All else default values
- Create Virtual that links local & remote
	- '+ Add Repositories'
	- 'Virtual Repository'
	- Repository Key = LASER\_[repo]_virtual
	- Move LASER\_[repo]\_local and LASER\_[repo]\_remote from **Available Repositories** to **Selected Repositories**
	- All else default values

### User Management  
On successful login a user account is created within Artifactory, from which access is managed. All Artifactory Users are by default added to an Artifactory Group that has appropriate permissions to the air gapped repositories.

#### Groups
- Group Name = LASER_Users
- Description = [empty]
- Administrater Platform = FALSE
- Manage Resources = FALSE
- Automatically Join New Users to this Group = TRUE

#### Permissions
- Name = LASER_Users_Permissions
- Resources 
	- Repositories = All required local and remote repositories (i.e. LASER_CRAN_local, LASER_Conda_local, LASER_PyPI_local, LASER_CRAN_remote, LASER_Conda_remote, LASER_PyPI_remote)
	- Builds = [empty]
- Users = [empty]
- Groups 
	- Selected Groups = LASER_Users
		- Repositories 
			- Read = TRUE
			- Annotate = FALSE
			- Deploy/Cache = TRUE
			- Delete/Overwrite = FALSE
			- Manage = FALSE

### Authentication Providers  
All LASER users should be able to log in to Artifactory web GUI using their University of Leeds credentials. The below settings map Artifactory to the Azure Active Directory for authentication. 

#### LDAP
LDAP Settings
- Enabled = TRUE
- Settings Name = Artifactory_AD_Sync
- LDAP URL = ldap://az-uks-adds01:389/dc=ds,dc=leeds,dc=ac,dc=uk
- Auto create users = TRUE
- Allow Created Users Access To Profile Page = TRUE
- Use Paged Results = TRUE
- User DN Pattern = [empty]
- Email Attribute = mail
- Search Filter = sAMAccountName={0}
- Search Base = [empty]
- Secure LDAP Search = TRUE
- Manager DN = CN=zz_artifactory_srv,OU=O365,OU=System Accounts,OU=ISS,OU=ACS,OU=Resources,DC=ds,DC=leeds,DC=ac,DC=uk
- Manager Password = [in KeePass]


LDAP Group Settings
- Settings Name = LDAP Dynamic Group
- LDAP Setting = Artifactory_AD_Sync
- Mapping Strategy = Dynamic
- Group Member Attribute = memberOf
- Group Name = cn
- Description Atrribute = description
- Filter = (objectClass=group)
- Search Base = [empty]
- Sub-tree Search = TRUE
- Synchronise LDAP Groups = [empty]

### License Details  
#### Licenses  
- Licence Key = [paste full key]

To update the licence:
- Log into Artifactory UI with an admin account
- In Administration section, go to Licenses > Licenses
- Replace the old licence key in the text box with the new licence key
- Click Save and check the licence details are correctly updated

### General
#### Settings
- Server Name = [empty]
- Custom Base URL = http://artifactory:8082
- Date Format = dd-MM-yy HH:mm:ss z
- Enable Help Component = TRUE
- Look & Feel = [empty]
