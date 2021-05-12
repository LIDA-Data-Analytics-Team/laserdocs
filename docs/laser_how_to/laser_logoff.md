---
layout: default
title: Closing a VRE
parent: LASER How To
nav_order: 1.1
---

## Closing a Virtual Research Environment  
There are three ways to close a VRE and each has significant differences regarding cost and continual processing:
- Sign out
- Shutdown
- Disconnect

The below table summarises the main differences, but the most significant is that **costs continue to accrue when shut down or disconnected** but not when signed out. 

We recommend signing out whenever you finish a session. Disconnecting from a session should _only_ be used if you need to walk away from the session but still want code to run while you are away. A disconnected session will continue to accrue costs even if code has completed running.

|Sign out |Shutdown |Disconnect |
|---|---|---|
|Stops accruing costs after 1 minute|Stops accruing costs after 1 minute|Costs continue to accrue |
|Terminates session|Terminates session|Keeps session running |
|Processes stop|Processes stop|Processes can continue |
|Other users can now log in to this VM|Other users can now log in to this VM|No other users can log in to this VM |

### How to Log off 
Click Start button --> Profile --> Sign out  

![](../../images/laser_logoff/vre_user_options.PNG)

### How to Shutdown
Click the big red icon on the desktop and choose yes on the dialog:  

![](../../images/laser_logoff/vre_brb_shutdown.PNG)  

![](../../images/laser_logoff/vre_brb_shutdown_dialog.PNG)  

### How to Disconnect
You can disconnect two ways, but only should if you want code to continue to run in your absence. **Costs will continue to accrue** and VM will be locked for use by other users **until you reconnect then sign out or shutdown**.  
	
- Expand the Citrix menu at the top of the screen --> Disconnect  

	![](../../images/laser_logoff/vre_citrix_options.PNG)
	
- X-ing out of the VRE window  

	![](../../images/laser_logoff/vre_x.PNG)
