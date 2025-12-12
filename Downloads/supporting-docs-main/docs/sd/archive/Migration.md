---
nav_exclude: true
---
# Migration to LASER

## From IRC

- Comment on Migration ticket to schedule a day for migration with Servers Team
- On Migration Day Servers drop VRE into maintenance mode
- DAT log in to IRC Gate
- Navigate to N: shared project storage on IRC (\\<V00xx>-file01)
- Run MD5 on N:  
  - Copy 'List files and hash check - Source and Destination.xlsm' from \\irc-vm0097\IRC Tools
  - Paste into root of N:
  - Open 
- Log in to Azure Storage Explorer
- Navigate to LASER project storage
- Drag contents of N: in to blob container
- Wait for transfer
- Run MD5 again
- Make VRE visual checks:
  - Drives mapped?
  - Data visible?
  - Internet locked out?
