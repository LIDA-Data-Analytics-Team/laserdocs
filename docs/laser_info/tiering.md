---
layout: default
title: LASER Data Risk Tiering
parent: LASER Info
nav_order: 1.1
---

# LASER Data Risk Tiering

Data providers often classify their data (e.g. personally identifiable, pseudonymised, anonymous) and share it based on a set of firm requirements detailed in a ‘Data Sharing Agreement’ (DSA). That would set the minimum standards of security required. LIDA and/or PI/researcher may have a view that the data is more sensitive and want more assurance than the provider contractually requires.

The following data risk classification tiers have been adopted from the Alan Turing Institute and are used to assess the data and associated risks.

## Data Risk Tier - Disclosure Impact

|Tier 0	|Tier 1	|Tier 2	|Tier 3	|Tier 4	|
|---|---|---|---|---|
|**No impact on UoL**, partners or data subjects	|**Low impact** on UoL; legal penalty or damage to reputation highly unlikely. |**Medium impact** on UoL or partners leading to legal, commercial, contractual, financial penalty or damage to reputation. |**High impact** to UoL, partners or data subjects with potential for contractual, commercial, legal, financial or reputational penalties.	|**Significant impact** to UoL, partners or individuals with potential for substantial legal, financial or reputational penalties.|
|	|**No impact** on partners or data subjects |**Limited impact** on data subjects |	|	|

## Data Risk Tier - LASER Description

|Tier 0	|Tier 1	|Tier 2	|Tier 3	|Tier 4	|
|---|---|---|---|---|
|Information that does not require any protections. |Not Personal Data - Confidence in the quality of the anonymisation is absolute. |Identifiable personal data which does not include special categories of data or link to special categories of data held elsewhere in the University of Leeds. |**Special categories of personal data or data collected under a duty of confidentiality** where disclosure poses **a threat** to personal safety, security, health or wellbeing: <br/>The data is: <br/>Weakly pseudonymised but does not contain direct identifiers, therefore poses little risk of unauthorised person viewing data e.g. over the shoulder of LASER. |**Special categories of personal data or data collected under a duty of confidentiality** where disclosure poses a **substantial threat** to personal safety, security, health or wellbeing: <br/>The data is: <br/>Directly identifiable |
|	|OR |OR |OR |AND/OR |
||Disclosive data where release/sharing was explicitly agreed in consent and fully described in participant information. |Pseudonymised or synthetic data where confidence in the quality of anonymisation is strong. This can be interpreted as: <br/>- Data provided by reputable 3rd party organisation where the 3rd party organisation holds the salt / pseudonymisation key <br/>- Data which is derived from personal data but it would not be possible to re-identify individuals from the data using any reasonable mechanisms available to the authorised user.|Robustly pseudonymised where individuals could be identified indirectly through combination with other information which is not easily available to the person accessing the information but could be available if the individual accessing the data were motivated to e.g. only protected by professional standards.|Commercial or governmental data which is sensitive or likely to be subject to attack by attackers with bounded capabilities, such as hacktivists. |
|	|AND |AND/OR |AND/OR |AND/OR |
||Datasets where the only risk of disclosure is assisting the researcher’s competitors.|Confidential project documents restricted by ethical, legal or contractual obligations. |Commercial or governmental data which is sensitive or likely to be subject to attack by attackers with bounded capabilities, such as hacktivists. |Consent, ethical or contractual restrictions controlling how the data is handled. |
|	|	| |AND/OR |OR |
||||Ethical, commercial or contractual restrictions controlling how the data is handled. |Weakly pseudonymised – real world identifiers remain which could be combined with other information easily available to the person accessing the information. |

## Data Risk Tier - LASER Examples

|Tier 0	|Tier 1	|Tier 2	|Tier 3	|Tier 4	|
|---|---|---|---|---|
|Derived (non-disclosive) analysis outputs, brochures, website text intended for  immediate publication (i.e. not subject to journal or other restrictions)|Derived (non-disclosive) analysis outputs, brochures, website text|Project uses data which has been pseudonymised by a 3rd party organisation. Although there is no intention to re-identify patients, 3rd Party organisation hold the pseudonymisation key|Datasets made up of pseudonymised and anonymised interview transcripts containing open ended questions and considerable personal detail on sensitive topics. |- Certain health conditions with contentious socio-political associations, <br/>- Protected characteristics, <br/>- Political activism, extreme religious or political affiliation <br/>- Criminal activity and witness statements <br/>- Extreme political <br/>- Direct access to NHS Spine|
||With appropriate consent, story-telling or oral histories.|Robustly de-identified primary care data on individuals with low risk of re-identification, provided by a trusted third party |Anonymisation of variable strength. Consent was given for the sharing of anonymised transcripts but academic norms in this discipline recommend a higher classification.|DSA states that safe room access must be used, commercial sensitivity|
||With appropriate consent, “On the record” interviews with public figures.|Data concerning mobile tower load & capacity; potential commercial sensitivity but highly aggregated so not possible to identify individuals|Data used in collaboration with industrial partners. Detail of implant designs are visible in CT scans of recipients that are then used to model mechanical properties in use.|Police crime data with personal identifiers removed, crime & response details and geographic markers present|
||||Care home data at building level de-identified at source, and individual care home staff level data de-identified at source. De-identification involves replacing identifiers only, no further statistic disclosure mapping therefore quality of pseudonymisation is weak.|Personal data about people taking part in / running a controversial piece of research (possibly where specific threat exists) – significant risk to these people’s safety in case of disclosure|
||||De-identified primary care data on individuals, provided by a trusted third party. DSA states data will be held in ISO27001 compliant environment|Governmental data related to defence systems|
||||Processing involving contact details of trial participants (participating in medical research) – disclosure would have negative consequences|Uses personal identifiable data including names, full addresses, NHS numbers and some medical history|
||||Processing of qualitative interview data about sensitive topics – disclosure would cause significant upset to data subjects|Processing bank details data (in research context, collecting bank details of trial participants so they can be reimbursed for specific expenses incurred through trial participation) – significant risk to people’s financial circumstances in case of disclosure|
||||Any other identifiable data. Any non-Tier 4 personal sensitive data (e.g. general health data) and personal data that does not pertain to a sensitive category, e.g. food outlet purchases, course module attendees. The latter could be deemed low threat (like tier 2), but is excluded from tier 2 because of its personal nature (not pseudonymised or commercial or legal).|Raw interview audio and transcripts containing very detailed personal information. Consent explicitly excludes sharing of raw data.|
|||||Poaching a serious threat. Detail of time and location of photographs is important to the value of the data – sensitivity cannot be reduced.|
|||||Camera trap data from wildlife surveys in threatened habitats.|
