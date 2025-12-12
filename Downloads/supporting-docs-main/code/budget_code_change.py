# https://learn.microsoft.com/en-us/azure/azure-resource-manager/management/tag-resources-python

from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.resource.resources.models import TagsPatchResource

def change_BudgetCode_AllResources(subscription_id, resource_group_name, budget_code):
    credential = AzureCliCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)

    tags = {
        "budgetcode": budget_code,
        }

    tag_patch_resource = TagsPatchResource(
        operation="Merge",
        properties={'tags': tags}
    )

    # Resource Group 
    resource_group = resource_client.resource_groups.get(resource_group_name)
    resource_client.tags.begin_update_at_scope(resource_group.id, tag_patch_resource)
    print(f"Tags {tag_patch_resource.properties.tags} were added to existing tags on resource group: {resource_group.id}")

    # Resources within Resource Group
    resources = resource_client.resources.list_by_resource_group(resource_group_name)
    for resource in resources:
        resource_client.tags.begin_update_at_scope(resource.id, tag_patch_resource)
        print(f"Tags {tag_patch_resource.properties.tags} were added to resource: {resource.id}")


def change_BudgetCode_NamedResources(subscription_id, resource_group_name, resource_list, budget_code):
    credential = AzureCliCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)

    tags = {
        "budgetcode": budget_code,
        }

    tag_patch_resource = TagsPatchResource(
        operation="Merge",
        properties={'tags': tags}
    )

    for resource_name in resource_list:
        resources = resource_client.resources.list_by_resource_group(resource_group_name, filter=f"name eq '{resource_name}'")
        for resource in resources:
            resource_client.tags.begin_update_at_scope(resource.id, tag_patch_resource)
            print(f"Tags {tag_patch_resource.properties.tags} were added to resource: {resource.id}")

