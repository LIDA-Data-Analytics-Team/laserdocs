---
layout: default
title: Closing a VRE
parent: LASER How To
nav_order: 1.1
---

## Closing a Virtual Research Environment  
There are three ways to close a VRE and each has significant differences regarding cost and continual processing:
- Log off
- Shut down
- Disconnect

The below table summarises the main differences, but the most significant is that **costs continue to accrue when disconnected** but not when logged off or if the VM is shut down. 

We recommend logging off or shutting down whenever you finish a session. Disconnecting from a session should **only** be used if you need to walk away from the session but still want code to run while you are away. A disconnected session will continue to accrue costs even if code has completed running.

|Log off |Shut down |Disconnect |
|---|---|---|
|Stops accruing costs after 20 minutes|Stops accruing costs immediately|Costs continue to accrue|
|Terminates session|Terminates session|Keeps session running|
|Processes stop|Processes stop|Processes can continue|
|Other users can now log in to this VM|Other users can now log in to this VM|No other users can log in to this VM|

### How to Log off 
Click Start button --> Profile --> Sign out  

![](../../images/laser_logoff/vre_user_options.PNG)

### How to Shut down
Click Start button --> Power --> Shut down  

![](../../images/laser_logoff/vre_power_options_shutdown.PNG)

### How to Disconnect
You can disconnect several ways: 
- Start button --> Power --> Disconnect  

	![](../../images/laser_logoff/vre_power_options_disconnect.PNG)
	
- Expand the Citrix menu at the top of the screen --> Disconnect  

	![](../../images/laser_logoff/vre_citrix_options.PNG)
	
- X-ing out of the VRE window  

	![](../../images/laser_logoff/vre_x.PNG)
