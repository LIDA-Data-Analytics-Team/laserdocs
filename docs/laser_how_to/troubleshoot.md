---
layout: default
title: Troubleshooting
parent: LASER How To
nav_order: 999
---

# Troubleshooting
{:.no_toc}

Here are the answers to some common issues. If you have a problem not covered here please get in touch with the Data Analytics Team at [dat@leeds.ac.uk](mailto:dat@leeds.ac.uk).

* seed list
{:toc}

## My desktop won't start

![cannot_start_desktop.png](../../images/troubleshoot/cannot_start_desktop.png)

If you see the error message "Cannot start desktop" then chances are good that another member of your team is currently logged in to that specific virtual machine. Try another VM if there is one available within the VRE, or check that no-one else is currently logged in.

A VM will remain 'occupied' even if the user has disconnected. 

Simply closing the window ('Xing out') will disconnect the user from the session. When disconnected the session remains active and running; users will need to log off or shut down to vacate the machine so that someone else can log on.

![error_1030.png](../../images/troubleshoot/error_1030.png)

If you see the error message "The connection failed with status (1030)" then you will need to update the Citrix client on your device to the latest version of Citrix Workspace. IT Services will be able to assist in this if you do not have the necessary permissions on your device.

## LASER login failure: You cannot log on using a smart card

If you try to login to LASER after having timed out from a previous session, you may see the following message:

![cannot_connect_using_smart_card.png](../../images/troubleshoot/cannot_connect_using_smart_card.png)

You can fix this by clearing browsing data up to and including the time since your last LASER login. Alternatively, avoid the error by opening a private/incognito window instead.

## Access LASER VRE on Linux machine

The steps below have been tested using Ubuntu OS and Firefox browser.

- Ensure versions of Ubuntu, Firefox and Citrix Workspace are up to date
- If you don't have Citrix Workspace:
    - Open the Citrix Workspace for Linux [download page](https://www.citrix.com/en-gb/downloads/workspace-app/linux/) and go to the latest version
    - Scroll to Available Downloads > Debian Packages > Full Packages (Self-Service Support) > Citrix Workspace app for Linux (x86_64)
    - Download and run the .deb file (if you're not running Ubuntu, you may need a different file)
- Go to https://laser.leeds.ac.uk and login.
- Select Detect Receiver
- Check box to always open receiver links:<br>
![allow_open_receiver_link.PNG](../../images/troubleshoot/linux_login/allow_open_receiver_link.PNG){:width="70%" .mx-auto}
- Select Already installed
- Open VRE from Storefront. It will download an ica file.
- In dialog box on what to do with ica file, tell Firefox to always open with Citrix Workspace. Select OK:<br>
![use_citrix_to_open_ica.PNG](../../images/troubleshoot/linux_login/use_citrix_to_open_ica.PNG){:width="70%" .mx-auto}
- The VRE will then open. In future, your browser will know to automatically open the VRE when an .ica gets downloaded.
- If you get an SSL Error 61 preventing you from opening your VRE:
    - Open Terminal
    - Run `sudo ln -s /usr/share/ca-certificates/mozilla/* /opt/Citrix/ICAClient/keystore/cacerts`
    - Type your password to authenticate (note that this requires admin rights)
    - Close Terminal window then retry LASER VRE login

## Anaconda Navigator slow (in online mode)

When you first open Anaconda Navigator in a VRE, it will take some time to load. This is because the VRE is an offline environment and Anaconda Navigator expects an internet connection. You can improve your user experience of Navigator in the VRE by enabling offline mode.

After loading Anaconda Navigator, go to File > Preferences (shortcut CTRL+P).

Check the box to "Enable offline mode", then select Apply and close the preferences pane.

![Fifth option from the top on the Preferences screen, checkbox](../../images/troubleshoot/anaconda_navigator.png){:width="70%" .mx-auto}

You should now see "_Working in offline mode_" appear in the top right. Offline mode should persist when you open Anaconda Navigator again.

## I cannot see R: drive

You may need to manually map the R: drive to your machine.
- Open File Explorer and right click on Network  
	![network_context_menu.png](../../images/troubleshoot/network_context_menu.png)
- Select 'Map network drive'
- Drive = R: 
- Folder = \\\azlrdprepos.file.core.windows.net\r-repo
	![map_r_drive.png](../../images/troubleshoot/map_r_drive.png)
- Click finish 

You should now see the R miniCRAN repository mapped to R: drive.

