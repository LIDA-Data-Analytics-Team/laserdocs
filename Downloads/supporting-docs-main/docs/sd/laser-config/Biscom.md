---
layout: default
title: Biscom
parent: LASER Configurables
has_children: false
---

# How to support LASER Biscom SFT

## Licence renewals

- Speak to Server team to make sure they know
- Email sales@biscom.com to request licence renewal for account called "Leeds Institute for Data Analytics – Laser", copying in Server team representative
- When we receive a quote, pass on the LIDA office manager (Kim Wright) to purchase
- Server team should deal with any work required to activate the new licence

## Patching and issues

- For resolving issues or patching vulnerabilities, email support@biscom.com and copy in a Server team representative
- Server team should be able to provide Biscom with any details they need about versions of software or the SFT application server
- Server team will deploy any patches to the application and/or server

## User password resets

- Usually users can reset their own password by requesting a reset email, but if this isn't possible for whatever reason we can reset it for them
- Log into Biscom with an account that has User Admin rights
- Go to Administration menu > Manage Users > Select the user needing a password reset
- Select password reset option
- Create new password and check box to require user to change password at first sign-in
- Select Update
- Provide new one-time password to user

## Biscom admin

- Biscom admin credentials stored in KeePass SFT folder, "LASER Biscom - admin" entry
- This account has Super User rights and Compliance Editor rights (added 2022-04-11), with the ability to:
    - edit/delete packages and deliveries
    - edit server configuration, such as default expiry times
- Change default delivery expiry time in Administration > Server Configuration > Delivery Settings
    - Default was 90 days. Reduced to 30 days on 2022-04-11.
- Change default package expiry time in Administration > Server Configuration > Package Settings
    - Default is 365 days. We should consider reducing this to 30 days as well, after better understanding the implications.

## Create permanent Biscom link

- As DAT account:
    - Go to Packages from the left menu, then select 'Create package' from the Action dropdown.
    - Give the package a name and create it.
- As admin account:
    - Go to Packages from the left menu, then edit the created package and remove the auto-delete date.
- As DAT account:
    - Go to the package again and select 'Send delivery' from the Action dropdown.
    - On the delivery page, delete the expiry date from the 'Date expires' field.
    - Send the Biscom message as usual by entering the recipient, subject, and secure message, then click Send.
