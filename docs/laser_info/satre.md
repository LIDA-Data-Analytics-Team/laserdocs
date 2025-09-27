---
layout: default
title: SATRE Self Assessment
parent: LASER Info
nav_order: 7
---

# SATRE Self Assessment
{:.no_toc}

<details markdown="block">
  <summary>
    Table of contents
  </summary>
  {: .text-delta }

* seed list
{:toc}
</details>  


The [Standard Architecture for Trusted Research Environments (SATRE)](https://satre-specification.readthedocs.io/en/stable/index.html) project provides a Standard Architecture for Trusted Research Environments (TREs). It incorporates knowledge and best practices from multiple institutions and sectors across the UK. This includes all aspects of TRE provision such as information governance procedures, computing technology, data management and other capabilities.  

It aims to standardise the capabilities of TREs, making it easier for users, operators, and developers to work with sensitive data, and making the operation of TREs more transparent to data owners and the general public.  

Below is LIDA's self assessment of LASER against the SATRE standard.  

{: .note-title }
> Scoring
>
> TREs are scored against each statement in the SATRE specification using this scoring system:
> 
> |Score|Meaning        |Description|
> |:-:  |---            |---        |
> |0    |Not met        |The TRE does not meet this requirement (if this is Mandatory this means the TRE is not SATRE compliant)|
|1    |Sufficient     |The TRE meets this requirement, but there is substantial scope for improvement|
|2    |Satisfied      |The TRE meets this requirement, but there may still be scope for improvement|
> |N/A  |Not applicable |The statement is not relevant to a TRE, may apply to Recommended or Optional statements, and a very limited number of Mandatory* statements|
> 
> A score of 1 or above means you have met the requirement. Optionally you can use 1 and 2 to indicate potential areas of improvement in your TRE.

## Summary  

Combined scores for each Pillar:

||Computing technology and Information Security|Data management|Information governance|Supporting Capabilities|
|---|:-:|:-:|:-:|:-:|
|**Combined score**|104/122|64/66|75/82|36/38|
|**Capabilities met?**|Yes|Yes|Yes|Yes|


Count of LASER scores for each component by Importance:  

|Score  |Mandatory  |Recommended    |Optional   |
|:-:    |:-:        |:-:            |:-:        |
|0      |0          |4              |3          |
|1      |3          |9              |3          |
|2      |74         |45             |13         |
|N/A    |2          |2              |2          |

## 1. Information Governance  
### 1.1. Governance Requirements  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**1.1.1.** You must gather and monitor the information governance requirements needed to fulfil any legal, regulatory and ethical standards.<br><br>Requirements will come from a variety of sources including legislation, contractual obligations and ethical standards.<br>Requirements must be monitored to ensure the TRE controls remain appropriate.|Mandatory|2|ISO27001:2022 15331-ISMS- 001 |
|**1.1.2.** You must ensure controls are implemented to ensure the requirements are met.<br><br>Control implementation should be systematic and directly aligned to the internal and stakeholder requirements.|Mandatory|2|ISO27001:2022 15331-ISMS- 001 |
|**1.1.3.** You must ensure there are adequate resources to meet information governance requirements.<br><br>Ensuring information governance controls are suitable and enforced requires an investment of funding and people appropriate to the size of the TRE.|Mandatory|2|Information Governance Manager , DAT team, support from IT |

### 1.2. Quality Management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**1.2.1.** You must ensure that changes to policies and standard operating procedures can only be made by trusted individuals.<br><br>It is important to ensure that policies and SOPs are relevant, up-to-date and carefully controlled to maintain the integrity and security of your TRE organisation.|Mandatory|2||
|**1.2.2.** You must use versioning and a codified change procedure for all policies and standard operating procedures.<br><br>This includes recording dates of changes, person responsible for carrying out changes, and summary of changes.|Mandatory|2|Version control on all documentation|
|**1.2.3.** You should measure the performance of information governance within the TRE with regular reporting available to your TRE organisation’s management team.<br><br>This may include reports and dashboards showing security incidents, quality management deviations and audit findings.|Recommended|2|Regular updates to Information Governance Management Group ( IGMG)  which includes LIDA Senior manager rep, CISO , GRC lead, DPO , IG manager and others |
|**1.2.4.** You must audit your TRE organisation against relevant requirements and standards.<br><br>If you are publicly accredited against a standard, for instance ISO27001, DSPT, CE+ *etc.*, you must have processes in place to ensure you remain compliant.|Mandatory|2|ISO27001:2022 15331-ISMS- 001 |
|**1.2.5.** You must report on and share outcomes of each audit of your TRE organisation with the required bodies.<br><br>This may include regulatory bodies or the organisations that manage accreditations you have.|Mandatory|2|External audit team can access any internal audit on request.  Internal and external audit results are reported to Information Governance Management Group ( IGMG)  , with escalation to University Audit and Risk  Committee as required. |
|**1.2.6.** You must ensure that suppliers, contractors and sub-contractors with access to your TRE align with your security requirements.<br><br>These should be included as mandatory, non-functional requirements in during procurement and contracting.<br>This will also include contractor staff contracts for example, legal liability and NDAs.|Mandatory|2|Managed according to University procedures|
|**1.2.7.** You must monitor compliance of your suppliers with the terms of the contracts.<br><br>This will include monitoring changes in the services and infrastructure being delivered and quality management within the contractor’s organisation.<br>This may be done through formal audit or by monitoring change and quality documentation provided by the supplier.|Mandatory|1|All suppliers are managed through University processes|
|**1.2.8.** You must track and maintain any physical assets used by your TRE.<br><br>All physical assets should be maintained and covered by warranty if applicable.<br>At the end of their lifetime, assets should be securely disposed of in such a way that data cannot be recovered from them.|Mandatory (where physical assets are in scope)|2|No physical assets, client devices not in scope|
|**1.2.9.** You must log, track and resolve any issues resulting from deviations from processes, incidents and audit findings.<br><br>This process could, for example, be tracked through an electronic record and workflow system with records retained.|Mandatory|2|Reported to IGMG |
|**1.2.10.** You must use reported issues to inform changes, such as for process improvement and risk management.<br><br>All issues should be analysed for their root cause and improvements put in place to prevent further occurrence.|Mandatory|2|Risk Management plan reported to Information Governance Management Group ( IGMG)  |
|**1.2.11.** You should collect and maintain quality management data for measuring the effectiveness of a TRE.<br><br>Large amounts of data will be produced by elements within the TRE.<br>These data should be analysed with reports and dashboards provided to guide TRE implementer’s improvements and provide re-assurance to data consumers and data subjects.|Recommended|2|Management data is available to affected parties via PRISM tool|
|**1.2.12.** You could use a QMS (Quality Management System) to standardise and automate quality management tasks and workflows, and to generate quality data and reports automatically.<br><br>A basic QMS could be a set of spreadsheets or documents held in a repository which are manually maintained.<br>More mature applications will provide workflows and generate quality data through manual and automated actions.|Optional|1|QMS is maintained manually. |

### 1.3. Risk Management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**1.3.1.** You must have a way to score risk to understand the underlying severity.<br><br>You have a risk assessment methodology for scoring risks on multiple axes such as impact and likelihood.|Mandatory|2|Risk Management plan reported to IGMG|
|**1.3.2.** You must carry out a data processing assessment for all projects requiring a TRE.<br><br>A data processing assessment is a process designed to identify risks arising out of the processing of sensitive data and to minimise these risks as far and as early as possible.<br>This may take the form of an existing regulatory requirements such as Data Protection Impact Assessment.|Mandatory|2|Data Management plan required for all LASER Projects|
|**1.3.3.** You must have a process for designing, implementing and recording risk mitigations where indicated by a risk assessment.<br><br>Actions that are taken or not taken following a risk assessment must be recorded.|Mandatory|2|Risk Management plan reported to IGMG|
|**1.3.4.** You must have a clear set of roles and responsibilities relating to risk including who owns risks and how they are escalated and delegated.<br><br>The highest level of risk ownership is the Top Management of the TRE organisation (see Governance Roles).<br>In order to ensure escalations to this level are rare, suitable structures should be put in place to own, mitigate and accept risk.|Mandatory|2|Roles and responsibilities recorded within ISMS.  IGMG reports to Information Governance Organisation Group (University Executive Group level meeting) and Audit and Risk Committee (University Council level meeting with external  accountability) by way of escalation.  |
|**1.3.5.** You must understand the risk appetite of your TRE organisation.<br><br>This includes understanding ownership of risk, and ability to accept risk which falls outside of the appetite should that become necessary.|Mandatory|2||

### 1.4. Study Management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**1.4.1.** You must have checks in place to ensure a project has the legal, financial and ethical requirements in place for the duration of the project.<br><br>This includes checks that contracts are in place where required, adequate funding is available for the duration of the project, and responsibilities concerning data handling are understood by all parties.|Mandatory|2|RMP sets out expectations and expected costs|
|**1.4.2.** You must have checks in place to ensure that any time limited compliance requirements are maintained.<br><br>This includes ensuring contracts remain in valid and action is promptly taken should they expire.<br>Any changes in the status of responsible persons should also be monitored, for example a data owner leaving an organisation.|Mandatory|2|Prism tool records project validity.  HR policy removes leaver access to all IT systems , including LASER.  Staff movers who no longer require access to LASER are reported by the principle investigator (PI) and removed accordingly.  Access to the LIDA offices is regularly reviewed. |
|**1.4.3.** You must have checks in place to ensure that changes in regulations are met for a project.<br><br>|Mandatory|2|Annual Check as part of ISMS Review.|
|**1.4.4.** You must have standard processes in place for the end of a project, that follow all legal requirements and data security best practice.<br><br>This includes the archiving of quality and log data along with the archiving or deletion of data sets.|Mandatory|2|Destruction certificate and process|
|**1.4.5.** You could implement a portal that can provide a workflow engine and database which automates the processes within this capability.<br><br>A portal should automate as much of the processes within the capability as possible.<br>Where processes are automated, process maturity is easier to achieve, with more consistent completion and automatic production of quality control and monitoring data.|Optional|N/a||
|**1.4.6.** You must keep a complete record of all the data assets held within the system.<br><br>Details of all data assets (current and past) held by the system should be retained along with meta-data useful for ensuring compliance can be demonstrated.<br>This would include ownership, data lifecycle, contracts, risk assessments and other quality data.<br>This is likely to already exist within the wider organisation but may require augmenting for the TRE.|Mandatory|2|Asset register included on PRISM|
|**1.4.7.** You should keep a complete record of all the research studies and projects within the TRE current and past.<br><br>The study register should contain all data related to a study including a reference to data assets, project team members, information asset owners and any compliance activities required.|Recommended|2|Asset register included on PRISM|

### 1.5. Member Accreditation  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**1.5.1.** You must have a robust method for identifying accredited members of your TRE organisation, prior to their accessing of sensitive data.<br><br>This may include ID checks or email/phone verification.|Mandatory|2|All LASER users must have Leeds Employment status that gives system authentication and have completed Information Governance training.  |
|**1.5.2.** You must have clear onboarding processes in place for all roles within your TRE organisation.<br><br>This may include all members signing role-specific terms of use or confirming that they have completed role specific training.|Mandatory|2|All LASER users must complete LASER user Agreement  and Information Governance training |
|**1.5.3.** You must have a set of services to manage access to resources based on identity.<br><br>This will include a security model for role based access with technical controls to ensure the principle of least privilege is enforced.|Mandatory|2|All users are granted access to assets in LASER upon PI approval once they satisfy all other requirements (such as training). Access is granted on a principle of least privilege. |
|**1.5.4.** You must not give anyone access to datasets without agreement from the Data Controller.<br><br>The Data Controller may choose to delegate this authority.|Mandatory|2||
|**1.5.5.** You must have robust and secure applications in place to authenticate users (and services) within the TRE.<br><br>The number of authentication applications should be kept to a minimum with common controls and standards applied across all such as MFA, password complexity *etc.*.|Mandatory|2||
|**1.5.6.** You must give each user of the TRE a unique logon with changes to any records strictly controlled.<br><br>The unique identifier and all associated records for a user should be traceable across the entire TRE.<br>This will include training records, affiliations, contract agreements and ethics approvals where required.|Mandatory|2|All LASER users have a unique log on which is controlled by University Identity management |

### 1.6. Training Delivery and Management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**1.6.1.** You must determine what training is relevant for all roles within the TRE organisation.<br><br>This may include, for instance, cyber security training, GDPR training, and higher level training for system operators.<br>Specialised roles are likely to need more tailored training.<br>Identification of these specialties should be done through a systematic training needs analysis.<br>Specific training may also be required based on the data or information asset owner such as GCP.|Mandatory|2|All University staff , including LASER Users must complete information governance, H&S and equality training.  |
|**1.6.2.** You must ensure that relevant training is available for all roles within the TRE organisation.<br><br>All TRE organisation members need to complete all relevant training and keep their training current.<br>You may need to provide help or guidance to enable them to do so.<br>Details of what training is needed will have been determined above.|Mandatory|2|University mandatory training is repeated on a specified cycle, with access being removed for non-completion of information governance training.  |
|**1.6.3.** You must provide repeat or updated training where necessary to account for changes in competency requirements.<br><br>Training is not a one-off event.<br>Electronic reminders for refresher training should be considered.<br>Ideally, training should remain relevant and so policies and processes should enable people to demonstrate competency rather than unnecessarily repeating training.|Mandatory|2|University mandatory training is repeated on a specified cycle, with access being removed for non-completion of information governance training.  |
|**1.6.4.** You must maintain accurate training records that are directly tied to the role and access levels within the TRE.<br><br>Training records should be tied to a user record and carefully maintained.<br>Maintaining training records enables you to ensure all people have completed the required training and that repeat training happens regularly.|Mandatory|2|Training records are maintained LMS|
|**1.6.5.** You should accept proof of relevant training certifications from trusted third parties.<br><br>You might choose to trust certifications provided by known training providers or your institution’s partner organisations.|Recommended|0|All LASER users are have University contracts and are required to complete University mandated courses,|
|**1.6.6.** You could have a training platform capable of delivering online training in a variety of formats.<br><br>This could be a simple content delivery platform or a more comprehensive LMS platform.<br>It could also include a range of multimedia delivery formats, and accessible training modules for those with access requirements.|Optional|2|LMS and Online / Paper version available.  Other accessible version will be made available on request. |
|**1.6.7.** You could implement a learning management system (LMS) to manage courses and deliver training as required.<br><br>Where possible an LMS should support a variety of course content and testing.|Optional|2||
|**1.6.8.** You could ensure that any courses you use are available in standard, transferable formats.<br><br>Support for standard formats such as SCORM allows courses to be shared between providers.<br>This could help facilitate standardisation of training provision for TRE users across organisations.|Optional|1|Available but not used and would require investigation|
|**1.6.9.** You could keep historical copies of courses in order to demonstrate competency at a given point in time.<br><br>Information asset owners and regulators may be required to audit historical records, *e.g.* for clinical trials.<br>It may be necessary to retain copies of superseded training along with versions of certifications within the training record.|Optional|0||

## 2. Computing technology and Information Security  
### 2.1. End user computing  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**2.1.1.** You must not allow users to copy data out of your TRE via the system clipboard.<br><br>A TRE user must not be able to copy sensitive data out of a workspace using the system clipboard.<br>A TRE may allow user to paste text into a workspace.<br>This might not be relevant to your TRE, for example if your user interface does not have a clipboard.|Mandatory|2|No data can be egressed from LASER except by DAT through approved processes|
|**2.1.2.** Your TRE workspace should provide an environment familiar to your users.<br><br>This may take the form of a virtual Windows or Linux desktops, non-desktop interfaces such as JupyterLab and other web applications, or a terminal.<br>Bespoke TRE-specific software should be avoided when widely used alternatives already exist.|Recommended|2||
|**2.1.3.** A TRE could restrict data access from data consumers entirely and provide an interface for submitting code.<br><br>For example, you might use a system where users submit jobs that run over the data and return results without allowing direct data access.|Optional|0|LASER is data agnostic; all users have permission to access the data in their TRE|
|**2.1.4.** Your TRE should be accessed via a user interface accessible using commonly available applications.<br><br>TREs which allow users to connect from their own devices should not require the installation of any bespoke TRE application on the user’s device.<br>In practice a web browser is the most common way to achieve this.|Recommended|2||
|**2.1.5.** Your TRE must provide clear guidance on how to use software tools and work with data in the TRE.<br><br>TREs that provide a virtual desktop environment for data consumers to work in should provide documentation detailing the available tools.<br>TREs where the analysis code is developed on the access machine (as oppose to within the TRE) should provide documentation detailing the mechanism by which code is submitted to the TRE.|Mandatory|2|DAT team work with and in the project team to assist with these processes. |
|**2.1.6.** Your TRE should, where possible, automatically apply security related updates for user software.<br><br>Reducing the risk of exploitable vulnerabilities in installed software will increase the security of your TRE.|Recommended|0|Although not automated , vulnerabilities are monitored and manually updated |
|**2.1.7.** Your TRE could provide shared services that are accessible to users in the same project.<br><br>This may include shared file storage, databases, collaborative writing, and other web applications.<br>This must only be shared amongst users within the same project.|Optional|2|Each TRE is restricted to named users. |
|**2.1.8** Your TRE must ensure that any shared services are only available to users working on the same project.<br><br>Poorly designed shared services could enable the unintended mixing of data between projects.<br>To prevent this it is necessary that each instance is only shared between users of a single project.|Mandatory|2|Each TRE is restricted to named users. |
|**2.1.9.** You must mitigate and record any risks introduced by the use in your TRE of software that requires telemetry to function.<br><br>For example, some licenced commercial software must contact an external licensing server at start-up.<br>You must be confident that only licensing information is sent to this server and that any network connections are secure.|Mandatory|2|Secure by design and pen tested|
|**2.1.10.** Your TRE must provide software applications that are relevant to working with the data in the TRE.<br><br>The tools provided will depend on the types of data in the TRE, and the expectations of users of the TRE.<br>For users working in a TRE via a virtual desktop, this may include programming languages such as Python and R, integrated development environments, Jupyter notebooks, office type applications such as word processors and spreadsheets, command line tools, etc.<br>TREs with non-desktop interfaces should similarly consider carefully which applications are best suited for the data consumers needs when interacting with the data, for example “point and click” GUI tools for querying a database and generating plots of data.<br>The set of tools should be reviewed regularly to ensure they are up to date.|Mandatory|2|Tool available via software centre |
|**2.1.11.** Your TRE should provide tools to encourage best-practice in reproducibly analysing data.<br><br>Reproducibility of analyses improves auditability and accountability of how data has been used, as well as being best-practice in research.<br>This may include version control software, and tools for developing and running data analysis pipelines.|Recommended|2|Tool available via software centre |
|**2.1.12.** Your TRE could provide access to some public software repositories or container registries.<br><br>For example, a TRE may allow direct installation of packages from Python or R repositories, or provide an internal mirror.|Optional|2|Tool available via software centre |
|**2.1.13.** Your TRE could tightly control which packages are available.<br><br>For example, a TRE may only allow installation of a pre-defined set of approved packages.<br>You might also choose to scan for malicious packages and/or go through an approval process before allowing code into the technical environment.|Optional|2|Tool available via software centre |
|**2.1.14.** Your TRE must maintain segregation of users and data from different projects when using non-standard compute.<br><br>High performance or specialist compute is often shared amongst multiple users.<br>Users and data must remain segregated at all times.<br>For example, when using physical compute resources, all sensitive data could be securely wiped before another user is given access to that same node.<br>In a cloud hosted TRE virtual machines could be destroyed and recreated.|Mandatory|2|VREs are dedicated work spaces for projects|
|**2.1.15.** Your TRE should be able to provide access to high performance computing or other scalable compute resource if required by users.<br><br>If a TRE supports users conducting computationally intensive research it should provide access to dynamically scalable compute or the equivalent.<br>For example this may be in the form of a batch scheduler on a HPC cluster, or a dynamically created compute nodes on a cloud platform.|Recommended|0|LASER compute is manually scalable |
|**2.1.16.** Your TRE should be able to provide access to accelerators such as GPUs if required by users.<br><br>GPUs and other accelerators are commonly used in machine learning and other computationally intensive research.<br>TREs should make it clear to users whether GPUs and other resources are available whilst projects are being assessed.|Recommended|2|GPUs are available as needed |
|**2.1.17.** Your TRE could make data available to data consumers using common database systems such as PostgreSQL, MSSQL or MongoDB.<br><br>Databases must be secured and only accessible to users within the same project.<br>If shared (multi-tenant) database servers are used, database administrators must ensure that the database server enforces segregation of users and databases belonging to different projects.|Optional|2|VREs are dedicated work spaces for projects|
|**2.1.18.** Your TRE could integrate with large-scale data analytics tools for working with large datasets.<br><br>For example, Spark and Hadoop can be used for distributed computing across a cluster.<br>This may be an advantage where a TRE is using an amount of data that is too large for single-machine computing to be practical.|Optional|0||

### 2.2. Infrastructure management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**2.2.1.** You must have a documented procedure for deploying infrastructure.<br><br>This might, for instance, be a handbook that is followed or a set of automated scripts.|Mandatory|2||
|**2.2.2.** You should, where possible, automate any repeatable aspects of your deployment.<br><br>This might involve using infrastructure-as-code tools or a series of scripts.|Recommended|1|Infrastructure as Code' used in TRE builds, manually run by IT Services|
|**2.2.3.** You must have a documented procedure for making changes to deployed infrastructure.<br><br>This refers both to changes that might be expected in the course of normal operation and emergency changes that might be needed.<br>Your change management process may form part of a wider accreditation such as ISO 27001.|Mandatory|2|Change management is part of ISO 27001 and supported by IT processes. |
|**2.2.4.** You must test changes before they are used in production.<br><br>This might involve a separate development environment or another system for testing.|Mandatory|2|Test TRE created for development. |
|**2.2.5.** You should have a development environment that mirrors your production environment which you use to test infrastructure changes before committing them to production.<br><br>If possible, you should automate application of changes between development and production environments.<br>Consider the costs and practicality of whether this will work for your situation.|Recommended|0|Test TREs are created when testing is required, but a full dev platform would double running costs|
|**2.2.6.** You must have a documented procedure for removing infrastructure when it is no longer needed.<br><br>Removing unused infrastructure not only reduces costs and management burden but also reduces the attack surface of a TRE and reduces the risk of unaddressed vulnerabilities.|Mandatory|2|TREs are removed at end of project lifecycle|
|**2.2.7.** You should understand the availability and uptime guarantees of any providers that you rely on.<br><br>For remote TREs this might include your cloud provider(s) and/or data centre operators.<br>For on-premises TREs, it might be worth using an uninterruptable power supply (UPS) and planning how you would deal with internet outages.|Recommended|1|Managed by IT|
|**2.2.8.** You should develop an availability target or statement and share this with your users.<br><br>Understanding how and when the TRE might be unavailable will help your projects in planning their work.|Recommended|1|Managed by IT|
|**2.2.9.** Your TRE must control and manage all of its network infrastructure in order to protect information in systems and applications.<br><br>Network infrastructure must prevent unauthorised access to resources on the network.<br>This may include firewalls, network segmentation, and restricting connections to the network.|Mandatory|2|Network segregation in place |
|**2.2.10.** Your TRE must not allow connectivity between users in different projects, or with access to different datasets.<br><br>Connectivity between users in the same project may be allowed, for example to support shared network services within the project.|Mandatory|2|Each TRE is restricted to named users.  Pen tested.|
|**2.2.11.** Your TRE must block outbound connections to the internet by default.<br><br>Limited outbound connectivity may be allowed for some services.|Mandatory|2|Pen tested.|
|**2.2.12.** You should be able to monitor the network configuration of your TRE to check for misconfigurations and vulnerabilities.<br><br>This may include regular vulnerability scanning, and penetration testing.|Recommended|2|Vulnerability monitoring done by IT cyber security team, Pen testing undertaken.|
|**2.2.13.** You should regularly monitor the network configuration of your TRE to check for misconfigurations and vulnerabilities.<br><br>This will involve following the monitoring procedure detailed above.|Recommended|2|Vulnerability monitoring done by IT cyber security team|
|**2.2.14.** Your TRE must record usage data.<br><br>This may include the number of users, number of projects, the amount of data stored, number of datasets, the number of workspaces, etc.|Mandatory|2|Azure portal / Prism|
|**2.2.15.** Your TRE should record which datasets are accessed, when and by who.<br><br>This helps maintain auditability of how sensitive data has been used.|Recommended|2|Splunk|
|**2.2.16.** Your TRE should record computational resource usage at the user or aggregate level.<br><br>This is useful for optimising allocation of resources, and managing costs.|Recommended|2|Azure portal / Prism|

### 2.3. Capacity management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**2.3.1.** You must ensure that all projects understand what resources are available and what the associated costs will be before the project starts.<br><br>For on-premises systems this might be related to the available hardware, for cloud-based systems there might be limits on how many instances of a particular resource (*e.g.* GPUs) can be used<br>Projects should use this information to understand whether the available resources will be sufficient for their requirements.|Mandatory|2|RMP provide cost expectations, PRISM allows monitoring|
|**2.3.2.** You should ensure that the anticipated needs of projects can be satisfied using available resources.<br><br>Note that this does not require you to accept requests for additional resources, but rather that promises made about resource availability before a project starts should be honoured wherever possible.|Recommended|2|RMP Process sets expectations|
|**2.3.3.** You must have a procedure for allocating available resources among projects.<br><br>For cloud-based TREs this may involve scaling resources, such as virtual machines or databases, or deploying additional resources.<br>For on-premises TREs this may involve a procurement process to ensure that necessary resources are available.<br>Not all requests for capacity increase must necessarily be granted, but having a clear process will help projects understand when/why/how they can make use of additional capacity.|Mandatory|2|RMP Process sets expectations|
|**2.3.4.** You must ensure that the anticipated resource requirements will not result in overspending by the TRE.<br><br>For cloud-based TREs this may involve budgeting and/or restricting resource consumption on a project-by-project basis.<br>For on-premises TREs this may involve managing expectations to match the available resource.|Mandatory|2|RMP provide cost expectations, PRISM allows monitoring|

### 2.4. Configuration management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**2.4.1.** You must have a documented procedure for configuring infrastructure.<br><br>This might, for instance, be a handbook that is followed or a set of automated scripts.|Mandatory|2||
|**2.4.2.** You should use configuration management tools to automate application of your configuration wherever possible.<br><br>This might involve configuration-as-code tools such as Ansible, Chef, Puppet or Windows Desired State Configuration or simply automated scripts.|Recommended|2||
|**2.4.3.** You should be able to verify whether the configuration is valid.<br><br>This might, for instance, involve running your configuration management tool in ‘check’ mode.|Recommended|1|Manual checks are undertaken|
|**2.4.4.** You should regularly verify your TRE configuration.<br><br>This will limit the amount of time the TRE can spend in a non-compliant state.|Recommended|1|Not all existing checks are performed to a schedule|
|**2.4.5.** You must be able to replace a non-compliant TRE with a compliant system.<br><br>This might involve reconfiguring a running system or by replacing it with a compliant one.|Mandatory|2||

### 2.5. Information security  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**2.5.1.** You should keep backups of data and research environments, provided that this is permitted by law.<br><br>Keeping backups could help reduce the impact of events like accidental deletion and data corruption on work in a TRE.<br>TRE developers may want to consider how different elements such as sensitive input data or users’ workspaces may be backed up, and whether they should be.|Recommended|2||
|**2.5.2.** You should build redundancy into infrastructure and storage.<br><br>Infrastructure should be as resilient as necessary to interruption.<br>This could include redundant infrastructure in different physical locations, load balancing and replication of data between multiple storage locations.|Recommended|2|Scable solution. |
|**2.5.3.** You should keep backups of infrastructure, applications and configurations.<br><br>This may include virtualised infrastructure snapshots which can restored as needed to recover from failure.|Recommended|2||
|**2.5.4.** You must have procedures in place for rapid incident response.<br><br>There may be legal requirements to disclose details of any incidents, such as data breaches for organisations subject to GDPR.<br>Having robust processes in place will ensure a swift and effective response when an incident occurs.|Mandatory|2|Data Breach process ties into University structure|
|**2.5.5.** You should test your incident response through simulation.<br><br>During simulated incidents the TRE organisation can measure their effectiveness.<br>This may involve people across the broader enterprise and/or external suppliers.|Recommended|1|Live exercise take place across the University . Process tested but not in TRE environment.|
|**2.5.6.** You should have an application in place to scan for vulnerabilities across infrastructure.<br><br>Software used to identify vulnerabilities should also report and alert.<br>Such an alert should be triaged, risk assessed and treated accordingly.|Recommended|2|Managed by IT|
|**2.5.7.** You must have a process in place for applying security updates to all software that forms part of the TRE infrastructure.<br><br>This includes any software used for remote desktop portals, databases, webapps, creating and destroying compute infrastructure, configuration management, or software used for monitoring the TRE.|Mandatory|2||
|**2.5.8.** Infrastructure should be automatically patched for vulnerabilities.<br><br>Planning will be required across infrastructure and software systems to ensure security patches remain available from suppliers.<br>Many systems may be isolated from the internet making TRE infrastructure more difficult to automatically patch.|Recommended|1|Manual patching processes in place|
|**2.5.9.** You should carry out penetration tests on your TRE.<br><br>By intentionally attempting to breach their TRE, organisations can proactively discover unnoticed vulnerabilities before they are exploited maliciously.<br>Tests can evaluate the effectiveness of security controls in preventing data breaches, unauthorised access, or other security incidents.|Recommended|2||
|**2.5.10.** You should update the security controls of your TRE based on the results of security tests.<br><br>Security testing can reveal bugs and discrepancies in the TRE architecture which should be addressed in advance of sensitive data being uploaded, or with urgency in the case of an operational TRE.<br>Regular testing will allow organisations to refine their TRE security controls and incident response capabilities.<br>It enables them to adapt to any new security concerns that may arise as a result of changes in the underlying software.|Recommended|2||
|**2.5.11.** You should publish details of your security testing strategy and, where possible, the results of each test.<br><br>Knowledge that regular security testing occurs will help to ensure stakeholders, including data consumers and information asset owners, can trust that the data they work with or are responsible for is secure within a TRE.<br>If security flaws are identified in a test, it may not be sensible to publicise these until a fix is in place.|Recommended|1|Internal sharing of results and limited information provied on request.|
|**2.5.12.** Your TRE must encrypt project and user data at rest.<br><br>This prevents unauthorised access to the data even if the storage media is compromised.<br>This may involve encrypted filesystems or tools to encrypt and decrypt data on demand.<br>The encryption keys may be managed by the TRE operator or by a trusted external actor, for example a cloud provider.|Mandatory|2||
|**2.5.13.** Your TRE must encrypt data when in transit between the TRE and external networks or computers.<br><br>Data encryption must be used to safeguard against interception or tampering during transmission.<br>This includes both data ingress and egress and users accessing the TRE, for example over a remote desktop or shell session.|Mandatory|2||
|**2.5.14.** Your TRE should encrypt data when in transit inside the TRE.<br><br>If possible, data transfers between different components of a TRE should also be encrypted.|Recommended|2||
|**2.5.15.** You should use encryption algorithms and software that are widely accepted as secure.<br><br>Encryption algorithms widely accepted as secure today may become insecure in the future, for instance due to newly-identified flaws, or advances in compute capabilities.<br>The latest security patches and updates should be applied to any encryption software being used by the TRE.<br>This helps address any known vulnerabilities or weaknesses in the encryption implementation.|Recommended|2||
|**2.5.16.** Your TRE should use secure key management.<br><br>TREs should employ secure key management practices, including storing encryption keys separately from the encrypted data and implementing strong access controls (*e.g.* Single Sign On) for key management systems.|Recommended|2||
|**2.5.17.** Your TRE could offer physical protection measures against data leakage or theft via physical means.<br><br>Restricting access to research facilities containing computers logged into TREs can help prevent malicious actors from viewing or stealing sensitive data, for example by photographing a computer screen.<br>Physical controls on access to a TRE could include surveillance systems, restricting physical access to authorised personnel only, visitor management systems and employee training.|Optional|2|Fob access to secure office denvioremnt .  Clear desk policies enforced. .  Tier 4 data is restricted to safe rooms / safe space where no phones , pen and papers allowed.  CCTV in place and visitors accompanied. |
|**2.5.18.** Your TRE may need to comply with specific regulatory requirements due to the types of data it is hosting.<br><br>Regulatory frameworks often emphasise the need for security controls to protect sensitive data.<br>Compliance with these regulations could require organisations to implement specific security measures to safeguard their TRE from unauthorised access.|Mandatory|2|All data managed according to DS  / DPIA  . ISO27001:2022 complaint , DSPT |

## 3. Data management
### 3.1. Data lifecycle management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.1.1.** You must have processes in place to assess the legal and regulatory implications of handling the data through its full lifecycle.<br><br>This involves considering your obligations to data controllers and subjects, and whether any security controls may be legally or contractually required.<br>An assessment of the risks involved will also be needed.<br>It may involve classifying the project into a predefined sensitivity category or defining bespoke controls.|Mandatory|2|Tiering model used to predefine sensitivity category|
|**3.1.2.** You should keep records of data handling decisions.<br><br>Decisions that are made as part of the process discussed above should be recorded and made available for inspection by all stakeholders.|Recommended|2|Recorded though DSA / DPIA|
|**3.1.3.** Information asset owners must classify data sets according to a common process and data classification methodology.<br><br>To classify the data, information asset owners must have a good understanding of the datasets and the process of classification.<br>Once classified, data can be stored in a TRE with an appropriate security controls (see later section on security levels and tiering), which can factor in the requirements for confidentiality, integrity and availability of the data.|Mandatory|2|Tiering model used to predefine sensitivity category|
|**3.1.4.** You must have a data ingress process which enforces information governance rules/processes.<br><br>The data ingress process needs to ensure that information governance is correctly followed.<br>In particular, it should require that an ingress request has been approved by all required parties.|Mandatory|2|BISCOM route for data ingress|
|**3.1.5.** You must have a data egress process which enforces information governance rules/processes.<br><br>The data egress process needs to ensure that information governance requirements are adhered to.<br>In particular, it should require that an egress request has been approved by all required parties.|Mandatory|2|BISCOM route for data ingress|
|**3.1.6.** Egress must be limited to the information asset owners or their delegates.<br><br>Egress of data from a TRE must be a specific permission associated with individual users<br>This permission must be given by information asset owners.<br>Egress may still require further approval (see 3.1.5).|Mandatory|2|Recorded though DSA / DPIA|
|**3.1.7.** Your data egress process could sometimes require project-independent approval.<br><br>There may be cases where there are multiple stakeholders for a piece of analysis including information asset owners, data analysts, data subjects, the TRE operator.<br>A data egress process may then require approval from people not on the project team, for example an external referee or TRE operator representative|Optional|2|Recorded though DSA / DPIA|
|**3.1.8.** You must keep a record of what data your TRE holds.<br><br>Good records are important for ensuring compliance with legislation, understanding risk and aiding good data hygiene.<br>The record should include a description of the data, its source, contact details for the data owner, which projects use the data, the date it was received, when it is expected to no longer be needed.|Mandatory|2|Recorded though DSA / DPIA|
|**3.1.9.** You must have a policy on data deletion.<br><br>There should be a clear, published policy on when data will be retained or deleted.<br>This may allow time for data owners to consider outputs they may want to extract from the TRE.<br>Any sensitive data, including all backups, should be deleted when they are no longer needed.<br>Having clear policies will help to avoid problems with data being kept longer than necessary or accidental deletion of outputs.|Mandatory|2|Recorded though DSA / DPIA|
|**3.1.10.** You should have a method of providing proof of deletion/removal of files.<br><br>Information asset owners may require certification of the deletion of files.<br>You should have a method of providing proof of deletion if challenged.|Recommended|2|Destruction certificate produced.|
|**3.1.11.** You should log how input data is modified.<br><br>If the input data is mutable a TRE should keep records of its modification.<br>For example, when the data was modified and by who.|Recommended|N/a|Data Agnostic service|
|**3.1.12.** You must, to a reasonable extent, prevent unauthorised data ingress or egress.<br><br>Movement of data which has not been subject to information governance processes risks breaking rules and is more likely to result in a data breach.<br>However, it is difficult to control for every possibility.<br>For example, a user may take pictures of their computer screen to remove data, or use a device presenting as a USB HID keyboard to input large amounts of text.<br>An example of a reasonable measure would be for a remote desktop based TRE to prevent data being copied from a local machine’s clipboard to a workspace.|Mandatory|2||
|**3.1.13.** Data held within the TRE should be the minimum required for analysis or research.<br><br>Data stored and processed within the TRE should be limited to the amount required for that purpose.<br>This increases the level of protection for data subjects, makes it easier to comply with data protection legislation and could reduce the overhead of storage and processing.|Recommended|2|We work with researchers and data owners to apply the principle of minimisation|

### 3.2. Identity and access management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.2.1.** You must not create user accounts for use by more than one person.<br><br>It is important that each user account should be used by one, and only one, person in order to facilitate the assignment of roles or permissions and to log the actions of individuals.|Mandatory|2|Each user has a unique user identify|
|**3.2.2.** You must be reasonably convinced of the identity of each person being granted an account.<br><br>It is important to ensure an account has been given to the correct person.<br>For example, multiple credentials may be used before account creation to verify identity or, when appropriate, photo ID checks may be required.|Mandatory|2|Each user has a unique user identify|
|**3.2.3.** You must restrict a user’s access to only data required in their work.<br><br>There is no need to grant an individual access to data they do not require.<br>Access may be assigned in a manner appropriate to a TREs design, for example through roles granted to user accounts or through isolated project workspaces.|Mandatory|2|Each TRE is restricted to named individuals|
|**3.2.4.** You must ensure that multi-factor authentication is enabled for all users.<br><br>Multi-factor authentication ensures that to successfully connect a user must have more than one piece of evidence in different categories.<br>Categories include something the user knows (*e.g.* a password), something the user possesses (*e.g.* a TOTP key) or something the user is (*e.g.* biometric data).<br>A TRE does not need to implement multi-factor authentication checks itself if it is provided by a third-party identity provider.|Mandatory|2|MFA in place ( Duo) |
|**3.2.5.** You could use federated authentication or single sign-on (SSO) for user login.<br><br>Institutions that use a SSO for other applications may wish to extend this login capability to a TRE.<br>This will simplify the login process for data consumers using a TRE and prevent them having to remember or store multiple login credentials.|Optional|2||
|**3.2.6.** You could restrict access to particular networks or physical locations.<br><br>Restricting access to a set of known, static, personal or institutional IP addresses can help avoid speculative attacks.<br>When appropriate, access could also be restricted to physical locations with security controls and access requirements.|Optional|2|Thin clients in place for Tier 4 data, network segregation in place for LASER |

### 3.3. Output management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.3.1.** You should have a system to help classify outputs.<br><br>Removing data from a TRE can be a difficult process as there is potential for sensitive data to be revealed.<br>Having guidance, processes and methods will help ensure that outputs are correctly classified and, furthermore, that outputs due to be openly published are identified.<br>Encouraging openly published outputs will enhance a TRE’s impact and transparency.|Recommended|2|Recorded though DSA / DPIA|
|**3.3.2.** You should establish the intended outputs of each project from the outset.<br><br>Identifying the purpose of a piece of work is important for compliance with data protection legislation.<br>Results will be produced which address the project’s purpose, some of which may be outputs that are removed from the TRE.<br>Understanding what these outputs are likely to be and their sensitivity as early as possible will help prepare for their processing and publication.|Recommended|2|Recorded though DSA / DPIA|
|**3.3.3.** You must have a documented process for disclosure control of outputs from the TRE.<br><br>This process should define expected risks and how to mitigate them.<br>All TRE outputs must be subject to this process.<br>You might choose to follow existing guidelines, for example around statistical disclosure.|Mandatory|2|Recorded though DSA / DPIA|
|**3.3.4.** You must have a process for assigning responsibility for output checking.<br><br>Output checkers should be given responsibility for checking outputs.<br>They must follow your disclosure control process and will be responsible for any automated parts of this process.<br>Output checking can help mitigate against unintentional data disclosure or leaks.|Mandatory|2|Recorded though DSA / DPIA|
|**3.3.5.** You must have a documented policy for handling disclosure risks associated with any outputs that cannot be manually checked.<br><br>Some categories of output, for instance binary files or very large numeric files, can be difficult to manually check.<br>If egress of such files is permitted then the risks of inadvertent disclosure must be mitigated and documented.<br>Refusing to allow egress of such files is also a valid policy decision.|Mandatory|1|Process is understood but yet to be documented|
|**3.3.6** You should have a statistical basis to guide the decisions of an output checker on the safety of outputs.<br><br>There should be a solid basis to allow decisions to be made about data based on risk factors such as re-identification of an individual or risk to commercial operations posed by outputs from the TRE.|Recommended|2|Tiering model used to predefine sensitivity category|
|**3.3.7** You could create a semi-automated system for checks on common research outputs.<br><br>Automation helps make decisions on outputs more consistent and reduces the overhead for output checkers.<br>It’s unlikely however that a fully automated output checking system (without humans in the loop) would be appropriate, given the risks associated with accidental data disclosure.|Optional|1|Humans in every loop |
|**3.3.8.** TRE outputs should be limited to the minimum required for sharing results of any analyses.<br><br>This decreases the risk of inadvertent disclosure, and makes it easier to comply with data protection legislation (e.g. GDPR).|Recommended|2|Recorded though DSA / DPIA|

### 3.4. Information search and discovery  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.4.1.** You should provide a metadata catalogue of available datasets for users.<br><br>This is particularly relevant for TREs with population-level data collection of general interest.<br>This may not be appropriate for TREs where each project has its own data sharing agreement with one or more data provider or very sensitive datasets.|Recommended|N/a||

### 3.5. Security Levels and Tiering  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.5.1.** You must be able to specify what categories of data your TRE is able to support.<br><br>Your TRE must provide an explanation of the kinds of data it has been designed to hold, with reference to its security capabilities, that can be understood by all stakeholders.<br>Relevant stakeholders may include information asset owners and project teams and they may have different levels of technical expertise.|Mandatory|2|Tiering model Allows project to work within a suitable level on control |
|**3.5.2.** Your TRE could support projects with differing security requirements through configurable security controls.<br><br>This allows projects with different security requirements to each be met with a suitable level of controls.<br>It helps ensure that users can work effectively, with minimal barriers.|Optional|2|Tiering model Allows project to work within a suitable level on control |
|**3.5.3.** Your TRE could offer a pre-defined set of security control tiers.<br><br>Security control tiers can be designed to cover the types of project or data you expect to handle.<br>Projects may be placed into the most suitable tier rather than having a bespoke design.<br>This reduces the number of unique configurations that need to be supported.|Optional|2|Tiering model Allows project to work within a suitable level on control |

### 3.6. Research Meta-Data  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.6.1.** You should have a consistent and easily accessible meta-data data model or similar to describe what a data asset contains.<br><br>Where possible, existing data models should be employed (and extended if necessary).<br>More detailed information on the data schema for data assets should also be provided to assist researchers in understanding what data may be available without the need to see the underlying data.|Recommended|2|Recorded though DSA / DPIA|
|**3.6.2.** You could provide summary, abstracted or synthetic data to researchers without exposing the underlying data set.<br><br>To reduce the need for access to row level data researchers could be provided with non-sensitive versions of the data either as summary data or using synthetic versions of the data for activities such as code development and cohort planning.|Optional|2||

### 3.7. Meta-Data Search and Discovery Application  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.7.1.** You could provide an interface application for data consumers and data subjects to query elements of the data.<br><br>In order to make data findable, an application which queries the meta-data or elements of the research data could be made more easily accessible than the data itself.|Optional|N/a||

### 3.7. 3.8. Data Archiving  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**3.8.1.** Archived data within the TRE should be read only.<br><br>Archived data by its very nature should not change and therefore be maintained as a read only store.<br>If an update is required, it may be pulled from archive into a separate operational store.|Recommended|2||
|**3.8.2.** Long-term archives must be held in simple, standard formats to ensure accessibility.<br><br>Some data archives may be required by policy or legislation to be kept for very long periods within the scope of the TRE.<br>Such data should be held in the simplest possible file format, conforming to international standards if available, to ensure they are platform and application agnostic.|Recommended|2||

## 4. Supporting Capabilities
### 4.1. Business continuity management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.1.1.** You should have a business continuity plan that includes consideration of loss of service for deployed TREs.<br><br>This may be due to downtime from service providers, a breach, or loss of power.<br>Your plan should detail your process for managing loss of service for deployed TREs, and evaluation of impact of such loss.|Recommended|2||
|**4.1.2.** You should regularly test the aspects of your business continuity plan concerning TREs, and have a process in place to iterate the plan if required.<br><br>|Recommended|2||

### 4.2. Project and programme management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.2.1.** You should ensure that all projects using your TRE have a named project manager.<br><br>The project manager has responsibility to ensure the smooth running of the project.<br>Their responsibilities may include budget management, tracking TRE status, managing communications with the TRE operations team, and other project support tasks.|Recommended|2||
|**4.2.2.** You should not give project managers direct access to the TRE.<br><br>Doing so ensures a separation between those able to access sensitive data, and those overseeing access to sensitive data.|Recommended|2||

### 4.3. Knowledge management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.3.1.** You must document all features of your TRE implementation.<br><br>This includes ensuring all documentation is discoverable, clear, and able to be easily updated based on stakeholder feedback|Mandatory|1|Some aspects could be more clear|
|**4.3.2.** You should have an education programme in place to upskill stakeholders in the use and management of your TRE.<br><br>This may include learning modules, workshops and other resources on how to effectively access and use a TRE, FAQ pages, and accessible pathways for additional support|Recommended|2||
|**4.3.3.** You should periodically carry out a training needs analysis (TNA) for all stakeholders included within your TRE provision.<br><br>At least once every 12 months you should assess the training needs of your stakeholders, and ensure they have easy access to all required training materials|Recommended|2|Done as part of ISMS review|

### 4.4. Financial management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.4.1.** You must ensure that all projects using your TRE are aware of any associated costs and are able and willing to pay them.<br><br>Costs may include provision of the underlying TRE infrastructure, additional resources required in a specific TRE (for instance memory or additional compute), hardware including managed devices, and staff support costs|Mandatory|2|Agreed through RMP|
|**4.4.2.** You should be able to track the costs associated with each TRE project.<br><br>This includes knowing which costs are associated with which project, and having an appropriate charging mechanism in place in line with your organisational policy.|Recommended|2|Azure portal / Prism|
|**4.4.3.** You should have a process in place to ensure your TRE provision remains financially sustainable.<br><br>This could include having a cost recovery process in place, or setting up a long-term funding mechanism to support projects with TREs.<br>At any given time, you should have funds free to cover all potential foreseen TRE provision for at least 12 months.|Recommended|2||
|**4.4.4.** You should minimise the cost of your TRE infrastructure wherever possible<br><br>You should have regular reviews of your TRE provision and actively work to bring down costs, streamline provision, and optimise support.|Recommended|2||

### 4.5. Procurement  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.5.1.** You must identify any goods or services that will be needed to operate the TRE and ensure that a plan is in place to purchase them as needed.<br><br>These may include computing hardware, cloud credits or devices through which users access the TRE.|Mandatory|2|Managed according to Univerty Processes|

### 4.6. IT Service management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.6.1.** Your TRE must have a team of Operators in place to support projects working with TREs.<br><br>This may be part of your organisation’s IT support team, or separate.<br>Responsibility should be clear and stakeholders should easily be able to access support appropriate to their needs.|Mandatory|2|DAT team and IT provide service to LASER |

### 4.7. Relationship management  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.7.1.** You should have a clear process in place for stakeholders to feedback on your TRE infrastructure.<br><br>This may include a GitHub repository where people can open issues and discussions, communication streams like Slack or email, or forms stakeholders can fill in.|Recommended|1|Issues and suggestions can be reported directly to DAT, discussed on the LASER User Group on Teams Channel or directly with IT Services|

### 4.8. Public Involvement and Engagement  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.8.1.** All public engagement activities must include a range of perspectives and be inclusive (*optional for TREs without personal data).<br><br>Any public engagement activity carried out by TREs should involve diverse participants and that activities are accessible.<br>Recruitment plans should consider how to proactively reach a representative sample of people or target particular groups of people where relevant<br>This could include following guidelines such as PEDRI.|Mandatory*|n/a|LASER is data agnostic, responsibility for this activity lies with each project and their PI; University processes (eg Ethics) should ensure compliance|
|**4.8.2.** Details of TRE operations, data available and projects which have accessed the data should be publicly available (*optional for TREs without personal data).<br><br>TREs should be as transparent as possible by providing information online.<br>Where information is made available online this should be written in clear language understandable to general public.<br>A record of projects which have accessed data via the TRE should be kept and made available.<br>Where possible it should include name, summaries, public benefit (if relevant) and organisations involved|Mandatory*|2|Information provide at Project level |
|**4.8.3.** Members of the public should be included in TRE operations and/or oversight (*optional for TREs without personal data).<br><br>Members of the public can be involved via presence on steering groups or project approvals panels.<br>Alternatively TRE’s can establish separate public panels available for both researchers and TRE staff to consult.|Mandatory*|N/a||
|**4.8.4.** You should publicly share details of incidents, near misses, and mitigations in a timely fashion, in line with good practices for responsible disclosure.<br><br>This may be via the TRE website or annual reports.<br>Sharing this information is particularly important when a TRE holds public sector data.|Recommended|2||

### 4.9. Legal services  

|Component  |Importance |Score      |Response   |
|---        |---        |:-:        |---        |
|**4.9.1.** You should identify areas where legal advice may be required and ensure that you have ready access to it.<br><br>It is likely that legal advice will be necessary for several issues around the handling of sensitive data, and managing project contracts.<br>TRE operators should have ready access to legal advice, including a way to solicit advice and carry out associated actions.|Recommended|2|DPO sits on Information Governance Managemnt Group (IGMG), Information Governance Manager embedded in LIDA|
|**4.9.2.** You should identify areas where advice on data protection issues may be required and ensure that you have ready access to it.<br><br>It is likely that data protection advice will be necessary for several issues around the handling of sensitive data.|Recommended|2|DPO sits on Information Governance Managemnt Group (IGMG), Information Governance Manager embedded in LIDA|
|**4.9.3.** You should identify who will be responsible for managing contracts related to the TRE.<br><br>These contracts may include data sharing agreements, secondments of personnel or limitations on how results obtained with the data can be distributed.|Recommended|2||
