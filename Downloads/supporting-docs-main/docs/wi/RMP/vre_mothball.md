---
layout: default
title: VRE Mothball
parent: RMP
has_children: false
---

# VRE Mothball

To mothball a VRE, first ensure the project PI understands the consequences of mothballing and has given their approval. They must understand that, once mothballed, their project data will be inaccessible for a minimum of six months and that regaining access to their project data will require extra funding unless they've already budgeted for it.

Once you have PI approval, submit a VRE mothball request in ServiceNow. Do this by opening the [LASER request catalogue](https://it.leeds.ac.uk/it?id=sc_category&sys_id=be3bfcb0db3a18d0cd2a449e3b96195c) and selecting a Data Archive/Restore request.

Fill in the project details in the request form.

For "Data archive, Archive restore or Delete partial archive?", select "VRE Data Archive". In the question that appears after your selection, select "VRE Mothball Archive (All Data)".

Provide extra information to IT if needed by writing in the text box.

Check the box to confirm the request has been authorised by the PI, then submit the request.

Once the request has been fulfilled, you can check the VRE contents by finding the resource group in Azure Portal. A mothballed VRE should contain only one resource: A storage account that holds an archive-tier blob container.

Let the project team know that the mothballing process is complete and remind them the planned end date of the mothball period.
