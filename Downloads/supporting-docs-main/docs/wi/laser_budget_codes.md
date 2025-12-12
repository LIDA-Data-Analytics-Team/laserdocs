---
layout: default
title: Budget Codes
parent: Work Instruction
has_children: false
---
# LASER Budget Codes  

Costs in LASER are managed and allocated to projects through the use of tags.  

Each and every Resource in the LASER subscription has a tag named "budgetcode" with a value equal to the University account code that costs accrued by that resource are to be charged against.  

On occasion it may be necessary to correct, amend or change the 'budgetcode' tags, for example if the funding of a project changes or if additional resources are added to a VRE that need to be charged against a different account. Sometimes resources are created and budgetcode tags are changed in error, so need to be fixed.  

> All changes must be recorded to the project record in Prism.  
> The PI (and budget holder if different) must also be informed of the changes, with the LIDA Finance Manager (Gareth Bancroft) cc'd.  

These tag value changes can be made manually from Azure Portal or programmatically using Azure REST API.  

> When changing the budgetcode tags for a Resource ensure that all associated Resources also have their tags changed. For example, if changing the budget code for a Virtual Machine named '**lzw-p0999v01-01**' you would also need to change the tag value for the Network Interface and the Disk. These associated resources will contain the primary resource in their name; e.g.:  
> - **lzw-p0999v01-01**-nic  
> - **lzw-p0999v01-01**_disk1_eb84776b5b0a4d69aad18bb3cad4f3a6  

## Manually change Budget Codes  
1. From [Azure Portal](https://portal.azure.com/#home) navigate to the resource that requires change  
2. Select the 'Tags' blade from the menu on the left  
3. Locate the tag named 'budgetcode'  
4. Change the value  
5. Click 'Apply'  
6. Repeat for each Resource that requires change  

It's important that no changes to Tag Names are made or any of the other Tag Values.  

## Python SDK to change Budget Codes
There's a Python script ([budget_code_change.py](../../code/budget_code_change.py)) in this repo with a couple of functions that can change 'budgetcode' tags for an entire resource group or for listed named resources within a resource group.  

It was adapted from [here](https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-python). 

To use the script you'll need an environment with the following Python packages installed:
- azure-identity
- azure-mgmt-resource

You'll also need [Azure CLI](https://learn.microsoft.com/en-us/cli/azure/install-azure-cli) installed locally and to be logged in to Azure using `az login`. 

Before running the code to affect changes to tag values on VMs you **may** need to ensure that the VMs are running first. The script has been known to error when VMs aren't in a running state, though not recently.  
Remember to stop the VMs once the changes are complete!  

> Save copies of the files that are used to run the below code into the Project folder on Teams, with a file name of '_Pxxxx Budget Code Change YYYY-MM-DD.py_'.  

### Full Resource Group & All Resources  
Using the function defined in the above python script:  
```python
from budget_code_change import change_BudgetCode_AllResources

subscription_id = <LASER Subscription ID>
resource_group_name = <Resource Group Name to change>
budget_code = <New Budget Code to change to>

change_BudgetCode_AllResources(subscription_id, resource_group_name, budget_code)
```

### List of Named Resources  
Using the function defined in the above python script:  
```python
from budget_code_change import change_BudgetCode_NamedResources

subscription_id = <LASER Subscription ID>
resource_group_name = <Resource Group Name to change>
budget_code = <New Budget Code to change to>
resource_list = [
    <1st resource name>
    , <2nd resource name>
    , <...>
    , <nth resource name>
    ]

change_BudgetCode_NamedResources(subscription_id, resource_group_name, resource_list, budget_code)
```
