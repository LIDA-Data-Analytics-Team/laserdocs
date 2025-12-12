---
layout: default
title: TRE Testing Checklist After Build
parent: RMP
has_children: false
---

## TRE Testing Checklist: After Build

Once a TRE build is completed and ready to be handed over to the project team, perform the following checks:

### Basic Functionality

Log in to the TRE and verify:

- All drives (e.g., N Drive, R Drive) are mapped correctly.
- **Software Centre** opens and displays available software as expected.
  - If applications are missing, try forcing an SCCM update:
    - Go to **Control Panel** → **Configuration Manager** → **Actions** tab.
    - Run the following actions:
      - *Application Deployment Evaluation Cycle*
      - *Machine Policy Retrieval & Evaluation Cycle*
- You can access Artifactory on the browser (http://artifactory:8082).
- Log off from the VM using the red button and confirm via the Azure portal that the VM deallocates after 10 minutes.

### Final Steps

- If all tests pass, update the **Prism record** to `'Active'`.
- If any issues are found:
  - Reopen the existing **ServiceNow request ticket**, or
  - Raise a new **incident request** on ServiceNow to report the issue.
