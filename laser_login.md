---
layout: default
title: Connect to LASER
nav_order: 2
video_src: "https://mymedia.leeds.ac.uk/Mediasite/Play/5072d91156ae4736bebcef7adbf4b6861d"
video_description: Logging into your LASER VRE
---

## How to connect to a Virtual Research Environment

<div class="t60">
    <div class="medium-4 columns">
        <iframe src="{{ video_src }}" width="100%" height="300" frameborder="0" marginwidth="0" marginheight="0" scrolling="auto" allowfullscreen="allowfullscreen" style="display:block;">
        </iframe>
        <p> 
            {{ video_description }}
        </p>
    </div>
</div>

### Prerequisites
You will need:
- Citrix Workspace installed to the machine you are connecting to LASER from.
  - Citrix Workspace is available through Software Centre on UoL managed devices.
- Duo two factor authentication enabled.
  - More infomation on DUO can be found [here](https://it.leeds.ac.uk/it/info/101/about_help_desk/142/privacy_notice?id=kb_article&sysparm_article=KB0014642).

### Log in to the Storefront
- Navigate to the StoreFront here: [https://laser.leeds.ac.uk/](https://laser.leeds.ac.uk/).
- Sign in using your University of Leeds credentials.
- When prompted, choose an authentication method and accept the login request/enter the passcode.  
![duo_auth_prompt.png](./images/duo_auth_prompt.png)
- You may be asked if Citrix Receiver is installed:
  - Click to detect installation.
  - Allow browser to 'Open Citrix Workspace Launcher'.
  - If not detected but installation is present click 'Already installed'.
- You are now presented with all of the VRE desktops you have access to.
- Click on the image of the monitor or expand the options and click 'Open' to connect.  
![citrix_store_front.png](./images/citrix_store_front.png)
  - You may be asked to download a *.ica launcher file.  
  ![citrix_launch_file.png](./images/citrix_launch_file.png)
  - Save and open this file, it will be deleted when your session ends.
- Citrix Workspace will launch and connect to your chosen VRE desktop.  
![vre_desktop.png](./images/vre_desktop.png)
