# Demand Forecast modelling for Deputyship in OPG
This document serves as a user guide to the OPG deputyship Forecasting Model in Python, held in this repository: 
https://github.com/moj-analytical-services/OPG/blob/main/Deputyship_Data.ipynb

&nbsp;
&nbsp;

# Contents

* What the Demand Forecasting for Deputyship Model does
* Why the Demand Forecasting for Deputyship Model is useful
* How users can get started with the Demand Forecasting for Deputyship Model
* Where users can get help with Demand Forecasting for Deputyship Model
* Who maintains and contributes to the Demand Forecasting for Deputyship Model

&nbsp;
# [Demand Forecasting for Deputyship Model](#summ) - summary of the quantitative methods used for forecasting deputyships.  
&nbsp;   
# [Inputs](#inputs)
&nbsp;
# [Outputs](#outputs)
&nbsp;
# [Higher-level Process flow Diagrams](#high-process-flow) - proccess flow diagrames of main inputs/outputs for the Demand Forecasting for Deputyship Model.
&nbsp;
# [Aim](#aim) 
&nbsp;
# [Objectives](#objectives)
&nbsp;   
# [Background Knowledge](#Background)
&nbsp;
# [Control Assumptions and Sensitivity Analysis](#control-assumptions)
&nbsp;
# [Data Sources](#data-sources)
&nbsp;
# [Model Calculation](#calc-model) - details of model calculation
&nbsp;
# [Feature Engineering and Data Preparation](#preprocessing)
&nbsp;
# [Implementing the Demand Forecasting for Deputyship Model](#model) - details of model scripts
&nbsp;
&nbsp;
# __Technical Guidance__
&nbsp;
## [Getting started](#start)
&nbsp;
## [Running the model](#run-model) - step by step instructions
&nbsp;
## [Loading python packages](#pack)
&nbsp;
## [Setting up a Python virtual environment](#setup) 
&nbsp;
## [Analytical Platform (AP) and AWS S3 access](#ap-s3) - instructions on setting up AP and s3 access
&nbsp;
## [Accessing the model from Github and Error handelling solutions](#github) - Pulling the Income-Profile-Forecast-Model repo to your local area of the AP from GitHub
&nbsp;
# [Data Marts (the old Demand Forecasting for Deputyship Model)](#data-mart)
&nbsp;
# [How to Data Modelling](#howto-d-m) - Data Modelling using Create-a-Derived-Table (CaDT) 
&nbsp;
+ [*1 - Data Sources and Pipelines*](#0how2)
+ [*2 - Data Modelling using Create-a-Derived-Table (CaDT)*](#1how2)
+ [*3 - Lookup Tables (seed in CaDT)*](#2how2)
+ [*4 - Macros (macros in CaDT)*](#3how2)
+ [*5 - Running Updates*](#4how2)
+ [*6 - Connection with Python code in Jupyter Lab*](#5how2)
&nbsp;
# [Managing files on the Analytical Platform](#ap-detailed) - a detailed instructions on setting up AP, Git and s3 access
&nbsp;
# [Python libraries and versions](#pythobpack) - details of python version and package versions used
&nbsp;
# [Data setup](#data-setup) - step by step instructions Data Engineering in Jupyter Lab
&nbsp;
# [Exporting Output into CSV and Excel](#export)
&nbsp;
# [Evaluation of the model](#evaluation)
&nbsp;
# [Plotting The Forecasted vs Actual values](#plot)
&nbsp;
# [Process flow Diagrams](#processflow) - proccess flow diagrames of inputs/outputs for the pre-model and model, and the python function process flow 
&nbsp;
# [Parameters](#parameters) - model parameters explained
&nbsp;
# [Logging](#logging) - information about output and error logging
&nbsp;
# [Data Register](#data-register) - a link to the Model data register log
&nbsp;
# [Assumptions](#assumptions) - a link to the Model assumptions log
&nbsp;
# [Risks](#risks) - a link to the risk register log
&nbsp;
# [Quality Assurance (QA)](#qa) - directions to the folder that holds the logs and evidence of initial model v1 QA
&nbsp;
# [Future Development](#future) - instructions on how to do some potential model developments
&nbsp;   
# [Previous implementation of the model](#old-model) - instructions on how the previous model was implemented
&nbsp;  
&nbsp; 
&nbsp; 

<a name="summ"></a>
# Demand Forecasting for Deputyship Model
The forecast method used for the Demand Forecasting for Deputyship Model in summerised below:
- To estimate the the number of the active caseloads for those people who have got deputyships and their order status is still active, so they all subject to active supervision by OPG and provide forecast demands for the number of client under active supersion in 5-10 years. 

&nbsp;
<a name="inputs"></a>
# Inputs
1. The deputyships orders made for each individual cases by the Court of Protection from CASRAC and Sirius databases
2. Financial information for the deputyship demands for each indiviual/case
3. ONS polulation Projection (e.g., Mortality Rate)
4. Family Survay Data
5. Indidual information
7. Number of LPA application (to be suntracted for the polulation to provide number of deputyships)

&nbsp; 
<a name="outputs"></a>
# Outputs
1. Forecasted figures for those caseloads under active supervisons of deputyship 
2. Trends and pattern of new deputyship orders

&nbsp;
<a name="high-process-flow"></a>
# Higher-level Process flow Diagrams
The following image demonestrates a proccess flow diagrames of main inputs/outputs for the Demand Forecasting for Deputyship Model.

*under constuction!

&nbsp;  
<a name="aim"></a>         
# Aim 
- The aim of this project is to Automation, modernisation, and simplifying the current forecast model as well as migration and transformation of the related data and in the future moving modelling to the Analytical Platform. 
- This model should provide input for the OPG projects in term of resource managment (staff and income).
 
&nbsp;
<a name="objectives"></a> 
# Objectives
1. The current active caseload, i.e., those cases under active supervision
To estimate the number of the active caseloads for those people who have got deputyships and their order status is still active, so they all subject to active supervision by OPG and provide forecast demands for the number of client under active supersion in 5-10 years. So they are the people that well either be being charged a fee supervision of affair cases some of the well received full exemptions or missions but not all of them and that is one of the things that we need to try and forecast.

2. The trend in the number of new deputyship orders
The active caseload there is not a reason they need to forecast bar is because they obviously generating come from that. It the same time we need to forecast the numbers of new orders. It is a bit like the sort of stopped-flow module. In which, basically it is a bit like the bath where the active caseload is the bath of water when they got new orders (new cases deputyships) that are flooding into it.

&nbsp; 
<a name="Background"></a> 
# Background Knowledge

- The reason for forecasting is that OPG needs to estimate the income generated from their fees. In addition, it affects the balance between LPA fees and deputyship fees. The reason behind this is that one of tasks that OPG currently do is the deputyship is partly subsidised by the LPA fee so depending on what that kind of balance is and kind of how much they subsidise e.g., the deputyship fee. Also the other reason they need to forecast is because they need to make sure they hve got enough staff in order to bond supervise the 50,000 plus deputyships are kind of and under active supervision.

- The deputyships are made by the Court of Protection. It is usually cases where people cannot apply for a power of attorney so because they did not have one. There are three kind of way that we could get a deputyships: 
    1. Adults who lost their mental capacity because they did not have a power of attorney in which case the Court of Protection would order a deputy to act on your behalf.
    2. Adults who never had have mental capacity. They have some sort of disability or some mental disability but did not have the capacity to make power of attorney and again the Court of Protection can order a deputy to act on your behalf and often in this case might be a local authority.
    3. Childern born with a disability and they do not have anybody there especially make the Court of Protection to act on their behalf and have a deputyships. The deputyship can be a family member or power of atherney or local authority, financial advisor, and soliciter to act on behalf and mange their affairs. The difference in here is that the Court of Protection made the decision for ordering the deputyship and they do not have any choice about it.
    
&nbsp;    
&nbsp;

&nbsp;




## Deputyship Forecasting Model
Basically, the way the deputyships is forecasted is similar to a stopped-flow model, essentially we have got the active caseload in the middle, which is the kind of expert thank OPG synchronising it and we have got he got new cases flowing in aa new orders that the Court of Protection is making and then you got those cases that are terminated. They might terminate for a number of reasons, generally the people die and sometimes it might not be it might just simply be that the order is not renewed.  It is unlike the power of authorny which is lasting, e.g., if they have got a power of attheney unless they seek to remove that, which they can do e.g., if they divorced or just they do not want it anymore or their attorney dies or needed a new one. Thus, with the deputyship, they have to be renewed so the Court of Protection has to renew it and it has generally done about every three years. People could flow off the active caseload for number reasons: that is generally when people die but it could also be the court order is not renewed but you know the reasons why that would happen and they are pretty limited so this would normally give a deputyship to somebody unless they really lost capacity, so I suppose they could have a situation where somebody is in a coma or something else and when they recover and regain their consciousness or something else and then they do not need one anymore. Thus, they could have a situation like that and those cases that are flowing off and the balance between those cases coming on and those cases are flowing off is what is really the active caseloads in the middle. 

- **If we imagine that water is flowing out of the bath through the plug hole, that is what the termination date is showing. So we have these people here who had died and the death of clients mainly changed their status from Active to being Closed. So to work out the active caseload each year, we need to work out how many new cases are going to be added and how many cases are going to be terminated. Those are the two key things that we need to know and then we can run the model forward in that way. 

Here we break down how the stopped-flow technique can be related to the bathtub model and how it might apply to understanding and calculating the rate of new deputyships orders in the Office of Public Guardian (OPG) for active supervision with termination dates due to death or order closure. In summary, the stopped-flow technique and the bathtub model analogy provide insights into dynamic systems, whether in chemical reactions or administrative processes like managing deputyships orders. By applying these concepts, the OPG can better understand and manage its caseload, ensuring effective supervision and timely responses to changing circumstances.

### Application of Bathtub Model Analogy to OPG Deputyships Orders:
The bathtub model is a classic example of a dynamic system involving the flow of water in and out of a bathtub. We consider the following components:
1. Faucet: Represents the inflow of new deputyships orders (e.g., due to appointments, court decisions).
The faucet taps into an infinite source of new orders, similar to how the OPG receives new cases.

2. Drain: Represents the outflow of deputyships orders (e.g., due to death, order closure).
The drain removes orders beyond the system (e.g., due to death or closure).

3. Tub: Represents the total number of active deputyships orders at any given time.
The rate of flow through the drain depends on the size of the drain opening and the amount of water (i.e., active orders) in the tub.

The key points in modelling:
- More water in the tub (more active orders) leads to a greater rate of flow through the drain.
- The system is open, as ultimate sources and sinks (e.g., legal decisions, court rulings) are external to the OPG.
- Over time, the rates of flow and the number of active orders may change.
* Ref: https://www.mfpt.org/wp-content/uploads/2019/10/Heiser-Thomas-Bathtub-Failure-Distribution-MTBF-Paper.pdf

- Analogously, the OPG’s deputyship orders system involves a dynamic process where new orders come in (faucet) and existing orders are terminated (drain).

### Application of stopped-flow to OPG Deputyships Orders:
- Imagine using the stopped-flow technique to monitor the rate of new deputyships orders entering the OPG system.
- The “mixing chamber” in this case would represent the OPG’s processes for handling new orders.
- By observing the rate of incoming orders and the rate of terminated orders (due to death or closure), the OPG can calculate the net rate of change in active orders.
- This information is crucial for active supervision and resource allocation within the OPG.
- The analogy helps us understand how the system dynamics (flow rates, order numbers) impact the overall process.
* Ref: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_%28Physical_and_Theoretical_Chemistry%29/Kinetics/02%3A_Reaction_Rates/2.01%3A_Experimental_Determination_of_Kinetics/2.1.06%3A_Stopped_Flow
* Ref: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_%28Physical_and_Theoretical_Chemistry%29/Kinetics/02%3A_Reaction_Rates/2.01%3A_Experimental_Determination_of_Kinetics/2.1.06%3A_Stopped_Flow


It is exactly analogous to basically a bath that is being filled up with water with a tap, and water is flowing out of the bath at the same time. So what we have got is the active caseload, which is the water in the bath. The water that is flowing into the bath is the new deputyships. So these are the new cases that are being added to the active case load. So that is why we need to know to understand the trend in the active caseload is. So we can **predict how many new deputy ships they are going to be? What is the flow of water going to be into this bath over the next five years?** And that generally there has been the assumption built into the model, which is how it links to the LPA stuff. The rate at which new Deputyships are generated. Is is going to be related to how many people do not have an LPA. 

For the vast majority of people, a deputyship is generated because they do not have an LPA. It is not entirely the case because obviously you have children, so you have children under the age of 18 who could never take out an LPA, but that number is quite small. However, there might also be adults, who do not have mental capacity, who may be required to take out or have a deputyship once they reached the age of 80. 

&nbsp;
&nbsp; 
<a name="data-sources"></a> 
# Data Sources
The evidence is suggesting that the deputyship data is now being recorded in Sirius . Previously I had noted that deputyship “orders” had been recorded in the Sirius data that we received but this no longer seems to be the case, and what was recorded was not the level of detail previously available from CASREC (the database that previously captured deputyship data). 

For the previous data, please look at a file called “order1” derived from CASREC to give you an indication of the data fields actually required. What is needed is to obtain all of the data required to update the model.
 
We would need to find useful information like when the order was made whether it's still active or not and we could work out the age of a **P: Protective People**.

The data should enables us to work out what the size of the active caseload is but also to work out the termination rate, how quickly people flow off the active caseload, so this whole issue with mortality rates. The termination refer to those records whether somebody dies or just leaves but the order is just not renewed. Thus, we would need to bounce calculator as well and that was very age dependent, generally the younger somebody is that termination rate is going to be lower.


## S3 Bucket Access
Data from the current python script lands here: 
s3://alpha-opg-analytical/sirius_data_cuts_3/

## Current Python Script
https://github.com/moj-analytical-services/opg-data-processing/blob/sirius-prod/opg-analytical-endpoint-3.py


## Data Engineering Database Access 
-	sirius-prod (raw data, includes LPA and deputyship data), 
-	Solicitors Regulation Authority, 
-	curated data warehouse tables. 



## Deputyship Meta-data for the lagacy order data:

### The current CASRAC old Variables are listed below:
1. Create: date of order was placed.

2. Order No: a ref that the Court of Protection is using.

3. Case: a unique identifier for one person and should be for a specific individual (same dob and postcode).

4. AppNo: nuber of orders for an individual and so the corrsponding case number.

5. Ord Stat: Active/Closed

6. Ord Type: 

7. Desc: Order Descrption: Property & Affairs Deputy (Financial) / Replacement P&A Order / Interim P&A Order / Health & Welfare Deputy

8. Made Date:

9. Issue Date:

10. Caseload Date:

11. Sex

12. DOB

13. Postcode

14. Term Date

15. Term Type

16. Desc

17. Ord Risk Lvl: Order Risk Level: a risk assessment level of deputyships under active supervision 

18. Remis

19. Exempt

20. Exempt Desc

21. Award Date

22. Order Cnt


#### Desc (Order)
Order Descrption can be categorised in: 
1. Property & Affairs Deputy (Financial) 
2. Replacement P&A Order 
3. Interim P&A Order 
4. Health & Welfare Deputy


Example:

| Create     | Order No   | Case      | AppNo     | Ord Stat | Ord Type | Desc                   | Made Date    | Issue Date   | Caseload Date | Sex | DOB         | Postcode | Term Date   | Term Type | Desc | Ord Risk Lvl | Remis | Exempt | Exempt Desc | Award Date | Order Cnt |
|------------|------------|-----------|-----------|----------|----------|------------------------|--------------|--------------|---------------|-----|-------------|----------|-------------|-----------|------|--------------|-------|--------|-------------|------------|-----------|
| 17-Jun-11  | 00079746   | 10000037  | 2         | Active   | 40       | Replacement P&A Order  | 14-Jun-2011  | 17-Jun-2011  | 24-Jul-2006   | M   | 10-Jul-1977 | FY8 1PN  |             | 2         | 0    | 0            |       |        |             |            | 2         |


The deputyships are made by the Court of Protection, so they are not made through an application process like an LPA. So there is an order number and the order number is the court order number. We actually look at the physical court order. It would have that reference number on it, so an order was made. In fact, you can hear sorry jumping around. The main date, so this order was actually made on the 14th of June 2011, so there will be a court order made on the 14th of June 2011 for this person and the order number will be this 00079746.

It is like LPA data in the sense that if somebody might have the order of renewed, then there is going to be sort of multiple records, if you like through the data. An individual protetected person within the deputyship data and trying to tracking the people through the data. This might be alittle bit tricky to use kid of case numbers, so if the case for that individuals was closed in 2007 and become active in 2011. Thus, for some reason or other there was a replacement of a property and affairs. Therefore, the orders was at the sort of jusncture or order status. We are interested to find those orders that are active in OPG Supervision.

*Note: the case number should be used as a unique identifier for one person not the order number. The order number and case number should be for a specific individual (same dob and postcode). The order number is a ref that the Court of Protection is using.*

#### Term date
For example, when the Term date (termination date) is empty, this would suggest that this initial order made in 2006 and was never terminated. Then, for some reason or other, a replacement order was made in 2011. The assupmtion could be a reason they required a new deputy to act on their behalf. So they went back to the Court of Protection for an update to the deputieship order. 
But effectively what we can infer from this, assuming that these are just the two data points that we have for this person, this person with this case reference, is that the original order was made in 2006. And then it was updated in 2011, and that order has been in place. Subsequently, and so you know this data, I think was received in 2022. So this has been a long term deputyship order, so this is probably somebody has needed a deputy ship since birth, probably or since they were quite young. 


The termination date is not always filled by a date, the reason is there might be an active orders for this case. Therefore, we could sort the records to see if they are Closed because, there's been some amendment to the order, so there is not a termination date as the deputyship has not been terminated, the person has not died or anything like that. Therefore, the case has gone back to the Court of Protection. A replacement order has been made and in this case. As can be seen in the records for this person, there was a new property and affairs deputyship order was actually made in. There is also a whole history here for this person here, e.g., the order was originally made in 1996 and then it was a replacement order was made in 2010 and then again, a further order was made in 2018. So in fact there have been three orders in this particular individual's case, but the order has been live throughout this whole period. The Closed status in here simply refers to the fact that the previous orders are now closed and now this is the active order. 

Example:

| Create    | Order No | Case     | AppNo | Ord Stat | Ord Type                           | Desc                                 | Made Date  | Issue Date  | Caseload Date | Sex | DOB        | Postcode  | Term Date   | Term Type   | Desc   | Ord Risk Lvl   | Remis   | Exempt   | Exempt Desc      | Award Date | Order Cnt |
|-----------|----------|----------|-------|----------|------------------------------------|--------------------------------------|------------|-------------|---------------|-----|------------|-----------|-------------|-------------|--------|----------------|---------|----------|------------------|------------|-----------|
| 28-Sep-07 | 00000006 | 10001403 | 1     | Closed   | 1                                  | Property & Affairs Deputy (Financial) | 29-Oct-1996 | 29-Oct-1996 | 29-Oct-1996   | F   | 13-May-1965 | NG17 4BR  |             |             | 2      | 0              | 7       | Other not known | 01-Apr-2023 | 3         |
| 22-Sep-10 | 00068457 | 10001403 | 2     | Closed   | 40                                 | Replacement P&A Order                 | 16-Sep-2010 | 12-Nov-2010 | 29-Oct-1996   | F   | 13-May-1965 | NG17 4BR  |             |             | 2      | 0              | 7       | Other not known | 01-Apr-2023 | 3         |
| 30-Jan-18 | 00180158 | 10001403 | 3     | Active   | 1                                  | Property & Affairs Deputy (Financial) | 22-Jan-2018 | 20-Mar-2018 | 29-Oct-1996   | F   | 13-May-1965 | NG17 4BR  |             |             | 2      | 0              | 7       | Other not known | 01-Apr-2023 | 3         |


So there will only be a termination where there should be a termination date and all order should be closed. In this particular instance there is no previous history. So it seems that in this case the order was made in 1997. There were no revisions to that order over that period. There is no indication of any further orders being made. Simply the person either died in 2015 or rather, the deputy deceased, so the order came to an end. So in this case, the person did not die, the deputyship came to an end and the case was closed. So that is no longer a case that is under Active supervision and case is closed and there is atermination date on this record.


Example:

| Create    | Order No | Case     | AppNo | Ord Stat | Ord Type                           | Desc                                 | Made Date    | Issue Date   | Caseload Date | Sex | DOB         | Postcode | Term Date   | Term Type | Desc           | Ord Risk Lvl | Remis | Exempt | Exempt Desc     | Award Date  | Order Cnt |
|-----------|----------|----------|-------|----------|------------------------------------|--------------------------------------|--------------|--------------|---------------|-----|-------------|----------|-------------|-----------|----------------|--------------|-------|--------|-----------------|-------------|-----------|
| 28-Sep-07 | 00000011 | 10002199 | 1     | Closed   | 1                                  | Property & Affairs Deputy (Financial) | 17-Jan-1997  | 17-Jan-1997  | 17-Jan-1997   | M   | 25-Feb-1959 | ME10 4JA | 16-Jun-2015 | R         | Deputy Deceased | 3            | 0     | 0      |                 |             | 1         |


*Note: we can use the "Desc" variable and the "Term Date" to figure out the termination rates, i.e., how many people are flowing out of this bath.*

#### Desc (Termination) 

The descriotion of the termination can be categorised in the following terms:
1. Death of Client 
2. Deputy Deceased
3. Duplicate case
4. Deputy Discharged
5. Rule 24.5 clt regain capacity
6. No Further Proceedings
7. Deputy Suspended
8. Full Order Expired
9. Funds Exhausted
10. Order Revoked
11. Blank

Another reason that we cannot really just apply mortality rates (like LPA) is because, this is not like a random selection of the population. These are often people who Don't have capacity already? Extremely, they would not have the mortality rates of the population as a whole, but also there are other reasons why the case might be terminated, like in this case the deputy died.

### Ord Type
This is related to the Desc variable and categorised the description of the termination.

### Ord Risk Lvl
This refers to the Order Risk Level of deputyships, in which are under active supervision, and this is based on an assessment of the risk level, which is coded here are charged at two different rates:
1. The full what they call a general fee.
Currently 360 pounds a year.

2. A minimal fee level 
Currently, £32 a year.

- If the person has more than £30,000 in liquid assets, they would go into the higher general fee category. 
- If it's under 30,000, it would be the minimal fee. So that's a fairly kind of arbitrary cut off.
The reason for this is relevant to the questions raised before about whether that is a sensible cut off, or whether there should be any cut off at all? And there have been moves in the past to try to equalise those fees, so everybody pays the same.

This information of supervision in which OPG is derived variable and was collected from financial information about protected persons, which is just was not routinely collected within the old data (CASRAC). It also raised questions about how that was actually being assessed around the collected data to see if it was possible to distinguish Whether somebody was entitled to a remission or an exemption. This is because Because if they are in receipt of certain possible benefits, they would automatically get an A fee exemption. then the same way could be with powers of attorney. E.g., if their income was under a certain amount (12k a year) they would get a remission. Otherwise they would have to pay the full fee.
But that is only true for general fee payers. If they are a minimal fee payer, they either pay it or you get a full exemption. So there are all these kind of issues around, what benefits people get, what their income. That were very hard to deal with the data that exists.

**The deputyship model is set up, at the moment, to forecast the active caseload in total and the numbers of new deputyships. What it does not do is split that between the minimal fee payers and general fee payers and then further between who pays a full fee and who gets a remission or an exemption. This would give much more information about the likely income, that the OPG would generate from deputyships, and how that will be changing over time? So at the moment it only the model is only looks at the kind of high level numbers of active caseloads. It does not decompose that into these different groups. With a known population of people who pay rermissions and exemptions within general and minimal fees, and then age that over a 5-10 year period to see how that might change over that period of time. If OPG essentially reports that the number of general fee payers is going to decline and within that they likely to get an increase in the number of exemptions then obviously that means that the amount of income that they would generate would generate from that would be quite, all of that would be relevant to trying to answer policy questions about, how you might equalise fees as well.**

*Note: This required kind of **Family Resources Survey** to look at the kind of household income and family circumstances and the age of population, in order to be able to collect more information around the differences between minimal and general fee payers.

The deputyship model, at the moment, is essentially does it in exactly the same way as the LPA model. So, it is a basically applying survival rates to a kind of it takes the sort of the numbers of new deputyships by single years. Here and then it ages them each subsequent year in the model to kind of.
So if we sort of pick a pick a higher number down here, if we talk at say 66 year olds, you know each year the numbers drop because the expected number that are going to terminate in each of those years reduces that number so. Obviously that adds a level of complication to the model that might not be necessary. 

A simpler way to do this is, to add the number of new starters / new deputyships to the active caseload, and a simpler way to do it might simply be to say. And then simply each year, assume that a certain proportion, which we calculate from the termination rates to work out a percentage termination rate. 
Leave that population so we assume that, we add in 50 cases age 29 to the active caseload and we assume that 1% of those that population will terminate by the following year. And then so that updates it for the next year and then we do the same thing for the next year. So that gives you a new active caseload we add in what we expect the new cases to be that year and then we assume another 1% will terminate. Rather than the way we have done it, which is sort of try to work out sort of cohort based sort of termination rates. Our forecast of the caseload by, minimal, general and remissions / exemptions because those numbers are much smaller, it would be easier just to apply Percentage termination rates at each step in the process, rather than a cohort based model which would make it more complicated.
So instead of trying to say if we started with 1000 people, how many do we expect to die after one year, two year, three-year, four years and five years? Because we have a survival rate for that.
The simplest way to do it would simply be to say, if we have 1000 people aged, given a particular of a particular age, what proportion of those people would die next year? Age 26 and and we simply use that and then use that as the new total for that next age population.
We add in the new deputy ships and then, we say whatever percentage 1% die that year and again that we then update that to the next year increment.


### Ord Stat = Active/Closed

#### Active Caseloads (Under Active Supervision): Ord Stat = Active

1. When the order status (Ord Stat) is **Active**:
This is to answer the follwoing research question:
**1. The current active caseload ie those cases under active supervision**

So in other words, under active supervision by OPG and that is one of the things that we are trying to **forecast over the next sort of five to 10 years, how many active cases were there and how old are the people under active supervision?**

E.g., somebody was 20 years old when the original order was made, they've had an order for 15 years before they took before that order was terminated. So in other words, you can work out what is the probability that somebody aged 20 is going to have that order terminated after so many years.

This records are used to calculate how many active cases were there in the historical data. The the previous orders that were made is because what that tells you is when the original order was made and the reason that is useful is because you could then **cross reference that with the termination date**.

#### Trends in the number of new deputyship orders: Ord Stat = Closed

2. When the order status (Ord Stat) is **Closed**. 
This is to answer the follwoing research question:
**2. The trend in the number of new deputyship orders**

This records are used to calculate how old are the people under active supervision in the historical data. So in other words, we would need to work out how old the person was when.


In theory, these variables are used to identify all those cases with a complete record of all deputyships made, and you ought to be able to identify when the first order was made for that person, and in what year? So in other words, you ought to then be able to count how many new orders were made each year. The possible flaw with this has been, because there is often a delay in OPG recording in the legacy database (CASRAC), and when tried before with the current estimate of that figure, it is not clear how many order have been made in the last six months or 12 months for example, unless we have had to rely in the past on OPG giving us a separate account for that because it exists somewhere else on a separate database.

*Note: we would need to get the deputyships data updated and understand how currently being curated in Sirius?*

### Deputyship Sirius data

- For each client they should have their own caserecnumber (its also known directly as 'court number' in Sirius), multiple orders can be attached to each court number, but the earliest date for a given court number will give the first order. However, there is some vagueness over which date you choose as the 'start date', since there are multiple points when a date is recorded, e.g., made, issued, when opg assign a risk level etc.

- Look at the schema on Athena (CoP -> Sirius/OPG), you can add in fields that you want for each order/client. It's just a bit awkward, because orders and lpas share tables, i.e. orders are in the 'cases' tables as well as lpas. Thus, as the casrec migration wasn't particularly elegant, there are a lot of fields not relevant to each type of 'case', or fields that have similar names etc.

- The annual reports is supervision data, however, there isn't a derived table for caseload though, I think the plan is to basically create one at some point. OPG havent prioritised it, but the code will give you will basically be the similar logic to whatever the derived table uses.

- There was an issue in that digital didn't bring ALL data across to Sirius from Casrec, due to data retention laws, so any case where no action had been on that order for 7 years, those were effectively deleted

## Supervision caseflow report update
The follwoing text is written by Stuart Stach and I categorised the information he provided below: 
*Note: we would need to finalise the plan and objectives and get back to him.

- Missing Records (more dependence on CASREC migrated data):
we should be thresholding only clients which 'started' before the cut-off of the seven-year data retention period. This cuts out about half the clients, leaving just over 70k clients in the report. If that isn't ok with you, then I need to go back to digital and fully understand what data they DIDNT transfer from CASREC due to data retention policy. If we do include ALL clients going back to the start of supervisions then the below issues will be more substantial (more dependence on CASREC migrated data).

- Missing values (termination dates and Desc (reasons)):
There are still some clients that are missing termination dates and reasons, from both Sirius and the CASREC report I have access too. The number is small but if you think this will impact any modelling work, they should probably be manually checked - we can get Dawn or someone else from Research+Data at OPG to find term dates and reasons for these cases.

- Missing details on remission/exemptions ('Exempt Desc'):
There seems to be a lot of details on remission/exemptions that were being supplied by CASREC that I can't find in Sirius. If the 'Exempt Desc' column from the old CASREC report is important to you, then I'll go back to digital and see what is happening there.

- More information added, e.g., 'type' of the feepaying deputy (e.g. Pro/Lay/PA) and the 'client accommodation type' and their marital status, and 'from_casrec' flag (current work-in-progress):
For openness, I have uploaded a current work-in-progress copy of the excel output to an s3 bucket which I believe I have given both of you access to. This can be found here: 

**s3://alpha-opg-mi-dashboard/Supervisions/caseflow/supervision_clients_caseflow_20230403.xlsx

This excel sheet might be a bit hard to parse at first, since its currently containing a lot of unnecessary information. It does combine the Sirius data with the CASREC report I was provided for debugging. I have added in info for each client such as the 'type' of the feepaying deputy (e.g. Pro/Lay/PA) and the 'client accommodation type' and their marital status...I am sure there is more information that might be useful to you that could be found in Sirius. **Where the termination date and reason is taken from the CASREC data and not from Sirius there is a 'from_casrec' flag.

If you want to see how this sheet is being made, the code for it is currently at:
https://github.com/moj-analytical-services/opg-supervision-mi/blob/dev/client_caseflow.py

*Note: This isn't QA'ed yet but should give you an idea of the scale of the data that we have access to.


- For the more detailed description of the work (e.g., 'order_made_date' and 'Caseload Date'):
We can pull every supervision client that is currently in Sirius, and for each client we can look to see what are the earliest 'order_made_date' for any order that the client is attached to. This is the closest proxy I can find for the 'start' date and it does match the 'Caseload Date' that was being supplied by the CASREC report and thus I suspect consistent with how what you were previously using.

- Concerns regarding replicating a Casrec report on Sirius due to the data retention period rules:
As to which clients we could/should be pulling; Matt Machell has warned about attempts to replicate a Casrec report on Sirius due to the data retention period rules. Digital apparently didn't port over all data from cases which closed before that period. In the absence of an actual list of how and what data wasn't ported over due to data retention.... for now I've thresholded to clients which have their earliest order_made_date within the last seven years. As-of 3rd April 2023, thats about 70833 clients (cf 140461 total clients in Sirius), if more historical data is required we can go back to Matt and try to properly understand what Digital mean by: 'it had data in it that was beyond retention period so wasn’t brought across to Sirius and was just inconsistent.

- 'termination date' from the CASREC report and 'orderclosurereason' before and after migration:
In theory this is now supplied by looking to the status_date for the last order that gets closed and the termination reason from the 'orderclosurereason'. These seem to be consistently getting filled in for orders which are getting closed after the CASREC->Sirius migration but don't appear to be consistently filled for orders closed before the migration. Where the client died, this is less of an issue since death_confirmations/notifications HAVE transferred over (probably due to being stored in their own table) but that still results in ~500 or so clients being 'CLOSED' but with no termination dates or reasons (although unlikely to be due to death).

- Number of 'missing' clients's termination dates and reasons from within CASREC before it was shut down:
To try and mitigate this I have matched the old CASREC excel spreadsheet report that Daniel supplied to the Sirius output to see how many of these 'missing' clients have their termination dates and reasons from within CASREC before it was shut down. That excel report does supply termination dates and reasons for the majority of these 'missing' client termination's but there does remain **79 clients which are 'CLOSED' but there is no termination date or reason.** This is probably a small enough pool that somebody could manually check these court_numbers in the Sirius frontend and see when and why these clients became 'closed'.


- 'ACTIVE' client was set as deceased due to Deputy error:
Another fun issue is that I can see a number of clients which are 'ACTIVE' but apparently have a dateofdeath attached to them in. There were a couple more of these supposedly dead but active clients that I have manually cleansed because there was a note attached to their orders notifying the client was set as deceased due to Deputy error.... so it would seem that Sirius doesn't have the capability of removing erroneous death notifications? either way, in the spreadsheet I have supplied, there are **13 ACTIVE clients with termination dates due to client being dead...these might not be correct and should probably be manually checked along with the 79 clients with no termination reason.**

&nbsp;


<a name="control-assumptions"></a> 
# Control Assumptions and Sensitivity Analysis

* ref: SUPERVISION CONTROL ASSUMPTIONS (tab) in the excel model

The number of the deputyship cases should be equivalent to the subtracted the LPA number of the LP as from the population. So that is why we are subtracting the number, the cumulative total number of people, that have an LPA from the population, because that then tells us **what is the population at risk of needing a deputyship and how likely it is to generate a new, and at which rate?** e.g., if we know the rate in whitch from 100,000 people without an LPA generates 20,000 deputyships, we can work out what that rate is and how that rate is changing over time, as can be seen in the control assumptions. So the assumption is, if we dropped from 100,000 people without an LPA down to 50,000 people without an LPA, then we would expect the number of new deputyships to drop as well because the the population at risk of needing an LPA is less.

To find out what data is available and how to access that we need to dig into new data to populate the model.

To simply the model, as there's a lot of redundancy in the excel model as there is as there was with the the LPA

The current model is expressing the numbers of new deputyship, this is trying to work out numbered of deputyship orders as a rate 1000 of the population without an LPA. 

The model is also looking at whatever the trend was in deputyship orders and calculating that as a rate per thousand population without an LPA.

In most the cases, the trend of deputyship orders is generally going down. An explanation for this could be based on the assumption at the time (although we did not really know what happened subsequently) because more of the population of got LPA's that number is such a growing each year and it would reduce the population at risk of needing a deputyship. Therefore, we would expect the numbers of deputyship for the remaining rate is to go down.

*Note: We would need to adjust these control assupmtions and play around with what looks like a set of four sensitivity tests.*

Manily on this controller is really what the key survival rates when we have got the deputyship data we can work now what are termination rates, when the order was made when somebody left the active caseload and on other orders were made and we can work out the period of time and how old they were when the order was made and when the case was terminated. In other words, we can work out what is the termination rate and it is a bit like mortality rate. So we can see the order that those termination rates tend to increase. 

Initially, it then sort of reflects something about the difference in the type of population because somebody in their 50s or 60s requiring a deputyship, probably because they have had an accident or something and they may be quite ill and so it's likely that they died quickly whithin the order was made. However, in some other reasons, they might have lost their mental capacity through dementia illness, thus, that was not terminal then there would live and bunch of other people who would survive for many years. Also, there are people who have had their deputyship for decades.

Because of these difference between cases, it could be very difficult to apply sort of simple mortality rates (as we did in LPA) to this deputyship dataset, because it's not the same sort of population.

We could simplify the model, so rather than putting such complexity of this a bit and made this a bit too complicated whereas the model, at the moment, tries to again treat the data as a cohort type of way where we sort of terminate people turning on their age overtime, 

but in reality it might be better as there is an argument that we could look a simple age-specific termination rate as that is not time-dependant, e.g., we simply consider if somebody is aged 50 or 60, what percentage of them terminate in any one year, rather than doing it in the sort of the cohort-based fashion and the reason for doing that might be that we could then track them over time better, so we can look if there are trends in the sort of termination rates which is much harder to pick out if we do it in this sort of cohort type of way so again there's sort of room for simplification in this.


*Note: We would need to work out what volumes of active caseload terminations that deputyship has.*

We are trying to forecast new deputyship and the active caseload, to forecast the new deputyship before we can forecast the active case we need to know how many active so how many new deputyship are gonna flow into the active caseload.


Basically, the starting point is the population forecast, so this is the population minus living LPA holders so this is the whole point of calculating how many living LPA holders there are so for anybody aged 18+. It is basically taking the population and subtracting from it what the current estimate for the number of living out LPA holders is and what is the relevance of forecasting and the number of living LPA holders, because this is obviously starting from 2018 but we would need to update this.

The LPA model is making a forecast of how many living LPA holders, so there will be obviously future LPA holders, so over time the numbers obviously changes if the number of LPA changes.

Another assumpotion is that there is no record for anyone under the age of 18 and that's because there are no LPA holders under the age of 18 or they shouldn't be that might be something or erroneously given at a younger age but that should not be correct so there should be none.

This part of the assupmtion worksheet is simply taking that information about LPA holders minus living MBA holders and then categorising them into age groups, e.g., the population 18 plus/minus living LPA holders sort of categorised by age and the reason for doing that is because it is obviously trying to build some control assumptions around deputyships as a proportion of remaining people without an LPA and break that down some age categories as it is been very hard to do it by single year of age.

Thus, this is a summary of the numbers of new deputyships each year by age group and this is really a summation of those two sheets, which Paul was using to try to estimate some of these figures, where we be good to kind of find out what the current status of the data is and whether it includes better historical data, so do we just need to rely on the information that we had after 2019 and we are just park that and added new data then or actually do we have that historical data now, so it might mean that we just need to park this historical data and then kind of add on to it if we have got new data since 2019 yeah, we could review this once we have been able to kind of review the status of the day.

To date this is a sort of summation of new deputyships orders, that there are obviously under the age of 18 are less than 200, which is not a large number, as it is the mother or obviously children born who need deputyships and volumes tend to increase with age, the same way that kind of LPA do. 

As can be seen, there is a bit of a bimodal peak in the sort of 18 to 24, that may be partly due to risky behaviour, but it also could be whether one of the very first things the soldiers join the forces in the UK is that they are required to fill out their well and power attorney because if they go into a compat zone and injured or died or they might lose mental capacity, so they need somebody to act on their behalf and if they do not do that then obviously that might require them to have deputyship as well so that may be why there is also a peek here. However, in fact that we know 18 to 24 year olds often show more risky behaviour that is why they are in a group that has the highest accident rate with driving. For example, they do crashed their car and they had a brain injury such that they are going to require deputyships as can been seen in the figures. 

The model, the essence of the way it works is a basic assumption that if they have a power of attorney they do not need a deputyship and when they do not have a power attorney, they are at risk of needing a deputyship.  That assumptions is probably reasonable for most deputyships. Having said that, it does not cover every cases because it does not cover for those adults who could never get a power attorney so they are then at risk of needing her attention or for those children because they could never have a power of attorney as well in both cases they tend to be younger so again unlike power of attorney which tend to be very skewed towards older people. However, you could see the same sort of similarity in deputyships as well that they tend to be much older because most of the cases are people who have already taken out a deputyship but it is a bit bimodal as we could get a lot of deputyships for younger adults and not so many children. Thus, there is a bit of bimodality in there as well simply because and others younger people do nt have power of attorney often said of engaging more risky type behaviour OK I can binding motorbikes or jumping out aeroplanes or something and so berries he got a bit of bimodality around people are kind of in their early 20s because they had some sort of injury or life limiting injury that means they also require a deputyship.  The way the model is working at most cases is simply trying to obtain that estimate of how many living people have got power attorney away from the subtract that from the population to work out what is the population that do nt have have a power attorney and therefore might be at risk of needing a deputyship and in the other cases for the younger groups, and for the children, it it just sort of naive extrapolation. 

Essentially all what is happening in the charts is to work out how many deputyships are here as a ratio or percentage of rate compared to the number of non-LPA holders and this information is used in the controlled assumptions. Then, to generate a forecast for the number of new deputyships per 100,000 of the population without an LPA. Thus, if we generate that as a rate then could apply that for the LPA to create forecasts of the size of population without an LPA. We have got rate and population to be multiplied with each other in order to estimate the number of new deputyships. For instance, if there are estimsting that there would be four new deputyships in 2030, 100,000 of polulation without LPA, thus, we can work out how many new deputyships we expecting in 2030 and how many left without LPA? 

In fact, for childern up to age 18 is more a nive extracolation of this figures and not worth doing much more coplicated work on that, as the number are very small and so it is a simple exponential smoothing forecasting.

&nbsp;
&nbsp;
## ######################################################################## ##
&nbsp; 
<a name="calc-model"></a> 
# Model Calculation - details of model calculation.


&nbsp; 
<a name="preprocessing"></a> 
# Feature Engineering and Data Preparation


&nbsp; 
<a name="model"></a> 
# Implementing the Demand Forecasting for Deputyship Model - details of model scripts.


&nbsp;
&nbsp;
&nbsp;
&nbsp;
# __Technical Guidance__
<a name="start"></a> 
## Getting started

&nbsp;



&nbsp;
<a name="run-model"></a> 
## Running the model
- step by step instructions

&nbsp;
<a name="pack"></a> 
## Loading python packages

&nbsp;
<a name="setup"></a> 
## Setting up a Python virtual environment

&nbsp;
<a name="ap-s3"></a> 
## Analytical Platform (AP) and AWS S3 access
- instructions on setting up AP and s3 access

&nbsp;
<a name="github"></a> 
## Accessing the model from Github and Error handelling solutions
- Pulling the Income-Profile-Forecast-Model repo to your local area of the AP from GitHub

&nbsp;
<a name="data-mart"></a> 
# Data Marts (the old Demand Forecasting for Deputyship Model)

&nbsp;
<a name="howto-d-m"></a> 
# How to Data Modelling
- Data Modelling using Create-a-Derived-Table (CaDT)


&nbsp;
<a name="0how2"></a> 
+ *1 - Data Sources and Pipelines* 

&nbsp;
<a name="1how2"></a> 
+ *2 - Data Modelling using Create-a-Derived-Table (CaDT)* 

&nbsp;
<a name="2how2"></a> 
+ *3 - Lookup Tables (seed in CaDT)*

&nbsp;
<a name="3how2"></a> 
+ *4 - Macros (macros in CaDT)*

&nbsp;
<a name="4how2"></a> 
+ *5 - Running Updates*

&nbsp;
<a name="5how2"></a> 
+ *6 - Connection with Python code in Jupyter Lab* 



&nbsp;
&nbsp;
&nbsp;
<a name="ap-detailed"></a> 
# Managing files on the Analytical Platform
- a detailed instructions on setting up AP, Git and s3 access

&nbsp;
<a name="python-pack"></a> 
# Python libraries and versions 
- details of python version and package versions used

&nbsp;
<a name="data-setup"></a> 
# Data setup
- step by step instructions Data Engineering in Jupyter Lab

&nbsp;
<a name="export"></a> 
# Exporting Output into CSV and Excel

&nbsp;
<a name="evaluation"></a> 
# Evaluation of the model

&nbsp;
<a name="plot"></a> 
# Plotting The Forecasted vs Actual values

&nbsp;
<a name="processflow"></a> 
# Process flow Diagrams
- proccess flow diagrames of inputs/outputs for the pre-model and model, and the python function process flow. 

&nbsp;
<a name="parameters"></a> 
# Parameters
- model parameters explained

&nbsp;
<a name="logging"></a> 
# Logging 
- information about output and error logging

&nbsp;
<a name="data-register"></a> 
# Data Register
- a link to the Model data register log

&nbsp;
<a name="assumptions"></a> 
# Assumptions
- a link to the Model assumptions log

&nbsp;
<a name="risks"></a> 
# Risks
- a link to the risk register log

&nbsp;
&nbsp;
<a name="qa"></a> 
# Quality Assurance (QA)
- directions to the folder that holds the logs and evidence of initial model v1 QA

## Data Quality Assurance

### AQA Template
https://aqa-website.apps.live.cloud-platform.service.justice.gov.uk/tools.html

*Note:Data and Analysis have just relaunched their website and are changing the AQA process, so this is likely to change. 

### OPG Internal Checks
We usually provide samples of our tables in CSV format for the OPG data team to manually check accuracy and flag data issues. I strongly recommend including these checks in your AQA because there are lots of problems with the data which vary by business epoch. For that I would contact Mandy directly when you have a table which is ready for use. 

### Ethics Assurance Template
Our team currently use this template from the UKSA: 
https://uksa.statisticsauthority.gov.uk/the-authority-board/committees/national-statisticians-advisory-committees-and-panels/national-statisticians-data-ethics-advisory-committee/ethics-self-assessment-tool/
MoJ have been working with the Alan Turing Institute for a while on reissuing the MoJ ethics assessment, but I’ve not been able to find anything hence defaulting to the UKSA version. 

&nbsp;
<a name="future"></a> 
# Future Development 
- instructions on how to do some potential model developments


&nbsp;
<a name="old-model"></a>   
# Previous implementation of the model 
- instructions on how the previous model was implemented


&nbsp;  