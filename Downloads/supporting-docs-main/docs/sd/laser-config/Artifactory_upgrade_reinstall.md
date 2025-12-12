---
layout: default
title: Artifactory Upgrade/Install
parent: LASER Configurables
has_children: false
---

# Artifactory Upgrade / Reinstall

Artifactory is installed to and runs from DAT01, which can be remoted to from DAT02.

These steps are adapted from guidance here:  
[artifactory-version-7.x-to-7.x-windows-upgrade](https://jfrog.com/help/r/jfrog-installation-setup-documentation/artifactory-version-7.x-to-7.x-windows-upgrade)  
[install-artifactory-single-node-on-windows](https://jfrog.com/help/r/jfrog-installation-setup-documentation/install-artifactory-single-node-on-windows)  

## Upgrade
1. Download [latest Artifactory files from here](https://jfrog.com/download-jfrog-platform/#artifactory). JFrog Artifactory - Windows.  
2. Download [JDBC SQL Drivers from Microsoft](https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server).  
3. Transfer them through to `//azlrdpartifatory.file.core.windows.net/user_files/Installation`.  
4. Extract both sets of installation files to `C:/JFrog` on `az-lrdp-dat01`.  
5. From Services set the Artifactory service startup type to '**Manual**'.  
6. Restart `az-lrdp-dat01` (you may need IT Services to do this).  
7. Rename existing `C:/JFrog/artifactory/app` to `C:/JFrog/artifactory/app.old`.  
	(ignore JFrog's guidance to place them in `var/bootstrap/...`).  
8. Move existing `/app` from newly extracted files to `C:/JFrog/artifactory/`.  
9. Copy all *.jar files from `../enu/jar` within SQL Driver files to `C:/JFrog/artifactory/app/artifactory/tomcat/lib`.  
	(ignore JFrog's guidance to place them in `var/bootstrap/...`).  
10. From Services set the Artifactory service startup type back to '**Automatic**'.  
11. Restart `az-lrdp-dat01` (you may need IT Services to do this).  
12. Wait a few minutes for the service to resume once the server has restarted.  
13. If everything works as expected, tidy up and delete the remaining extracted installation files and the .old directory.  

## Fresh reinstall prep

1. Stop Artifactory service
2. Set service to manual run
3. Restart DAT01
4. Make a copy of:
	- `system.yaml` from `C:/JFrog/artifactory/var/etc`
	- `binarystore.xml` from `C:/JFrog/artifactory/var/etc/artifactory`
5. Delete directory `C:/JFrog/artifactory`
6. Rename (or delete) `/filestore` from `\\azlrdpartifactory/artifactory/binaries` file share
7. Drop all database constraints, tables and sequences

## Fresh reinstall 

1. Extract installation files to `C:/JFrog`
2. Rename unzipped folder to `artifactory`  
	```
    C:  
    |_ /JFrog  
        |_ /artifactory  
			|_ /app  
			|_ /var  
    ```
3. Get [JDBC SQL Drivers from Microsoft](https://learn.microsoft.com/en-us/sql/connect/jdbc/download-microsoft-jdbc-driver-for-sql-server)
	- extract and copy \*.jar files to `C:/JFrog/artifactory/app/artifactory/tomcat/lib`
4. Copy `system.yaml` to `C:/JFrog/artifactory/var/etc`
5. Copy `binarystore.xml` to `C:/JFrog/artifactory/var/etc/artifactory`
6. Set service to automatic and confirm log on as `zz_artifactory_src` (password in KeePass)
7. Restart DAT01

## Check:
- `console.log` for yaml validation
- `artifactory-service.log` for service log
- run `curl localhost:8082/router/api/v1/system/health` from cmd

If running a fresh install you will need to log in to the web front end (from within LASER) as admin (using default password) and configure it for use as per [Artifactory Configuration](artifactory_configuration.md), remembering to **change the default password**.  
