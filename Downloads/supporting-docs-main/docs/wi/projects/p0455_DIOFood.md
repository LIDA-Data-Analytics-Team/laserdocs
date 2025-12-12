---
layout: default
title: P0455 DIO
parent: Project Work Instruction
has_children: false
---

# DIO Food Project

The **DIO Food Project** is a multi-retailer project that receives data from four major retailers, namely:
- **ASDA**
- **Morrisons**
- **Sainsbury's**
- **TESCO**

Three of these retailers have **TREs** on **LASER** and one on **Morrisons** systems.

The names of the TREs, the retail data held, and the method of file transfer are listed in the table below:

| **TRE Name** | **Data Held**   | **Method of File Transfer** | **Any Other Data Held** |
|--------------|-----------------|-----------------------------|-------------------------|
| P0455v01     | ASDA            | Biscom                      | Brandbank data           |
| P0455v02     | Sainsbury's     | Snowflake*                  | Brandbank data           |
| P0455v03     | TESCO           | Biscom**                     | Brandbank data           |

\* Adam should be given access to the Snowflake system, and the Snowflake URL can only be accessed in DAT02 (URL: yk60034.eu-west-1.snowflakecomputing.com/console)  
\** The TESCO Data transfer will require setting up an **RSA encryption** file and a **Biscom** account to enable data transfer.

The **Brandbank data** is held across all the TREs.

The three TREs also have a code share drive, which is used for code sharing across all TREs and can be accessed as the **W:** drive.  



When we have access to **Morrisons' system**, there may be a need to import additional data into their environment — **Brandbank data** and some **Geography data**. Morrisons has agreed to make provisions for this. The details of the data to be imported will be provided by the **DIO FOOD research fellow**. Examples of this can be found on `I:\P0455_allTREs`:

- `npm_calculator`
- `2024-06-17` (Geography data)
- `Brandbank`

Additionally, some code/scripts may be imported if necessary.
