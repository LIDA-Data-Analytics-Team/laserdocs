---
layout: default
title: P0011 CDRC
parent: Project Work Instruction
has_children: false
---

# CDRC VRE File Transfer

**CDRC VRE** receives files from multiple sources. While the primary file transfer method is through Biscom SFT, some data providers prefer to use their own file transfer methods, for instance Mastercard.

## Mastercard
Occasionally Mastercard will send details of file(s) ready for import into LASER. The email comes in a machine generated format from an address like `DW_TES_File_Transfer@mastercard.com` and contains information on Delivery Controls, Files Delivered, plus the Host Name, Port, Directory & Userid.

There isn't much other information in this email or how to access it. If you haven't done this before you won't have the encryption credentials established with Mastercard to implement the transfer. 

It requires you to follow these steps: 
1. Generate a SSH key pair on DAT02 (as detailed below). 
2. Reply to the Mastercard email address with the **public** part of that key attached, asking them to register your key in their system. (You'll need to transfer that part out of the DAT02 to your local machine.)
3. Await a reply from Mastercard to confirm that they have added/registered your key for encryption.
4. Secure-copy the files from Mastercard server to DAT02 using the `scp` command in BASH (or use FileZilla if preferred). An example of this is as follows: 
```bash
scp -P 22022 leedsunivUK@files.mastercard.com:/geoinsights/data/fromMC/Geogrids_University_of_Leeds_postcode_sector_20240201_20240229_final.csv.gz .
```

You will need to **modify the path and filename** based on the name and location of the new files.
The `.` at the end will copy the file to the current directory. `-P` determines the port.

### Steps to Generate SSH Key with Git Bash

1. Open Git Bash, in your local machine or in DAT02

2. Enter the following command and hit `Enter`:

    ```bash
    ssh-keygen -t rsa -b 4096
    ```

    This command generates a new RSA SSH key pair with a length of 4096 bits.

3. When prompted to "Enter file in which to save the key", hit `Enter` to accept the default file location (`/c/Users/<Username>/.ssh/id_rsa`).

4. At the prompt to "Enter passphrase (empty for no passphrase)", hit `Enter` to proceed without a passphrase.

5. When asked to re-enter the passphrase for confirmation, do so and press `Enter`.

### Post-key Generation Steps

1. Copy the generated files (`id_rsa` and `id_rsa.pub`) from `/c/Users/<Username>/.ssh/id_rsa` to a new folder in the project's incoming staging area in DAT02, `I/P0011/ssh_key`.

2. Share the `id_rsa.pub` with the Mastercard team.

*Note: Remember to replace `<Username>` with your actual username.*
