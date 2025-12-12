---
layout: default
title: IG references and information for DSAs
parent: Useful Information
has_children: false
---

# IG references and information for DSAs

When projects apply for data or prepare data sharing agreements, we're often asked to provide information about LASER technical controls and security assurances.

[LASER](#laser)  
[University of Leeds](#university-of-leeds)  
[Microsoft](#microsoft)  
[Documents](#documents)  
[FAQs](#faqs)  


## LASER

| Item | Reference | Date Certified | Expires |
| --- | --- | --- | --- |
| ISO 27001 | 15331-ISN-001 | 18 April 2023 | 14 May 2026 |
| NHS DSPT | [8KM29](https://www.dsptoolkit.nhs.uk/OrganisationSearch/8KM29) | Latest Status: 2022-23 Standards Met <br>Date Published: 02 May 2023<br>NHSD confirmed CAG reqs met: 17 August 2022<br>Date self-assessment submitted to NHS England: 20/02/2023 | 30 June 2024 |

<details>
<summary>Processing & Storage Locations: (click to expand)</summary>

<h3>Processing Location(s)</h3> 
<table>
    <tr>
        <th>Microsoft Limited</th>
    </tr>
    <tr>
        <td>Location Area</td>
        <td>England & Wales</td>
    </tr>
    <tr>
        <td>Organisation Address</td>
        <td>Azure UK South (Primary Data Centre)<br>London<br>KT9<br></td>
    </tr>
</table>
<table>
    <tr>
        <th>Microsoft Limited</th>
    </tr>
    <tr>
        <td>Location Area</td>
        <td>England & Wales</td>
    </tr>
    <tr>
        <td>Organisation Address</td>
        <td>Azure UK West (Backup Data Centre)<br>Cardiff<br>CF10<br></td>
    </tr>
</table>

<h3>Storage Location(s)</h3> 
As above

<h3>Territory of use:</h3>  
England & Wales  

</details>

## University of Leeds

| Item | Reference | Expires |
| --- | --- | --- |
| DPA registration | [Z553814X](https://ico.org.uk/ESDWebPages/Entry/Z553814X) | 2023-08-27 |

- Name: University Of Leeds
- Organisation address: Woodhouse Lane, Leeds, West Yorkshire, LS2 9JT

## Microsoft

| Item | Reference | Expires |
| --- | --- | --- |
| DPA registration | [Z6296785](https://ico.org.uk/ESDWebPages/Entry/Z6296785) | 2024-01-08 |
| ISO 27001 | [1729711-12A](https://servicetrust.microsoft.com/viewpage/ISOIEC) | 2026-06-17 |

## Documents

Sometimes we need to share documents to evidence security standards etc. Not all documents can be shared freely. Here is a list of documents data providers may ask for and how they can be shared.

| Item | Public/Confidential | Location |
| --- | --- | --- |
| LASER ISO 27001 certificate | Public | `N:\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\ISO 27001\ISO27001 Certificates\IRC 27001 Certificate of Registration 2023-2026.pdf` |
| LASER DSPT review against CAG confirmation | Public | `N:\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\NHS IG Toolkit\LASER\2021 LASER DSPT\Confirmation LASER DSPT met CAG requirements 2022-08-25.msg` |
| LASER DPIA | Public | `\\ds.leeds.ac.uk\shared\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\LASER documents\` |
| NHS Cloud Controls (LASER) | Public | [General - TEAM - LIDA Data Services Team\Information Governance\DSPT\Cloud Controls - LASER.xlsx](https://leeds365.sharepoint.com/:x:/r/sites/TEAM-LID/Shared%20Documents/General/Information%20Governance/DSPT/Cloud%20Controls%20-%20LASER.xlsx?d=wb672dd6e526941099d4195a47ca77141&csf=1&web=1&e=sNOaVA) |
| LASER ISMS | Confidential: Ask LIDA IG Manager for shareable info | `\\ds.leeds.ac.uk\shared\Academic-Services\ISS\IRC-Data-Services\Processes\ISMS\` |
| Microsoft Azure ISO 27001 certificate | Public | `\\ds.leeds.ac.uk\shared\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\LASER documents\` |
| Microsoft DPA and T&Cs | Public | `\\ds.leeds.ac.uk\shared\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\LASER documents\Microsoft DPA\` |
| Instruction to process data in UK | Public | `\\ds.leeds.ac.uk\shared\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\LASER documents\Instruction to process data in UK\` |
| Microsoft-UoL enrollment agreement | Confidential: Do not share without signed NDA | `\\ds.leeds.ac.uk\shared\Academic-Services\ISS\IRC-Data-Services\Information Management\Assurance Frameworks\LASER documents\Microsoft Enrollment Agreement\` |

## FAQs

Here are questions we've previously been asked and answers that were approved by IG and/or fine to use again:
- What agreements are in place to ensure the solution keeps pace with information security developments?
    - The University of Leeds have a Data Processing Agreement with Microsoft which covers the keeping pace with information security developments.
- Are the system’s network interfaces hardened?  For example have all unnecessary services been disabled and ports closed?
    - All interfaces configured in line with the University security policy, the platform is ISO27001 certified and compliant
- How does the solution protect access to network traffic on shared networks?
    - By default all research projects are segregated onto their own subnet and protected by Network Security Groups.
- What anti-malware controls apply within the solution?
    - All workstations and servers have McAfee endpoint protection installed.
    - UPDATE 2022-10-19: McAfee/Trellix is being replaced with Windows Defender for Endpoint in the future
- What method of disposal or destruction will be used when this period has expired (including archive and backup copies)?
    - We delete the data, then delete the encryption key for the storage and backups, then destroy the entire project environment. Microsoft Azure media destruction follows NIST 800-88 guidelines.
- What evidence will be obtained that destruction has occurred (e.g. IT supplier certificate of destruction)?
    - We can provide a university-administered certificate of data destruction
- Describe how the mechanisms which safeguard data security will be audited and reviewed at regular intervals to ensure their continued efficacy.
    - Annual audits for compliance against ISO27001 and NHS DSPT security standards, including penetration testing. More regular internal reviews of ISMS policies, processes that underpin the policies and documentation that supports the processes.
- Describe the breach reporting mechanisms to be invoked in the event of any inappropriate access to data or other information security incident
    - We follow university process for reporting a data breach: https://dataprotection.leeds.ac.uk/reporting-a-data-security-incident/. Except we escalate directly to the LIDA Information Governance Manager rather than IT Service Desk. Project responsible owners, data owners/subjects and the ICO are informed as needed.
