<!--{::options parse_block_html="true" /}-->
# Data Transfer App 

The Mermaid charts below can be viewed in [Markdown in repo](https://gitlab.com/lida-data-analytics-team/supporting-docs/-/blob/master/docs/sd/dta.md).

[Import Data Flow](#import-data-flow)  
[Export Data Flow](#export-data-flow)  
[Database Schema](#database-schema)  



## Import Data Flow

<!--![Data Transfer App](../../images/Import_Data_Flow.jpg)-->   

```mermaid
flowchart TB
	subgraph Key
        requestor(Requestor<br>action)
	    reviewer(Reviewer<br>action)
	end
	
	create_job --> |Files moved by DTA| review_store
    import[[Import]] --> |Biscom/OneDrive/STFP etc.| import_store
	
    import_store -.- is_path{{"\\azlrdpDataImport.file.core.windows.net\Staging\Project\[user]\Downloads"}}
	review_store -.- rs_path{{"\\azlrdp[VRE #].file.core.windows.net\Staging\[Job #]"}}
	project_store -.- ps_path{{"\\azlrdp[VRE #].file.core.windows.net\Project\[Job #]"}}
	
    subgraph DTIS [Data Transfer Import Server]
        import_store[(Data Transfer <br> Import Storage)]
        import_store --> create_job(Create New <br> Import Request <br> in DTA)
	end

	subgraph VRE
        review_store[(VRE Import <br> Review Storage)]
        review_store --> review(Review Files)
        review --> approve_reject(Approve / Reject <br> in DTA)
        approve_reject --> |Files moved by DTA| project_store[(VRE Project <br> Storage)]
	end

	style requestor fill:Gold
	style reviewer fill:lightgreen
	style import_store fill:LightSkyBlue
	style review_store fill:LightSkyBlue
	style project_store fill:LightSkyBlue
	style create_job fill:Gold
	style review fill:lightgreen
	style approve_reject fill:lightgreen
```


## Export Data Flow

<!--![Data Transfer App](../../images/Import_Data_Flow.jpg)-->   

```mermaid
flowchart TB
	subgraph Key
        requestor(Requestor<br>action)
	    reviewer(Reviewer<br>action)
	end
	
    export_store --> |Biscom/OneDrive/STFP etc.| export[[Export]] 
    approve_reject --> |Files moved by DTA| export_store
   
    export_store -.- es_path{{"\\azlrdpDataExport.file.core.windows.net\ExportApproved\[VRE #]\[Job #]"}}
    export_review_store -.- rvew_path{{"\\azlrdp[VRE #].file.core.windows.net\ExportReview\[Job #]"}}
    export_request_store -.- rqst_path{{"\\azlrdp[VRE #].file.core.windows.net\Export"}}
    project_store -.- ps_path{{"\\azlrdp[VRE #].file.core.windows.net\Project"}}

    subgraph VRE
        project_store[(VRE Project <br> Storage)]
        project_store --> |Requestor creates files in Export Request Storage| export_request_store
        export_request_store[(Export Request <br> Storage)] --> create_job(Create New <br> Export Request <br> in DTA)
        create_job --> |Files copied by DTA| export_review_store[(Export Review <br> Storage)]
        export_review_store --> review(Review Files) 
        review --> approve_reject(Approve / Reject <br> files in DTA)
    end

    subgraph DTES [Data Transfer Export Server]
        export_store[(Data Transfer <br> Export Storage)]
    end
	
    style requestor fill:Gold
	style reviewer fill:lightgreen
    style export_store fill:LightSkyBlue 
    style export_review_store fill:LightSkyBlue 
    style export_request_store fill:LightSkyBlue 
    style project_store fill:LightSkyBlue
    style export fill:LightSkyBlue
    style create_job fill:gold
    style review fill:lightgreen
    style approve_reject fill:lightgreen
```


## Database Schema

All tables populated by VRE build scripts or Data Transfer App, **except** for dbo.DataOwner and dbo.DSA. These tables must be populated by DAT.

### Asset Register
- List of assets that have been added
- Relates to AssetDSA

### AssetDSA	
- links AssetRegister with DSA
- likey decommed in future

### DSA
- AmendOf not used by App

### DataOwner
- RebrandOf not used by App	

### DataIORequest
- Lists all request jobs
- Request TypeID links to RequestType
- RequestedBy is GUID, linked to AAD
- RequestedReviewer 
	- All Reviewer = GUID of AAD group
- ReviewedBy is GUID of person who completed request

### FileRegister
- RequestID links to DataIORequest

### FileAuditLog
- File movements are stored here
- Links to FileRegister

### Project
- No impact other than ProjectCode must be same as in ActiveDirectory
- AD Groups are at VRE level, populated by build script using mid(string)

### VRE
- Storage account cannot be accessed without StorageAccountKey
	- Key Vault set up for each application resource group
- fileshare names must match names of fileshares in Azure
	
<summary markdown="span">

	
	
