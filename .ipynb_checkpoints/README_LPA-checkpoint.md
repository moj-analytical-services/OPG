# Demand Forecast modelling for LPA in OPG
This document serves as a specification documentation and user guide to forecasting model for Living Power of Attorney (LPA) applications in the Office of the Public Guardian (OPG) implemented in jupter lab, excel, and held in this repository: 
https://github.com/moj-analytical-services/OPG/blob/main/LPA_Data.ipynb

&nbsp;
&nbsp;

# Contents

* What the Demand Forecasting for LPA Model does
* Why the Demand Forecasting for LPA Model is useful
* How users can get started with the Demand Forecasting for LPA Model
* Where users can get help with Demand Forecasting for LPA Model
* Who maintains and contributes to the Demand Forecasting for LPA Model

&nbsp;
# [Demand Forecasting for LPA Model](#summ) - summary of the quantitative methods used for # Short And Long Term Demand Forecasts for LPA.  
&nbsp;   
# [Inputs](#inputs)
&nbsp;
# [Outputs](#outputs)
&nbsp;
# [Higher-level Process flow Diagrams](#high-process-flow) - proccess flow diagrames of main inputs/outputs for the Demand Forecasting for LPA Model.
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
# [Implementing the Demand Forecasting for LPA Model](#model) - details of model scripts
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
# [Data Marts (the old Demand Forecasting for LPA Model)](#data-mart)
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
# [Previous implementation of the model](#old-model) - instructions on how the previous model was implemented
&nbsp; 
# [Future Development](#future) - instructions on how to do some potential model developments
&nbsp;    
&nbsp;
# [Managing files on the Analytical Platform](#ap-detailed) - a detailed instructions on setting up AP, Git and s3 access
&nbsp; 
&nbsp; 

<a name="summ"></a>
# Demand Forecasting for LPA Model
**Lasting Powers of Attorney (LPAs)**:
   - **Definition**: LPAs are legal documents where an individual (the donor) nominates someone (the attorney) to make decisions on their behalf if they lose mental capacity.
   - **Creation**: LPAs are set up while the donor still has mental capacity.
   - **Types**: There are two types of LPAs: one for financial decisions and another for health and care decisions.
   - **Flexibility**: LPAs offer flexibility, allowing individuals to choose and trust their attorneys.
   
The forecast method used for the Demand Forecasting for LPA Model should be able to estimate the the number of the active caseloads for those people who have got LPAs and their order status is registered by OPG and provide forecast demands for the number of LPA demands in 5-10 years. 


&nbsp;
<a name="inputs"></a>
# Inputs
1. The LPAs orders made for each individual cases by the Court of Protection from CASRAC and Sirius databases
2. Financial information for the LPA demands for each indiviual/case
3. ONS polulation Projection (e.g., Mortality Rate / Survival Rate)
4. Family Survay Data
5. Individual information
7. Number of LPA application

&nbsp; 
<a name="outputs"></a>
# Outputs
1. **Short Term LPA Forecast**: 
    - projections of 12 months or less of LPA applications received and numbers registered as a month profile. 
    - Frequency (to be agreed). Supports long term forecast.

2. **Long Term LPA Forecast**: 
    - It is necessary to forecast LPA income, and forecast trends in deputyships an investigations. 
    - Long term projections (5 years +). 
    - Annual numbers of LPA applications received and registered with uncertainty ranges. 
    - Frequency: Annual updates.

&nbsp;
<a name="high-process-flow"></a>
# Higher-level Process flow Diagrams
The following image demonestrates a proccess flow diagrames of main inputs/outputs for the Demand Forecasting for LPA Model.

*under constuction!

&nbsp;  
<a name="aim"></a>         
# Aim 
- The aim of this project is to Automation, modernisation, and simplifying the current forecast model as well as migration and transformation of the related data and in the future moving modelling to the Analytical Platform. 
- This model should provide input for the OPG projects in term of resource managment (staff and income).
- The main aim of this work is to work out how many people applied for LPA and recieved the power of atthorney and how many applications in a year/month/week by age group since 2007 ages over 19 years old.

&nbsp;
<a name="objectives"></a> 
# Objectives
1. Forecasted figures for Living LPAs 
2. Trends and patterns of the LPA orders
3. Data modelling (Dimentional Modelling in CaDT)


## Business Needs
- Analytical resource is required to support OPGs plans to develop a fully digital LPA. Specifically: 
    1. To explore what impact, under a range of options, would fully digital LPAs have on overall demand?
    2. What will be the residual need for paper applications?
    3. What impact will fully digital LPAs have on LPA demand across a range of protected characteristics  
- Long term forecasts support OPG income forecasts, fee setting and broader strategic decisions and business objectives. 
- Short term forecasting is a critical function supporting plans for resources needed to handle applications and  calls etc and in-year monitoring of external impacts particularly around broadcast / media events, and early indications of the impact of marketing events.


## Key Deliverables
1. Adaptation of the long term and short term LPA forecasts to include scenario based assumptions on how fully digital LPAs will impact on LPA take-up. These scenarios will also Impact on Deputyship and Investigations Forecasts.

2. Forecasts of future applications by type (fully digital, and paper) including residual numbers of paper applications

3. Background analysis of online applicants to inform assumptions on digital take-up (see what has been achieved so far). Integration with work by Lisa Moretti (OPGs Digital Sociologist) and Behavioural modelling.

*Notes:
1. Need to work closely with Jude Rattle (OPG/MOJ Digital), Samera Aslam, and Mandy Roper
2. Recent improvements making records of online applications mandatory within Sirius will help significantly with this (however, this also limits analysis of historic data. 



*Note:* 
The links to the workshop presentation slides as this may provide some further context:
https://justiceuk.sharepoint.com/:x:/s/MLPAModelOfficeDatarequirements/EQlqQ6r-a3NOm_9mSKlhd2gBmA9PUDMy0tjOyP-yxvK3dQ?CID=0815868E-19DB-4742-A5E3-2552C35614D2&wdLOR=c754D2377-1644-496B-A2FE-3C389D82AFA6 

https://justiceuk.sharepoint.com/:p:/s/MLPAModelOfficeDatarequirements/Eb-Tacu42N9Cq6TDk2oRgRIBDMa3Q0wTSEUa02VrzpmGKg?CID=CBF3B356-D9AE-4AD8-BE69-BDAB70A97D69&wdLOR=c5BF25DD4-1AE4-4375-8564-951C3018AA71

Please note that individual data points have not yet been identified and will be our next step in this process (along with understanding which data tables/source these data points sit).
In the spreadsheet the green tabs were from the workshop – the information has collated into a summary tab which is easier to navigate (blue tab), so I would advise you to refer to the summary tab (the green tabs hold further information/discussion points for each of the data requirements – these may help understanding (the summary tab contains links to these). 

## FULLY DIGITAL LPAS - Development Work
1. Develop assumptions for the impact of fully digital LPAs on the long term LPA forecast under a range of options. See project notes on FULLY DIGITAL LPAs.
2. Extend forecast of the impact of fully digital LPAs on demand to impact on deputyships and investigations.
3. Explore potential improvements to assumptions on the risk of investigations . See project notes on INVESTIGATIONS: Developing Insights and Practical Applications To Improve Safeguarding. 
4. Update to Missing Persons Deputyships.
5. Build insights on OPG Customer Segmentation Forecasts into Long Term LPA Forecast.
6. Develop geographic LPA demand forecasts.

## Modernising LPAs
- This policy change will transform how customers purchase LPAs and how the OPG interacts with them.
- Long-term strategic concerns include assessing the impact on overall LPA demand and adapting to changing circumstances.
- This will be a major change in how customers will be required to purchase an LPA and how OPG interacts with customers in the future.
- Again it is hard to summarise such a complex policy effect but some of the long term strategic concerns might be: 
    - How this will impact overall LPA demand in the longer term; plausible arguments can be made for demand increasing (assuming LPAs are made more accessible eg not requiring a printer) or reducing (where digital capability or need to employ a solicitor becomes an issue). It would probably be best to characterise the potential impact on LPA demand as highly uncertain. 
    - Following the uncertainty in demand , would be uncertainty around income and how OPG plans for this , and what impact this might have on fees for both LPAs and Deputyships in order to rebalance its books.
    - Whether MLPAs are compatible with the broader aim of widening the appeal of LPAs; this has not really been tested (I think ?). 
    
### Ongoing Development
1. Invest in automating, data modelling, improving data pipelines to improve data quality and timeliness
    - Optimise the SQL scripts and use Parallelisation in CaDT
    - The intention of the data modelling work we’re doing with OPG is that we can create a data warehouse which consolidates all the different processing that’s done across different teams into a single set of tables that are available to the whole organisation.
   
2. To support work on the impact of fully digital LPAs it would be useful to additionally explore: 
    - If the rollout of the online tool increased LPA take-up (i.e., was there a digital dividend)? 
    - Can digital services provide a way to access harder to reach customers ? Where might changes to digital access be needed? 
    - What might be potential barriers to access ? (e.g., noteable low use in rural areas).
    - Incorporating Covid period uncertanties around data and how to apply this to the cohort model for forecasting LPA?
    
3. Automate models 
    - Quicker, more flexible models in AP 
    - Review models and improve methodology 
    
4. New tools, models and products 
    - Investment in wider portfolio of products and tools to deliver insight/analysis and to improve modelling  
    
5. Wider Modelling Hub vision
    - Contribute to delivery of wider modelling hub vision
    - maximise benefits from the hub, in particular  


## POTENTIAL UNMET NEED FOR LPAS
- Highlights specific geographic areas where LPA take up is low and indicators of potential need for an LPA, such as high dementia prevalence, are relatively high.
- Conclusions on high levels of unmet need depend strongly on how potential need is defined . Focusing on specific conditions such as dementia and stroke tends to locate areas of highest unmet need within urban ethnic diverse and often low income areas , whilst using age as the key indicator tends to locate most unmet need in coastal locations. Currently OPG comms have tended to target areas with higher numbers of lower income ethnically diverse communities.
- A more general finding from this research was that the higher the level of potential unmet need within communities the more different these communities look when compared with existing OPG customers.    

## Potential Unmet Need for LPAs
- Geographic disparities exist in LPA uptake. Some areas have low adoption rates, while others show indicators of potential need (e.g., high dementia prevalence).
- Defining potential need varies: Focusing on specific conditions (like dementia) or using age as an indicator leads to different conclusions.
- Existing OPG customers differ from communities with higher unmet needs.

### REMISSIONS AND EXEMPTIONS FOR FEES
- The OPG means test has not been updated for more than a decade; attempts to update it previously have proved problematic for a variety of reasons;
    - The current test is incredibly simple and highly unusual in that it is an assessment of individual financial circumstances rather than joint / benefit unit level circumstances. Attempts to update the test particularly for Supervision to allow for protected persons with low income but high levels of capital have necessitated making the test more complex which have raised both practical  and legal issues about consistency with the Attorney scheme.
    - Changing the test will have an impact (potentially negative) on OPGs income adding to the uncertainty around income . But if OPG wants to make LPAs more accessible to a wider range of customers then it will also need to increase take up of the remissions and exemptions scheme.
    - OPG does not collect sufficient information on its customers to adequately test options for updating the remissions and exemption schemes for LPAs or Deputyships.  
- The quality of the data collected on the existing remissions and exemption schemes is uncertain ; this is suggested by the proportion of donors claiming exemptions which is extremely low. 

### SUPERVISION AND LPA FEES
- Attempting to correctly balance Supervision and LPA fees over the longer term will depend on much of what has been suggested above particularly changing LPA demand , income , impact of MLPAs, any planned changes around remissions and exemptions, the success or otherwise of making LPAs more widely accessible and the impact on income, and specific decisions such as the level of cross-subsidy .
- Another significant factor is the cost of Investigations (see below) .

### INVESTIGATIONS  
- Whilst we are in the process of updating this forecast , it is reasonable to say that the number of investigations that OPG will need to deal with will continue to rapidly increase for two reasons:
    - The proportion of living LPA holders will continue to increase and generate more concerns
- The proportion of those with LPAs where the LPA is actually in use will continue to increase as the age of living LPA holders increases. 
    - Whilst numbers of investigations will increase these remain a very small percentage of the overall number of living LPA holders relative to comparable figures on elder financial abuse produced by Age Uk etc.  This itself may be a concern as this may indicate that a large amount of abuse goes undetected. 
- It is unclear what impact MLPAs will have on investigations.
- Should reducing investigations / safeguarding concerns be a strategic concern ?

### FORECASTING LONG TERM LPA DEMAND
- This is difficult but necessary. 
- Strategically it is useful to understand the causes of uncertainty and risks around LPA demand.
- Current horizon scanning tries to reflect both the impact and probability of events on LPA demand . Currently three events are identified as having the potential to have a large impact on LPA demand with a high probability in the short to medium term; these are MLPAs, Suppressed demand due to the pandemic and the cost of living crisis. 
- Other potential risks to LPA demand and OPG more generally might include:
    - Cyber Risk, generally or more specifically on Government Systems including OPG systems. Risk likely increased with MLPAs, AI and broader geo-political events.
    - Evidence of LPA market saturation becomes more pronounced 
    - Worsening of geo-political events and disruptive impact on the UK economy worsens the current cost of living crisis reducing LPA demand.
    - There is always an increasing risk of unknown unknowns. 

&nbsp; 
<a name="Background"></a> 
# Background Knowledge

## What has been achieved so far?  
1. We have previously been asked to develop scenario based forecasts for the take-up of online LPAs under a range of alternative assumptions. 
2. To support the consultation on modernising LPAs we have explored patterns in take-up of online applications. 

### Implications of modernising LPAs
Modernising Lasting Powers of Attorney (LPAs) can have significant implications for both individuals and the Office of the Public Guardian (OPG):

1. **Accessibility and Ease of Use**:
   - **Positive Implication**: Modernisation aims to make LPAs more accessible and user-friendly. Simplified processes, digital platforms, and clearer guidance can encourage more people to create LPAs.
   - **Challenges**: Ensuring that the modernised system accommodates diverse needs (including those of older adults and people with disabilities) is crucial.

2. **Increased Adoption**:
   - **Positive Implication**: Streamlined procedures may lead to increased adoption of LPAs. More people will proactively plan for their future decision-making.
   - **Challenges**: Raising awareness about the importance of LPAs remains essential. Many individuals still lack information about their benefits.

3. **Cost and Affordability**:
   - **Positive Implication**: Modernization could potentially reduce administrative costs, benefiting both users and the OPG.
   - **Challenges**: Balancing affordability while maintaining the quality of service is critical. Some individuals may still find fees prohibitive.

4. **Digital Transformation**:
   - **Positive Implication**: Digital platforms allow online creation, registration, and management of LPAs. This convenience can encourage more people to engage.
   - **Challenges**: Ensuring data security, privacy, and accessibility for all, especially those without digital literacy, is essential.

5. **Efficiency and Timeliness**:
   - **Positive Implication**: Streamlined processes can expedite LPA creation and registration.
   - **Challenges**: Managing increased demand efficiently and avoiding delays in processing are key considerations.

6. **Monitoring and Oversight**:
   - **Positive Implication**: Modernization can enhance oversight, ensuring attorneys and deputies act in the best interests of the person they represent.
   - **Challenges**: Balancing oversight without creating unnecessary bureaucracy is crucial.

7. **Legal Clarity and Consistency**:
   - **Positive Implication**: Clearer guidelines and standardized practices can improve consistency.
   - **Challenges**: Ensuring that legal changes align with societal shifts and evolving needs is essential.

8. **Impact on OPG Resources**:
   - **Positive Implication**: Efficient processes may allow OPG staff to focus on critical casework.
   - **Challenges**: Adequate staffing and training are necessary to handle increased demand and address complex cases.

In summary, modernising LPAs presents opportunities for better accessibility, efficiency, and user experience. However, addressing challenges related to awareness, affordability, and equitable access remains crucial. The OPG must strike a balance between innovation and maintaining its core mission of safeguarding vulnerable individuals. 

    
## Useful Contacts
The OPG’s strategy team prepare OPG’s overarching 3-5yr strategy, the first phase of which is collecting a range of evidence. 
Provide documentation that outline analysis on unmet need, fees, horizon scanning etc. 
Sam Cuthbertson (sam.cuthbertson@hmrc.gov.uk) in HMRC: Lisa Barret: Director at GDS
DWP (need contact) rollout of digital services e.g., carer allowance

## Why Don't People Take Out LPAs?
- Reasons are multifaceted and complex.
It is difficult to summarise this but it is clear that the reasons are complex and multifaceted.
- Factors explored include age, ethnicity, geographic location, household income, mental health status, awareness, digital capability, and access to services.
Factors that have been explored for which there are plausible explanations include age, ethnicity, geographic location , household income / wealth status, physical and mental health status, awareness and responsiveness to information, digital capability and access to services,  Isolation not just geographically but within communities.
- A behavioral model suggests that taking out an LPA depends on four conditions: Need, Drive, Awareness, and Accessibility.
A simple behavioural model to help understand why people don’t take out LPAs might summarise the decision purchase an LPA is dependant on 4 key conditions being met ; Need , Drive,  Awareness and Accessibility. The paper summarises this as a Venn Diagram.

## What happens if I don't have an LPA?
1. **Loss of Decision-Making Control**:
   - Without an LPA, you won't have designated attorneys to make decisions on your behalf if you become mentally incapacitated.
   - Critical decisions related to your finances, health, and welfare may be left unresolved.

2. **Court-Appointed Deputyship**:
   - If you lack an LPA and lose mental capacity, someone (usually a family member or friend) may need to apply to the Court of Protection to become your deputy.
   - The deputy will have legal authority to make decisions for you, but this process can be time-consuming and costly.

3. **Limited Autonomy**:
   - The court-appointed deputy may not always make decisions aligned with your preferences or values.
   - You lose the autonomy to choose who represents you during incapacity.

4. **Financial and Legal Challenges**:
   - Managing your financial affairs becomes complicated without an LPA.
   - Accessing bank accounts, paying bills, and handling property matters can be challenging.

5. **Healthcare Decisions**:
   - Without a health and welfare LPA, medical decisions (such as treatment options, care preferences, and end-of-life choices) may be made by healthcare professionals or family members without your input.

6. **Risk of Delay and Disputes**:
   - If disputes arise among family members regarding decision-making, the court may need to intervene.
   - This can lead to delays and emotional strain during an already difficult time.

7. **Costs and Burden on Loved Ones**:
   - Applying for deputyship involves legal fees, court costs, and ongoing supervision fees.
   - Loved ones may bear the burden of managing your affairs if you lack an LPA.

In summary, having an LPA ensures that your wishes are respected even if you lose mental capacity. It provides peace of mind and empowers trusted individuals to act on your behalf. 

&nbsp;
&nbsp; 
<a name="data-sources"></a> 
# Data Sources

- The complete LPA database to 18th March is located here in 10 csv files . The newest data is contained in part 10 and the oldest on part 1 etc.
- The old data was located in Dom1: S:\hq\102PF\Shared\CJG\FMDU\Data Share Area\OPGDOCS\LPA Data\LPA Data To March 2024

## Meta data and Variable selection and Data Cleaning for the LPA data in Data Warehouse:
https://github.com/moj-analytical-services/OPG/blob/main/LPA_Data.ipynb


&nbsp;
&nbsp; 
&nbsp;
<a name="data-setup"></a> 
# Data setup
- step by step instructions Data Engineering in Jupyter Lab:
https://github.com/moj-analytical-services/OPG/blob/main/LPA_Data.ipynb


## MLPA Project Data Requirements (OPG Data):
1. Understand and agree what data is required for the MLPA Model Office/ Private Beta (and for the wider MLPA project), and prioritisation
2. Understand the expected source of the required data for highest priority requirements
3. Understand how we access the required data and who owns it
4. Explore options for how we store and report on the data

## Data Requirements & Prioritisation Questions
1. What is the data and does it currently exist?
2. Where is/will the data be held?
3. What is the justification for needing this data?
4. What priority is this data in the overall context?
5. Must have in place for day one of private beta (October 2024)
6. Must have in place before full go-live (initial target April 2025)
7. Nice to have at some point in the future


&nbsp;
<a name="howto-d-m"></a> 
# How to Data Modelling

## Dimensional modeling
- Dimensional modeling is a data modeling technique where you break data up into “facts” and “dimensions” to organize and describe entities within your data warehouse. The result is a staging layer in the data warehouse that cleans and organizes the data into the business end of the warehouse that is more accessible to data consumers.
- By breaking your data down into clearly defined and organized entities, your consumers can make sense of what that data is, what it’s used for, and how to join it with new or additional data. Ultimately, using dimensional modeling for your data can help create the appropriate layer of models to expose in an end business intelligence (BI) tool.
- The ultimate goal of dimensional modeling is to be able to categorize your data into their fact or dimension models, making them the key components to understand.
- A fact is a collection of information that typically refers to an action, event, or result of a business process. As such, people typically liken facts to verbs. In terms of a real business, some facts may look like account creations, payments, or emails sent. It’s important to note that fact tables act as a historical record of those actions. You should almost never overwrite that data when it needs updating. Instead, you add new data as additional rows onto that table.
- A dimension is a collection of data that describe who or what took action or was affected by the action. Dimensions are typically likened to nouns. They add context to the stored events in fact tables. In terms of a business, some dimensions may look like users, accounts, customers, and invoices. A noun can take multiple actions or be affected by multiple actions. It’s important to call out: a noun doesn’t become a new thing whenever it does something. As such, when updating dimension tables, you should overwrite that data instead of duplicating them, like you would in a fact table.
- Pre-cloud data warehouses, there were two dominant design options, star schemas and snowflake schemas, that were used to concretely separate out the lines between fact and dimension tables. 
    - In a star schema, there’s one central fact table that can join to relevant dimension tables.
    - A snowflake schema is simply an extension of a star schema; dimension tables link to other dimension tables making it form a snowflake-esque shape.

### The dimensional modeling design process
- According to the Kimball Group, the official(™) four-step design process is:
     1. selecting a business process to analyse, 
     2. declaring the grain, 
     3. Identifying the dimensions, 
     4. Identifying the facts. 

- Coming back down to planet Earth, your design process is how you make decisions about:
    - Whether something should be a fact or a dimension
    - Whether you should keep fact and dimension tables separate or create wide, joined tables
    - This is something that data philosophers and thinkers could debate long after we’re all gone, but let’s explore some of the major questions to hold you over in the meantime.
- Should this entity be a fact or dimension?
    - Time to put on your consultant hat because that dreaded answer is coming: it depends. This is what makes dimensional modeling a challenge!
    - Kimball would say that a fact must be numeric. The inconvenient truth is: an entity can be viewed as a fact or a dimension depending on the analysis you are trying to run.

- Advantages of dimensional modeling
    - More accessibility: Since the output of good dimensional modeling is a data mart, the tables created are easier to understand and more accessible to end consumers.
    - More flexibility: Easy to slice, dice, filter, and view your data in whatever way suits your purpose.
    - Performance: Fact and dimension models are typically materialised as tables or incremental models. Since these often form the core understanding of a business, they are queried often. Materialising them as tables allows them to be more performant in downstream BI platforms.

- Disadvantages of dimensional modeling
    - Navigating ambiguity: You need to rely on your understanding of your data and stakeholder wants to model your data in a comprehensible and useful way. What you know about your data and what people really need out of the data are two of the most fundamental and difficult things to understand and balance as a data person.
    - Utility limited by your BI tool: Some BI tools don’t handle joins well, which can make queries from separated fact and dimensional tables painful. Other tools have long query times, which can make querying from ultra-wide tables not fun.

*Ref: https://docs.getdbt.com/terms/dimensional-modeling

- Guide structure overview
- We'll walk through our topics in the same order that our data would move through transformation:
    - Dig into how we structure the files, folders, and models for our three primary layers in the models directory, which build on each other:
    - Staging — creating our atoms, our initial modular building blocks, from source data
    - Intermediate — stacking layers of logic with clear and specific purposes to prepare our staging models to join into the entities we want
    - Marts — bringing together our modular pieces into a wide, rich vision of the entities our organization cares about
    - Explore how these layers fit into the rest of the project:
    - Review the overall structure comprehensively
    - Expand on YAML configuration in-depth
    - Discuss how to use the other folders in a dbt project: tests, seeds, and analyses

**We have got two options for data modelling:

1. Data modelling using queries of the warehouse tables directly from Python/R.

```sql
with events as (
	select *
	from "dim_guardianship_dev_dbt"."fct_case_receipts"
	where extract_type = 'latest_extract'
		and receipt_date >= date_parse('01-01-2008', '%d-%m-%Y')
),
dates as (
	select *
	from "common_lookup_dev_dbt"."dim_date"
),
donors as (
	select *
	from "dim_guardianship_dev_dbt"."dim_donors"
),
cases as (
	select *
	from "dim_guardianship_dev_dbt"."dim_cases"
),
attributes as (
	select dates.calendar_year as receipt_year,
		events.receipt_date,
		cases.case_id,
		cases.case_type,
		cases.case_subtype,
		cases.case_status,
		cases.donor_age_at_receipt,
		donors.gender,
		donors.region_name,
		events.extract_date
	from events
		left join dates on events.receipt_date = dates.date_name
		left join cases on events.extract_case_id = ces.extract_case_id
		left join donors on events.extract_donor_id = donors.extract_donor_id
)
select *
from attributes
```


2. Data Modelling using Create-a-Derived-Table (CaDT)
    - This should be built a fixed table to be used as the LPA data by using in create-a-derived table. 
    - The data engineering team has already done this, and it is available in Athena at guardianship_derived_dev_dbt.case_receipts. The data modelling part for LPA data has been done with data engineering team and here I exploited Dimensional Modelling  for the OPG warehouse using create-a-derived-table to customise the LPA data modelling for the forecasting model. In this case, fct_case_receipts is the fact table containing all POA receipt dates, while dim_donors and dim_cases are the dimension tables which contain information on the donor and case respectively.
    - I would need to check this, so they can move this table into prod once we’ve added any additional columns you need. 
    - One thing to note is that these tables are updated daily with new information from Sirius and inform the data engineering team to make some adjustments if we need a fixed table.
        - Adding consistent D.o.B, Age, and Postcode variables to the current derived tables:
            Cyrrently dob is missing from the derived tables for LPA and age is my code should be consistent with the current derived tables created by the data engineering team. Thus, rather than adding source variables like dob, it would be more useful if we could add any relevant calculated fields that you create to the derived tables. We’d actually like to avoid including columns like date of birth if possible as it can result in multiple ways of calculating age which we have already done some work to resolve. In fact, in the current code there appears to be yet another method for calculating age, so would be even more useful if we could bring this into line with the rest of analysis across OPG. This is the same as the idea behind my previous comment that it would be better for us to include geographical classifications rather than postcode in the data.
            
        - Adding Unique case reference for each donor = [donor_dob + donor_postcode + donor_gender]
            - We need to extract a list of Power of Attorney receipts with the following columns: 
            ['receiptdate', 'uid', 'type', 'casesubtype', 'status', 'donor_postcode', 'donor_gender', 'age'].
            
        - Sort by the unique id and count how many application

        - Dermine Whether the application type [casesubtype] is hw=health and welfare or pfa=property and finance

        - How many certificate provider (cp) for each lpa application?

        - Location based data and geographical data for the donor can be used to identify the financial situation and wherether they are located in England or Wales
        - In terms of the two ways that you use dob that we could include in the underlying tables:
            - To impute missing ages by giving them the most common age for that year of receipt. How does date of birth factor into this if you already have individual age values? 
            - There are already unique identifiers in the data for individual donors and ones which link the same person together across different donor_id values. What does your derived identifier using dob, gender and postcode do that these don’t? If you’ve identified a flaw in the existing IDs it could be that it would be more useful to add your derived ID to the underlying tables.

            - Peter mentioned a few of points on what we would like to see included in the Sirius data as follwoing in response to the above queries suggested by Phil:
 
            •	It is really helpful to have built in geographic location data linked to the donors postcode that we can use off-the-shelf so to speak. However, our use of postcode data is not limited to this and we are still developing ways in which specific postcodes can add significant value to the analysis of LPA customers. Examples include, but are not limited to for instance, measures of distance where individual postcodes can be linked to grid references; customer segmentation (CAMEO and Output Area Classifiers are already included) is an area of huge potential and we would want the flexibility to add new predictive tools as these become available. Retaining individual postcode data is therefore something of a priority for us.
            
            •	In principle, providing age by single year rather than date of birth would be ok. However, please can you describe how age is calculated? For forecasting and modelling purposes we need to calculate age at date of receipt in single years. It would not be sufficient to calculate age in another way, for instance on application, as applications can often take several years before they are received. This shouldn’t in theory be an issue with MLPAs where the application and receipt by OPG ought to occur at the same time but this will remain an issue with the relatively large volume of legacy LPAs which are likely to be received for a number of years, post MLPA implementation. It would also not be sufficient to try and recalculate age on receipt by using age on application (for instance) and add the additional time to receipt as this would be inaccurate in some cases. Alternatively providing the date of birth would allow us to calculate the donors age appropriate to the purpose required.
            
            •	The unique donor identifier. Grateful if you can provide details of this (e.g., variable name) as I don’t believe we currently receive this, but it would be useful to do so. 

In response to the points below:

•	Happy to add postcode to the data for development purposes. Our main objective is to ensure that any additional measures that are derived from the source data are all included in the data warehouse for use by others. But agree it makes sense for you to have them for the purpose of developing new measures on the basis that you can then provide us with any finalised code to add into the warehouse tables. I’ll look at adding this in a separate table where we keep variables that are used for development purposes but aren’t intended to be used as part of the end user model.

•	Year of age at receipt is already available. The warehouse currently includes single year of age at the point of receipt, donor signature, registration, and dispatch for LPA cases. Adding a new field for an age at any other relevant date would be fairly trivial if you needed any alternative points.

•	The column parent_id in the Sirius person table is used to link separate records that relate to the same person. In the data model we’ve added a new column called master_id which is parent_id if a person has one, or their person_id if not. This should therefore produce an id that links records together, although as with all these methods it isn’t perfect.

I’m currently making a few changes to the data model which should make it easier for you to add age data in your analysis. As part of this, I’ll also create a donor dimension with the date of birth and postcode information for you to use. Once this is finished, it would probably be worth us having a requirements gathering session where I can talk you through the changes and also see what the next steps might be for any other requirements you have.


&nbsp;
<a name="0how2"></a> 
+ *1 - Data Sources and Pipelines* 

&nbsp;
<a name="1how2"></a> 
+ *2 - Data Modelling using Create-a-Derived-Table (CaDT)* 

&nbsp;
<a name="2how2"></a> 
+ *3 - Lookup Tables (seed in CaDT)*
Seeds are lookup tables easily created from a .csv file. Put the .csv in the ./mojap_derived_tables/seeds/ directory and follow the same directory structure requirements and naming conventions as for models. As with marts models, your seeds should have property files that have the same filename as the seed. Seeds can be accessed by anyone with standard database access and so must not contain sensitive data. Generally, seeds shouldn’t contain more than 1000 rows, they don’t contain complex data types, and they don’t change very often. You can deploy a seed with more than 1000 rows, but it’s not reccomended and it will take quite a long time to build.

⚠️ Seeds must not contain sensitive data. ⚠️
    
The dbt seed command will load csv files located in the seed-paths directory of your dbt project into the data warehouse.

**Selecting seeds to run**
Specific seeds can be run using the --select flag to dbt seed. Example:
```console
>> cd mojap_derived_tables
>> dbt seed 
>> dbt seed --select "...__..."    
```
&nbsp;
<a name="3how2"></a> 
+ *4 - Macros (macros in CaDT)*
Macros in Jinja are pieces of code that can be reused multiple times 
– they are analogous to "functions" in other programming languages, and are extremely useful if you find yourself repeating code across multiple models. 
Macros are defined in .sql files, in the macros directory (create-a-derived-table/mojap_derived_tables/macros/income/income__get_latest_snapshot.sql).

The base derived tables should be to get the up-dated data through a macro "income__get_latest_snapshot" to get the most recent data from the FamilyMan derived tables by passing extract_date to the sql code.
    
The following code shows the macro, I wrote to filter the source derived table based on the most up-to-date data created by data engineering team:
    
```console

{% macro income__get_latest_snapshot(tables) %}

{% set latest_common_export_date_query %}
with exports as (
{%- for table_name in tables %}
select distinct mojap_snapshot_date
from {{ source('familyman_derived_live_v4', table_name) }}
{%- if not loop.last %}intersect{% endif -%}
{% endfor %}
)
select max(mojap_snapshot_date) AS latest_glueexporteddate
from exports
{% endset %}

{% set results = run_query(latest_common_export_date_query) %}

{% if execute %}
  {% if results|length > 0 %}
  {% set result = results.columns[0].values()[0] %}
  {% else %}
  {% set result = null %}
  {% endif %}
{% else %}
{% set result = null %}
{% endif %}

{{ return(result) }}

{% endmacro %}
```
   
#### Set variables at the top of a model
{% set ... %} can be used to create a new variable, or update an existing one. We recommend setting variables at the top of a model, rather than hardcoding it inline. This is a practice borrowed from many other coding languages, since it helps with readability, and comes in handy if you need to reference the variable in more than one place.


&nbsp;
<a name="4how2"></a> 
+ *5 - Running Updates*
**1. Check the lookup tables (located in seed directory in CaDT) as inputs in the Model are fed  and have properly updated. It may mean linking the seeds tables and especially FAM ID convertor csv file to the newest version of the source table based on snapshot date in the written macro in CaDT.**

**2. Check and run the seeds (using "dbt seed").**

&nbsp;
<a name="5how2"></a> 
+ *6 - Connection with Python code in Jupyter Lab* 
To connect the CaDT data models to Jupyter lab, use temp table ans read query in Python.
For more information see below.
https://docs.getdbt.com/reference/dbt-commands

&nbsp;
&nbsp;

&nbsp;
<a name="data-mart"></a> 
# Data Marts (the old Demand Forecasting for LPA Model)

## Meta data for the LPA source data

```sql
Select 
    uid, # unique identifier 
    type, # type od appliation # type = lpa (living power of atthorney)
    casesubtype, # type of lpa (hw=health and welfare, pfa=property and finance)
    status, # status = application should be Registered and stand by OPG and be used by or perfect, not other options like pending or withdrown
    receiptdate, # NOT NULL # very important for indexing and time series # recieptdate = actual receipt date that the application recieved by OPG and might change slightly and may produce the volume 
    registrationdate, # registration date only if the application is registered/Perfect/Payment Pending/Pending/Withdrawn.
    lpadonorsignaturedate, # donor signed the application # 2-3% of application are in this category and it is useful to track delay and identify top draw lpa as donor they dont want to pay for the power of athorney
    applicationtype, # application type is either Online or Classic (physical form) and 70% is doing the application in the Classic paper form
    repeatapplication, # Not Important and be ignored
    attorneyactdecisions, # Not Important and be ignored
    haveappliedforfeeremission, # Not Important and be ignored
    paymentremission, # Not Important and be ignored
    paymentexemption, # Not Important and be ignored
    paymentbycheque, # Not Important and be ignored
    lifesustainingtreatment, # Not Important and be ignored
    how_attorneys_appointed, # donor can appoint more than one attorney  # = (JS (Joined attorneies), S (Solely attorney))
    instructions_or_preferences, # each application might generate multiple OPG reciepts # = NONE/BOTH/INST/PREF
    donor_dob, #  NOT NULL # KEY VARIABLE to create a unique key # Date of Birth of the donor
    donor_postcode, #  NOT NULL # KEY VARIABLE to create a unique key # Postcode of the donor  
    attorney_count, # How many atthornies a donor applied for
    replacement_attorney_count, # if one of the attorneies died or withdrawns 
    a1_dob, # the first attorney DoB
    a2_dob, # the second attorney DoB
    a3_dob, # the third attorney DoB
    a4_dob, # the fourth attorney DoB
    a1_postcode, # the first attorney Postcode
    a2_postcode, # the second attorney Postcode
    a3_postcode, # the third attorney Postcode
    a4_postcode, # the fourth attorney Postcode
    r1_dob, # the first 
    r2_dob, # the second 
    r3_dob, # the third 
    r4_dob, # the fourth 
    cases_glueexporteddate, # date of lpa application cases extracted (e.g., 18/03/2024) # this useful to index the 10th file
    cp1_firstname, # certificate provider (cp) first name # can be a doctor or family/neighbor of donor # when donor and attorney signed needed to be withnessed and the person is an cp = to
    sign the document and assert the attorny
    cp1_surname, # certificate provider (cp)s second name 
    cp1_adr_lines_1, # certificate provider (cp)s the first line of address 
    cp1_adr_lines_2, # certificate provider (cp)s the second line of address 
    cp1_adr_lines_3, # certificate provider (cp)s the third line of address
    cp1_pcode, # certificate provider (cp)s postcode
    donor_gender, #  NOT NULL # KEY VARIABLE to create a unique key # Gender of the donor # sex = female,male, other (Dr, prof, etc)
    donor_nspl_oa11, # the geograpgical location of donor to measure of household finance and more useful information
    donor_nspl_cty, # Location based data wherether in England or Wales
    donor_nspl_laua, # 
    donor_nspl_ctry, # 
    donor_nspl_rgn, # 
    donor_nspl_lsoa11, # 
    donor_nspl_msoa11, # 
    donor_nspl_ccg, # 
    donor_nspl_ru11ind, # 
    donor_nspl_oac11, # 
    donor_nspl_imd, # 
    donor_nspl_rgn_name, # 
    donor_nspl_laua_name, # 
    donor_nspl_ctry_name, # 
    donor_nspl_ccg_name, # 
    donor_nspl_oac11_supergroup, # 
    donor_nspl_oac11_group, # 
    donor_nspl_oac11_subgroup, # 
    donor_wimd_decile, # 
    donor_imd_decile, # 
    donor_cameo_CAMEO_UKP, # 
    donor_cameo_CAMEO_UKPG, # 
    donor_cameo_Age_Score, # 
    donor_cameo_Age_Band, # 
    donor_cameo_Tenr_Score, # 
    donor_cameo_Tenr_Band, # 
    donor_cameo_Comp_Score, # 
    donor_cameo_Comp_Band, # 
    donor_cameo_Econ_Score, # 
    donor_cameo_Econ_Band, # 
    donor_cameo_Life_Score, # 
    donor_cameo_Life_Band, # 
    donor_cameo_CAMEOINTL, # 
    donor_cameo_CAMEO_UKP_name, # 
    donor_cameo_CAMEO_UKPG_name, # 
    donor_cameo_CAMEOINTL_group, # 
    donor_cameo_CAMEOINTL_type
```

&nbsp;
&nbsp; 
<a name="preprocessing"></a> 
# Feature Engineering and Data Preparation


&nbsp; 
<a name="model"></a> 
# Implementing the Demand Forecasting for LPA Model 
- details of model scripts.

## Long-Term Forecasting (Cohort-Based Model)
Cohort-based forecasting is a method used to predict future trends in customer behavior based on historical data. Unlike traditional forecasting methods that rely solely on aggregated data, cohort-based forecasting breaks down customer data into smaller groups with similar characteristics and looks at each group individually.
* ref: https://kohort.io/the-metrics-blog/cohort-based-forecasting-what-is-it-and-what-do-you-mean-its-kinda-like-football


These models are typically trained on time series data containing subscriptions by dates. However, an interesting alternative is to reformat the data to have subscriptions by users’ registration dates and purchase dates, effectively transforming the time series data into tabular data. This approach allows us to apply regression models, such as Generalized Linear Models (GLM) or Gradient Boosting Machines (GBM), which often produce better forecasts and offer additional insights regarding the attribution of future subscriptions to cohorts of users. These models are referred to as cohort-based models.
* ref: https://towardsdatascience.com/forecasting-with-cohort-based-models-e71003bc7ecd

### Key concepts related to cohort-based forecasting:

- Cohorts: By definition, a cohort is a “group of people with a shared characteristic, usually age.” In the context of subscription services, cohorts represent users who registered on a specific date. For example:
The “cohort of 2019–01–01” consists of all users registered on January 1, 2019.
The “cohort of 2019” includes all users registered during the entire year 2019.
Registration Date: This is the date when a user registers.
Upgrade Date (Purchase Date): The date when a user purchases a premium subscription.
Age of a Cohort/User: The number of days since the registration date.
Premiums: Refers to paid subscriptions.
Typically, users first register and then buy a subscription, sometimes on the same day, while other times only after using the product at no cost for a while. Many companies follow a “freemium” business model or offer free trial periods for their products.

When analysing cohorts, we often observe that they behave similarly. For instance:
When plotting the premiums of multiple cohorts with different registration dates by upgrade date, we notice that they have similar shapes.
The similarity becomes even more evident when we plot the same cohorts by age (days since registration).
Additionally, cohorts may generate premiums long after registration, as indicated by the long tails in the cohort curves over time2. This understanding of cohort behavior allows companies to make more accurate forecasts and tailor their strategies accordingly. In summary, cohort-based models provide an alternative approach to forecasting by considering user cohorts and their behavior over time. By doing so, companies can gain valuable insights and improve their subscription forecasts.

* ref: 

### Implementing cohort-based forecasting
The break it down implementing cohort-based forecasting for LPA applications in the OPG using Excel involves several steps:

#### Data Collection and Preparation:
**Gather historical data on LPA applications** 
including registration dates, upgrade dates (when the LPA is granted), and other relevant information.

**Organise the data into a tabular format** 
with each row representing an LPA application and columns for relevant attributes (e.g., registration date, upgrade date, user details).

#### Creating Cohorts:
**Define cohorts based on registration dates.** 
For example, create cohorts for each month or quarter.

**Calculate the age of each cohort **
(i.e., the number of days since registration).

#### Calculating Metrics:
For each cohort, calculate key metrics such as:

**Conversion Rate:**
Percentage of LPAs granted within a specific time frame (e.g., 6 months, 1 year) after registration.

**Retention Rate:**
Percentage of LPAs still active (not revoked) over time.

**Average Time to Grant:** 
Average duration from registration to LPA grant.

**Cumulative LPAs:**
Total LPAs granted by each cohort over time.

**Build Excel Formulas:**
Use Excel formulas to calculate the metrics mentioned above.
For example:
**Conversion Rate:**
Number of LPAs granted / Total LPAs in the cohort

**Retention Rate:**
(Total LPAs at a specific time - Revoked LPAs) / Total LPAs at the start

**Average Time to Grant:**
Average of (Upgrade Date - Registration Date) for granted LPAs

**Cumulative LPAs:** 
Use cumulative sum formulas.

**Visualize Data:**
Create charts (line charts, bar charts, etc.) to visualize cohort behavior over time.
Plot metrics such as conversion rates, retention rates, and cumulative LPAs for each cohort.

**Forecasting:**
Use historical data to project future trends.
Apply regression models (e.g., linear regression) to predict future metrics based on cohort age.
Extrapolate the metrics for the next 5 years.

**Scenario Analysis:**
Consider different scenarios (e.g., changes in LPA regulations, increased awareness) and their impact on cohort behavior.
Adjust your forecasts accordingly.

#### Cohort Analysis:
Cohort-based models group LPA applications based on common characteristics (e.g., application date, demographics, or region). 
Analysing historical cohorts helps identify trends and seasonality.
Machine learning techniques such as Survival Analysis can estimate the duration until an event (e.g., LPA application approval) occurs. 
Survival models account for censored data (applications still in progress).

#### Feature Engineering:
Extract relevant features related to the impact of COVID-19, such as:
**Mortality Rate:** Incorporate mortality data to understand its effect on LPA applications.
**Population Projection:** Use population growth projections to adjust demand estimates.
**Economic Indicators:** Consider economic factors (e.g., GDP, unemployment) that influence LPA demand.
**Healthcare Policies:** Include policy changes affecting LPA applications during the pandemic.

#### Time Series Models:
For long-term forecasting, consider ARIMA (AutoRegressive Integrated Moving Average) or Prophet models.
ARIMA captures seasonality, trends, and autocorrelation in historical LPA data.
Prophet is robust to missing data and handles holidays and special events well.





## Short-Term Forecasting (Exponential Smoothing):
*Collaborate with legal experts and domain specialists to refine approaches. Additionally, consider ensemble methods (combining multiple models) for robustness.

### Exponential Smoothing:
Exponential smoothing methods(e.g., Holt-Winters, ETS (Error, Trend, Seasonality)) are suitable for short-term forecasting.
These models adaptively weigh recent observations, emphasizing recent trends and seasonality.
Incorporate COVID-19 impact variables (e.g., lockdowns, vaccination rates) as additional inputs.

### Machine Learning Techniques:
Random Forests and Gradient Boosting can handle nonlinear relationships and feature interactions.
Train these models using historical LPA data, including COVID-19-related features.
Evaluate model performance using metrics like RMSE, MAPE, and R-squared.

### Uncertainty Modeling:
To address data uncertainty, use Bayesian Structural Time Series (BSTS) models.
BSTS captures both observed and unobserved components, allowing for better handling of irregularities caused by external events (like COVID-19).

#### Bayesian Structural Time Series (BSTS): 
BSTS is a powerful method for modeling and forecasting time series data. 

* ref: https://www.activeloop.ai/resources/glossary/bayesian-structural-time-series/
* ref: https://en.wikipedia.org/wiki/Bayesian_structural_time_series
* ref: https://www.mckinsey.com/capabilities/operations/our-insights/ai-driven-operations-forecasting-in-data-light-environments
* ref:

However, like any technique, it has its limitations. Here are some key points to consider:

*Computational Complexity:
Bayesian inference techniques used in BSTS can be computationally intensive, especially for large datasets or complex models.
Handling the calculations efficiently may require specialized hardware or software1.

*Mathematical Underpinning:
BSTS relies on a relatively complicated mathematical framework, including concepts like state-space models and Kalman filtering.
Implementing BSTS as a computer program can be challenging for researchers without a strong mathematical background2.

*Model Interpretability:
While BSTS provides accurate forecasts, understanding the underlying components (trend, seasonality, regression effects) can be complex.
Interpreting the model’s results may require domain expertise and careful analysis.

*Assumptions and Priors:
Like any Bayesian approach, BSTS relies on prior distributions for model parameters.
Choosing appropriate priors can impact the model’s performance, and selecting informative priors may be challenging.

*Handling Irregularities:
BSTS assumes that the underlying time series follows a specific structure (e.g., linear trend, Gaussian noise).
Handling irregularities (e.g., sudden outbreaks, volatility) may require additional modeling or adjustments3.

*Data Availability:
BSTS performs best when historical data is abundant and informative. Sparse or noisy data may lead to less reliable forecasts.

*Despite these limitations, BSTS remains a valuable tool for time series analysis, especially when combined with domain knowledge and other techniques. 
Researchers should carefully consider their specific use case and explore alternative methods if necessary

&nbsp;
&nbsp;
&nbsp;
&nbsp; 
<a name="calc-model"></a> 
# Model Calculation - details of model calculation.
# __Technical Guidance__
<a name="start"></a> 
## Getting started
&nbsp;
<a name="run-model"></a> 
## Running the model
- step by step instructions
&nbsp;

## LPA Control Assumptions
Specific Key Assumptions that control expected demand, LPA market size and saturation.

## ONS Mortality Statistics 
### Source Data For Mortality Statistics and Modelled Age Specific Survival Rates (Model Input Set By Control Assumptions)

* ref: 'LPA MODEL': 	Mortality Statistics	MALE: ESTIMATED AGE SPECIFIC SURVIVAL		FEMALE: ESTIMATED AGE SPECIFIC SURVIVAL

Copy Nemerical Values in column C and transpose paste in column F		Copy Nemerical Values in column C and transpose paste in column F

* ref: Source: Office for National Statistics: 		Source: Office for National Statistics: nationallifetables3yearenglandandwales.xlsx		nationallifetables3yearenglandandwales.xlsx		Sheet: '2020-2022'		Sheet: '2020-2022'	Released: 11 January 2024		Released: 11 January 2024

* ref: Downloaded from: National life tables: England and Wales - Office for National Statistics		National life tables: England and Wales - Office for National Statistics

* ref: The best source of information for the ONS mortality statistics which are here: Mortality rates (qx), by single year of age - Office for National Statistics (ons.gov.uk)

#### risks in Mortality Statistics
The main issue with these figures is that they are only provided separately for England , and separately for Wales , and not as a combined rate for England and Wales. This is frustrating but comparing the rates the differences are extremely small so probably would not make any practical difference if we chose to use the figures for just England.

To be clear what these figures are showing are equivalent to the mortality rates in columns O and P on the Mortality Statistics sheet in the model. Looking at the mortality rates in the model in column O for example showing male morality at age 18 this gives a figure of 0.3 per 1000 adults or 0.0003 (ie 0.3/1000). The equivalent figure in the ONS mortality tables for males aged 18 for 2017-2019 is 0.00039 so slightly higher. The actual ONS mortality rates suggest that the model currently over-estimates mortality rates for donors aged 90 and over so it will be useful to update these.

I think to simplify things and given the very small difference in mortality rates between England and Wales for 2017-19 that we could just use the mortality rates for England. Once we have more time we can add some complexity by adding variants such as rates for Wales or combined England and Wales estimates.  



## POPULATION PROJECTION data

### understanding the data (“Population Forecast Model Input” tab in the excel model):

* ref: As this data is fed from other tabs 'Population Variants England' and 'Population Variants Wales'.

In the last version of the model, the source of data was 2016-based and 2018-based which are zipped files including:
“HIGH FERTILITY PROJECTION 2018 (2016 BASED TO 2017)”, “HIGH POPULATION PROJECTION 2018 (2016 BASED TO 2017)”, “HIGH LIFE EXPECTANCY PROJECTION 2018 (2016 BASED TO 2017)”, “HIGH MIGRATION PROJECTION 2018 (2016 BASED TO 2017)”, “PRINCIPLE POPULATION PROJECTION 2018 (2016 BASED TO 2017)”  and similar data for the “LOW” figures in xml files.

I have just find out that the national population projections data files (in the National population projections: 2021-based interim (located in National population projections table of contents - Office for National Statistics) has been changed in terms of formatting since 2020 and there is one excel file (e.g., for 2021-based, there is only one worksheet: “2021-based interim edition of this dataset” in Zipped population projections data files, England - Office for National Statistics), which only provided the PRINCIPLE POPULATION PROJECTION data.

* Note:
‘The use of the term ‘interim’ in the release title is to reflect that these projections reuse mortality and fertility assumptions from the previous 2020-based NPPs, do not include the range of variant projections that are usually published, and are being published as a headline-only release ahead of 2022-based NPPs.’ Thus, I am not quite sure if I have to reuse mortality and fertility assumptions from the previous years and exclude years without this information? Also, I could also add more data by using “Zero net migration (natural change only) variant - England population in age groups - Office for National Statistics (ons.gov.uk)” data in the following link: Zero net migration (natural change only) variant - England population in age groups - Office for National Statistics (ons.gov.uk), which represent “Projected populations at mid-years by age last birthday in five-year age groups”. 


### Calculationas: Population Forecast Model Input
             
**The follwoing formula calculate the National Population Projections: 2018-based Statistical Bulletin - Office for National Statistics, older versions used for older data**

Calculating the total Sum of **'Population Variants England' and 'Population Variants Wales' (Males + Females) based on year - age: 18+** the follwoing database based on the LPA assumption of model input categories listed below:

1. High Population Variant
2. High Fertility Variant
3. Low Population Variant
4. Low Fertlity Variant
5. High Life Expectancy Variant
6. Low Life Expectancy Variant
7. High Migration Variant
8. Low Migration Variant
9. Principle Projection

**The corresponding excel formula:**

('Population Variants England'!C245+'Population Variants Wales'!C245)*'LPA Control Assumptions'!$B$62+('Population Variants England'!AI245+'Population Variants Wales'!AI245)*'LPA Control Assumptions'!$B$63+('Population Variants England'!BM245+'Population Variants Wales'!BM245)*'LPA Control Assumptions'!$B$64+('Population Variants England'!CR245+'Population Variants Wales'!CR245)*'LPA Control Assumptions'!$B$65+('Population Variants England'!DW245+'Population Variants Wales'!DW245)*'LPA Control Assumptions'!$B$66+('Population Variants England'!FB245+'Population Variants Wales'!FB245)*'LPA Control Assumptions'!$B$67+('Population Variants England'!GG245+'Population Variants Wales'!GG245)*'LPA Control Assumptions'!$B$68+('Population Variants England'!HL245+'Population Variants Wales'!HL245)*'LPA Control Assumptions'!$B$69+('Population Variants England'!IQ245+'Population Variants Wales'!IQ245)*'LPA Control Assumptions'!$B$70              
* NOTE: The dependencies tables: 


## LPA MARKET SHAPE 
The forecast assumes that the "Shape" of the LPA market = LPAs as a % of Population Totals
LPAs as % of Population Totals = Assumed Market "Shape"

* ref: LPA MODEL / LPA MARKET SHAPE

### Calculation:
The total SUM (donor counts (age specific for two consecusive years)) 

DIVIDED BY (the total SUM of 'Population Forecast Model Input' (age specific for two consecusive years))

**The corresponding excel formula:**
=SUM(AO8:AP8)/SUM('Population Forecast Model Input'!O25:P25)

* NOTE: The dependencies tables: 

## Assumed Potential Maximum Market
For single age groups individuals aged 88 have the highest probability of purchasing an LPA. If we imagine theerfore that we could theoretically persuade every person aged 88 to purchase an LPA in any given year then the current  maximum level of demand amongts other age groups is assummed to be in proportion to LPAs as % of Population Totals (ie the same shape).

* ref: LPA MODEL / Assumed Potential Maximum Market

### Calculation:
Peak_age = 90

IF: 'LPA Control Assumptions: Assume Market Shape Based On LPA Age Distribution Applies' = 1 (TRUE) 

THEN: 'Assumed Potential Maximum Market' at Peak_age 

MULTIPLIED BY ('LPA MARKET SHAPE' by the corresponding age and year DIVIDED BY 'LPA MARKET SHAPE' at Peak_age)

OTHERWISE: 1


**The corresponding excel formula:**
=IF('LPA Control Assumptions'!$B$520=1,$AW$80*AU8/$AU$80,1)

* NOTE: The dependencies tables: 

## MAX MARKET ESTIMATES
This calculates the maximum market estimates based on proportion of the ONS population projection at the specicific age and year

* ref: LPA MODEL / Assumed Potential Maximum Market

### Calculation:
'Population Forecast Model Input' (the corresponding age and year)
MULTIPLIED BY "Assumed Potential Maximum Market" (age specific)


**The corresponding excel formula:**
='Population Forecast Model Input'!D25*AW8


* NOTE: The dependencies tables: 

## LPA SURVIVAL TABLES:
Meta data and Variable selection and Data Cleaning for the Mortality statastics data based on population projections:
* ref: LPA MODEL/LPA SURVIVAL TABLES


### Goal: percentage of people are died in one year
#### What proportion of the UK population are likely to buy LPA and still alive?
*How many people are still alive (Living Donors bought LPA)*
*Based on ONS Data of Population of Engalnd and Wales, how many people are still alive and how many of them are dead?*
*e.g., if there are 1000 people and 100 of them are still alive and bought LPA,
so there are 900 of them still didn't buy LPA.


**1. These rates are standardised to the 2013 European Standard Population, expressed per million population; 
they allow comparisons between populations with different age structures, including between males and females and over time. 
**2.  Deaths per 1,000 live births. 
**3.  Death figures are based on deaths registered rather than deaths occurring in a calendar year.

*if a 1000 40 years old male bought an LPA in 2008, what proportion of are still alove today?

#The model taking each age categories (categorical variable) and assumed that they are 
singe age-specifics in the age category 18 to 90 and provide figure what percentage of people for male died within one year?

e.g., in the 15-19 age category, 0.3 percent of males died within one year in the UK and 0.03 per 1000

e.g., in the 25-29 age category, 0.6 percent of males died within one year in the UK and 0.06 per 1000

e.g., in the 70-74 age category, 23.7 percent of males died within one year in the UK or 2.37 per 1000

*if you started at age 18, 7 years and become 25 years old ahead, 
as the ages goes up you will fall into a higher mortality category (from 0.3 to 0.6)

#### Data Path
**qx: is the mortality rate between age x and (x +1), that is the probability that a person aged x exact will die before reaching age (x +1).**

**We extract data from Age 18+.**

* NOTE: The dependencies tables: 

### LPA SURVIVAL TABLES: (BY YEAR OF APPLICATION)

### Calculation:
1. For each year, we would need to fill the corresponding year by the actual LPA DATA. For each corresponsing year and age group (e.g., year = 2007 to 2023 and age = 18 to 106): 
Fill the column age specific from the number of donors actual LPA DATA

2. For the follwoing years after the corresponding year, we would need to use the 'Mortality Statistics': MALE/FEMALE: ESTIMATED AGE SPECIFIC SURVIVAL tables and calculate the number of donors based on the survival rate:
**prior year = the corresponding year REDUCTED from the starting (base) year 2007 = the number of previous years till the corresponding year to track back and calculate the ESTIMATE AGE SPECIFIC SURVIVAL for male/female.**

IF: 'LPA Control Assumptions: FORECAST ASSUMPTIONS: MORTALITY RATES' = 1 (Male) 
THEN: ((the number of donors for **prior_year** years before the corresponding year (age - **prior_year**))
MULTIPLIED BY ('Mortality Statistics': MALE: ESTIMATED AGE SPECIFIC SURVIVAL) for the corresponding age and +**prior_year**)
OTHERWISE: ((the number of donors for **prior_year** years before the corresponding year (age - **prior_year**))   
MULTIPLIED BY ('Mortality Statistics': FEMALE: ESTIMATED AGE SPECIFIC SURVIVAL) for the corresponding age and +**prior_year**)
**The corresponding excel formula:**
=IF('LPA Control Assumptions'!$B$45=1,CD8*'Mortality Statistics'!$BC$4,CD8*'Mortality Statistics'!$DU$4)

3. For the consecutive tables: for each year - age specific, generate a table that start with the consecutive year of the above table. For the corresponsing year, fill the column for the year (from 2008 to 2023)  similar to the the number 1 equation above: Fill the column age specific from the number of donors actual "LPA DATA". Then for the forecasting years (from 2024 to 2030): Fill the column age specific from the forecasted number of donors in "NEW LPA FORECAST". For the rest of consecutive years in the table, follow equation in number 2 above. 


* NOTE: The dependencies tables: actuals from LPA DATA table, and 'Mortality Statistics': MALE/FEMALE: ESTIMATED AGE SPECIFIC SURVIVAL tables


## LPA SURVIVAL TABLES: (TOTAL)

### Calculation:
* For each corresponsing year and age (e.g., year = 2007 to 2030 and age = 18 to 106):
SUM (LPA SURVIVAL TABLES: (BY YEAR OF APPLICATION))


**The corresponding excel formula:**

* From 2007 to 2030
=CD8+CD100+CD192+CD284+CD376+CD468+CD560+CD652+CD744


* NOTE: The dependencies tables: LPA SURVIVAL TABLES: (BY YEAR OF APPLICATION), NEW LPA FORECAST, and LPAS AS A % OF REMAINING CUSTOMERS (UNADJUSTED  for media events)

## LPAS AS A % OF REMAINING CUSTOMERS (UNADJUSTED  for media events)

### Calculation:
1. for each corresponsing year and age group (e.g., year = 2024 and age = 18-20):
SUM (number of donor applications: Fill the column age specific from the number of donors actual LPA DATA) 
DIVIDED BY 
SUM (LPA SURVIVAL TABLES: (TOTAL))

2. Controls The % of the Previous Value
SUM (
(% for (year - 1) and (age: 21-25))
MULTIPLY BY 
('LPA Control Assumptions': Smoothing Factor: Aged 18-20 (% of Previous Value): 10-30% = RANDBETWEEN(lower bound *1000, upper bound * 1000) / 1000))

(1 - ('LPA Control Assumptions': Smoothing Factor: Aged 18-20 (% of Previous Value): 10-30% = RANDBETWEEN(lower bound *1000, upper bound * 1000) / 1000))
MULTIPLY BY 
(( % for (year - 1) and (age: 21-25)) - ( % for (year - 1) and (age: 26-30))))

(% for (year - 1) and (age: 21-25))
)

**The corresponding excel formula:**
1. From 2007 to 2023
=SUM(AD8:AD10)/SUM(EH8:EH10)

2. from 2024 to 2030
=FY9*'LPA Control Assumptions'!$B$123+(1-'LPA Control Assumptions'!$B$123)*('LPA MODEL'!FY9-'LPA MODEL'!FX9+'LPA MODEL'!FY9)

* NOTE: The dependencies tables: 

## NEW LPA FORECAST

### Calculation:
1. for each corresponsing year and age group (e.g., year = 2007 to 2023 and age = 18 to 106): Fill the column age specific from the number of donors actual LPA DATA

2. MULTIPLY "REMAINING CUSTOMERS" by "Controls The % of the Previous Value"

**The corresponding excel formula:**
1. For 2007 to 2023


2. From 2008 to 2030
=FZ9*EY8

3. SUMMARY: ()
Historic: SUM ()
Forecast: SUM ()

* NOTE: The dependencies tables: "REMAINING CUSTOMERS" by "Controls The % of the Previous Value"


## REMAINING CUSTOMERS
This table calculates the maximum market estimates based on proportion of the ONS population projection at the specicific age and year

* ref: LPA MODEL / Assumed Potential Maximum Market

### Calculation:
1. for each corresponsing year and age group (e.g., year = 2007 and age = 18 to 106): Fill the column age specific from the "MAX MARKET ESTIMATES" 

2. IF the "MAX MARKET ESTIMATES" greater than "REMAINING CUSTOMERS" by "Controls The % of the Previous Value"

**The corresponding excel formula:**
1. For 2007 to 2023


2. From 2008 to 2030

**The corresponding excel formula:**
=MAX(0,BB8-DF8)


* NOTE: The dependencies tables: 




## Donor Estimates & Actuals
Unadjusted estimates: 2007 - 2015. Applies the age specific percentage of donors (known values from 2016 & 2017 data) to historic Meris data to estimate numbers of donors. Totals are unadjusted as they do not equal the total number of LPA appplications witin each year.

Adjusted estimates to LPA totals: Initial estimates of the numbers of donors are scaled up to equal actual LPA totals.


**The corresponding excel formula:**
=$C$98/$Q$98*Q8

Q8: C8*'Sirius Donor Attorney Splits'!AS7 in Donor Estimates & Actuals

Multiply "Donor Estimates & Actuals" for the year from LPA data by sum of (Raw Age Distributions (Donors & Attorneys)) devided by sum of (Donor Estimates & Actuals) for that specific age on the choosen year

C8:
male = 1
female = 2
randomise = 3

If the applications are for male = 1 then MALE: ESTIMATED AGE SPECIFIC SURVIVAL in year and age 
    
* NOTE: The dependencies tables: LPA DATA (actuals)

    
* NOTE: This was used in the previous version of LPA MODEL, now is skipped to simplify the model.

#### For information on registration delays for a range of causes, see: 
    https://webarchive.nationalarchives.gov.uk/ukgwa/20160106020016/http://www.ons.gov.uk/ons/guide-method/user-guidance/health-and-life-events/impact-of-registration-delays-on-mortality-statistics/index.html

A limiting factor in modelling numbers of surving LPA holders aged 90+ has been the absence of single age specific mortality rates 
for this group. Estimates* suggested that previously applied mortality rates were too low increasing the apparent numbers of 
surviving LPA holder saged 90+ and therefore over-estimating the "sauration of this market.

For the 2018 LPA forecast , Age specific mortality rates for those aged 90+ have therefore been extrapolated based on 
a standard log power law that best fits existing mortality rates to age. 

*numbers of surviving LPA holders were estimated to exceed the total projected  population in each age group which was 
clearly not possible.
&nbsp;



&nbsp;
<a name="ap-s3"></a> 
## Analytical Platform (AP) and AWS S3 access
- instructions on setting up AP and s3 access
Go the the repo in Git:
https://github.com/moj-analytical-services/OPG

Open Terminal:
```console
git clone git@github.com:moj-analytical-services/Income_Profile_Forecast_Model.git
```

If there is any error then follow the instruction below:
Create and add JupyterLab SSH key to GitHub

&nbsp;
<a name="setup"></a> 
## Setting up a Python virtual environment
```console
pip install -r requirements.txt
```
    
```python 
!. venv/bin/activate
#!pip install arrow-pd-parser
``` 


&nbsp;
<a name="github"></a> 
## Accessing the model from Github and Error handelling solutions
- Pulling the OPG repo to your local area of the AP from GitHub
When working on your models it is likely that your branch will get out of date with the main branch. 
To update you branch with the latest changes from main open a terminal and run the following:

Check your working tree, commit/push any changes if required:

```console
git status
```

Switch to the main branch and collect the latest changes, if any

```console
git switch main
git fetch
git pull
```

Switch back to your branch and merge in the changes from main

```console
git checkout -b <your initial>/model-a-development
git switch <your initial>/model-a-development
git merge main -m "update branch with main"
```

&nbsp;
<a name="python-pack"></a> 
# Python libraries and versions 
- details of python version and package versions used

&nbsp;
<a name="pack"></a> 
## Loading python packages
Before you can run this project, you need to install some Python packages using the terminal:
```python 

```

&nbsp;
<a name="export"></a> 
# Exporting Output into CSV and Excel

&nbsp;
<a name="evaluation"></a> 
# Evaluation of the model

&nbsp;
<a name="plot"></a> 
# Plotting The Forecasted vs Actual values

## Visualizing cohort data in Excel can help you gain insights and identify patterns over time. Here are some steps to visualize your cohort analysis results:

**Conditional Formatting:**
Highlight key insights from your cohort table using conditional formatting.
Select your cohort data.
Click on Home > Conditional Formatting > Color Scales.
Choose a color scale that suits your data.
Adjust the scale to enhance the contrast between high and low rates.
Colors will reveal patterns in customer retention.

**Charting and Graphing:**
Excel offers a range of charting and graphing options to visualize your cohort analysis results.

**Create:**
Line Charts: Represent how metrics change over time within different cohorts.
Bar Graphs: Compare metrics across different cohorts.

**Heatmaps:**
Show variations in metrics by color intensity.
Visualizations make it easier to identify trends and patterns within your data2.
Remember to organize your data with the necessary attributes and timestamps, define your cohorts, and calculate relevant metrics before creating visualizations.


**an example of a cohort line chart?**

A cohort analysis chart is a powerful tool for understanding user behavior over time. It allows you to group users based on specific characteristics (such as acquisition date) and track their actions or metrics over subsequent periods. Let’s take a look at an example of a cohort analysis chart:

**Example Cohort Analysis Chart (Weekly Revenue per Group):**

In this chart, we’ll focus on revenue generated by cohorts of customers acquired in specific weeks.
The vertical axis represents the cohorts, with the oldest cohorts at the top and the newest ones at the bottom.
Each row corresponds to a cohort of customers who started using a product or service during a particular week.
The horizontal axis represents time (e.g., weeks, months) after the cohort’s acquisition.
The cells in the chart display the revenue generated by each cohort during each time period.
Here’s a simplified representation of how the chart might look:

Week 1   Week 2   Week 3   Week 4   ...   Week N
-------------------------------------------------
Cohort 1:   $100     $120     $110     $130          ...
Cohort 2:   $80      $90      $100     $95           ...
Cohort 3:   $150     $140     $160     $155          ...
...         ...      ...      ...      ...           ...
Cohort M:   $200     $210     $220     $205          ...

Each cell shows the revenue generated by a specific cohort during a particular week.
You can read across the rows to see how a cohort’s revenue changes over time.
Reading from top to bottom allows you to compare different cohorts during a specific time period.
Diagonally, you get a snapshot of how each cohort performs at a specific point in time.
In this example, you’d analyze how revenue evolves for each cohort as weeks progress. This information can guide strategic decisions, such as optimizing marketing efforts, improving product features, or addressing customer retention.

Remember that cohort analysis can be customized based on the specific metrics you’re interested in (e.g., user engagement, churn rate, conversion rate). The key is to segment users into meaningful groups and track their behavior over time to uncover valuable insights1. 


&nbsp;
<a name="processflow"></a> 
# Process flow Diagrams
- proccess flow diagrames of inputs/outputs for the pre-model and model, and the python function process flow. 
The following image demonestrates a proccess flow diagrames of main inputs/outputs for the Demand Forecasting for LPA Model.

*under constuction!

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
*What are the common challenges in LPA forecasting?

## Risk of usig excel model: 
Remember that Excel has limitations for complex forecasting models, especially when dealing with large datasets. WE might switch to more sophisticated modeling, consider using specialized statistical software or programming languages like Python or R.

## Risk, assumptions, and challenges forecasting for LPA
*When it comes to forecasting for Lasting Power of Attorney (LPA) applications, there are several challenges that organizations and individuals may encounter. 

Let’s explore some of these common challenges:

### Legal Validity and Challenges:
1. Lack of Capacity: 
An LPA must be created by someone with the required mental capacity as defined in the Mental Capacity Act 2005. If there are doubts about the donor’s capacity during the creation of the LPA, it can lead to legal challenges1.
2. Fraud or Duress: 
LPAs created fraudulently or under duress can be challenged. If an LPA is suspected to be invalid due to coercion or deception, legal action may follow1.
3. Attorney Suitability and Abuse:
4. Unsuitable Attorneys: 
Sometimes, appointed attorneys may not act in the best interests of the donor. Relatives or concerned parties can challenge an LPA if they believe an attorney is unsuitable.
5. Abuse of Position: 
If an attorney abuses their position (e.g., mismanaging finances, neglecting the donor’s welfare), it can lead to disputes and legal challenges1.
6. Notification and Objection:
7. Notification Process: 
When someone creates an LPA, they can list individuals to be notified by the Office of the Public Guardian (OPG). These notified individuals have the chance to object to the registration of the LPA.
8. Relatives’ Awareness: 
In some cases, relatives may not know that the donor has made an LPA until later, which can complicate matters if they wish to challenge it1.
9. Personality Clashes and Autonomy:
10. Reasonable Grounds: 
Challenges must have genuine and reasonable grounds. A mere personality clash with an attorney is not sufficient to have them removed. Autonomy in choosing attorneys is essential.
11. Balancing Autonomy and Protection: 
Balancing the individual’s autonomy to choose attorneys with the need to protect their interests can be challenging1.
12. Complex Application Process:
13. Errors in Completion: 
Completing the LPA application correctly is crucial. Errors can lead to delays or rejection by the OPG. Avoiding common mistakes during the application process is essential2.
14. Health and Welfare LPAs:
15. Timing: 
Health and welfare LPAs only take effect once the donor has lost mental capacity. Forecasting the timing of capacity loss accurately can be challenging.
16. Changing Circumstances: 
Health conditions and circumstances can change, affecting the applicability of health and welfare LPAs1.
In summary, LPA forecasting involves legal, practical, and ethical considerations. Organizations and individuals must navigate these challenges to ensure effective decision-making and protection for donors.



### Addressing capacity fluctuations in forecasting, especially in the context of Lasting Power of Attorney (LPA) applications, is crucial for accurate predictions. Here are some strategies to consider:


#### Understand Capacity Fluctuations:
Recognize that mental capacity can change over time due to various factors (e.g., health conditions, aging, stress).
Monitor the individual’s cognitive abilities and assess their capacity periodically.

#### Historical Data Analysis:
Examine historical LPA applications to identify patterns related to capacity fluctuations.
Look for trends in the timing of capacity loss or improvement.
Consider whether certain age groups or health conditions are more prone to fluctuations.

#### Segmentation by Risk Factors:
Divide your data into segments based on risk factors (e.g., age, health status).
Analyze how capacity fluctuations vary across these segments.
Adjust your forecasting models accordingly for each segment.

#### Probabilistic Models:
Use probabilistic models to account for uncertainty.
Bayesian models, Markov models, or survival analysis can incorporate changing probabilities of capacity loss.
These models allow you to update predictions as new information becomes available.

#### Scenario-Based Forecasting:
Create scenarios that simulate different capacity trajectories. For example:
- Stable Capacity: Assume capacity remains stable over time.
- Gradual Decline: Assume a gradual decline in capacity.
- Sudden Decline: Consider sudden capacity loss due to unforeseen events (e.g., stroke, accident).
- Forecast LPAs under each scenario and assess their impact.
- Collaborate with Healthcare Professionals:
- Consult with healthcare providers who can assess capacity objectively.
- Obtain medical opinions and consider their insights in your forecasting process.
#### Sensitivity Analysis:
- Test the sensitivity of your forecasts to capacity fluctuations.
- Vary the assumptions about capacity loss rates and observe the impact on LPA applications.
- Educate Attorneys and Donors:
- Educate attorneys (appointed individuals) and donors (those creating the LPAs) about capacity fluctuations.
- Encourage them to review and update LPAs periodically to reflect changing circumstances.
- Remember that capacity fluctuations are inherent in LPA forecasting, and no model can predict with absolute certainty. However, by incorporating flexibility and considering different scenarios, you can improve the accuracy of your forecasts. 


&nbsp;
&nbsp;
<a name="qa"></a> 
# Quality Assurance (QA)
- directions to the folder that holds the logs and evidence of initial model v1 QA

**Optimisations of the SQL Query Checks:**
1. Avoid nested joins: Instead of nesting multiple joins, we can perform them in a single level, which can improve readability and potentially performance.
2. Simplify aggregation: Instead of using the GROUP BY clause at the top level, we use it within the TRANSFORM clause, simplifying the query structure.
3. Optimize join conditions: Ensure that join conditions are efficient and necessary indexes are in place for better performance. However, this depends on the database system and schema.

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

## Bayesian models
Incorporating Bayesian models in Lasting Power of Attorney (LPA) forecasting can enhance accuracy and provide a probabilistic framework for handling uncertainty. Let’s explore how Bayesian methods can be applied to LPA forecasting:


#### Understanding Bayesian Models:
Bayesian models are based on Bayes’ theorem, which updates our beliefs (probabilities) based on new evidence.
These models incorporate prior knowledge (prior distribution) and update it with observed data to obtain a posterior distribution.
In the context of LPA forecasting, Bayesian models allow us to quantify uncertainty and make informed predictions.

#### Dynamic Linear Models (DLMs):
DLMs are a class of Bayesian state space models commonly used for time series forecasting.

#### They consist of two components:
State Equation: Describes how the underlying state (e.g., capacity fluctuations) evolves over time.
Observation Equation: Relates the observed data (e.g., LPA applications) to the underlying state.
DLMs can handle time-varying parameters, seasonality, and irregularities in data.

### Steps to Incorporate Bayesian Models:

#### Prior Specification:
Define prior distributions for model parameters (e.g., capacity loss rates, trend coefficients).
Priors can be informative (based on domain knowledge) or non-informative (flat priors).

#### Likelihood Function:
Specify the likelihood function that relates observed data to the model parameters.
For LPA forecasting, this could be based on historical LPA application data.

#### Posterior Inference:
Use Bayes’ theorem to update the prior distribution based on observed data.
Markov Chain Monte Carlo (MCMC) methods or variational inference can estimate the posterior distribution.

#### Prediction:
Simulate from the posterior distribution to obtain predictive samples.
These samples represent possible future scenarios, accounting for uncertainty.
Model Selection:

#### Choose an appropriate DLM structure:
Local Level Model: Represents a random walk (e.g., gradual capacity decline).
Local Linear Trend Model: Includes both level and slope components.
Seasonal Models: Capture seasonal patterns.
Regression Models: Incorporate external predictors (e.g., health indicators).
Model selection can be guided by cross-validation or information criteria (e.g., Bayesian Information Criterion).

#### Updating Over Time:
As new LPA application data becomes available, update the model using Bayesian methods.
This allows the model to adapt to changing conditions (e.g., shifts in capacity fluctuations).

#### Scenario Analysis:
Generate probabilistic forecasts for different scenarios:
Gradual capacity decline.
Sudden capacity loss due to health events.
Capacity improvement (if relevant).
Assess the impact of these scenarios on LPA applications.
Remember that Bayesian models provide a flexible framework for incorporating prior knowledge, handling uncertainty, and adapting to changing conditions. While implementing Bayesian models in Excel directly may be challenging, consider using specialized statistical software (e.g., Python with libraries like pymc3 or Stan) for more complex modeling12. 




### While Bayesian models offer several advantages, they also come with limitations, especially when applied to Lasting Power of Attorney (LPA) forecasting. Let’s explore some of these limitations:
#### Computational Complexity:
Bayesian models involve complex calculations, especially when estimating posterior distributions using Markov Chain Monte Carlo (MCMC) methods.
For large datasets or high-dimensional models, the computational burden can be significant.

#### Subjectivity in Prior Selection:
Bayesian models require specifying prior distributions for model parameters.
The choice of priors can impact the results, and different analysts may choose different priors based on their beliefs or domain knowledge.
Subjective priors can introduce bias if not carefully considered.

#### Data Requirements:
Bayesian models perform well when sufficient data is available.
Sparse or noisy data can lead to unreliable posterior estimates.
In the case of LPAs, historical data may be limited, especially for specific subgroups (e.g., rare health conditions).

#### Model Misspecification:
If the chosen Bayesian model does not accurately represent the underlying process (e.g., capacity fluctuations), the results may be misleading.
Model misspecification can lead to biased parameter estimates.

#### Assumptions of Independence:
Many Bayesian models assume independence between observations.
In reality, dependencies may exist (e.g., correlations between LPAs within the same family).
Ignoring dependencies can affect the accuracy of forecasts.

#### Interpretability:
Bayesian models provide posterior distributions, which are more informative than point estimates.
However, interpreting complex posterior distributions can be challenging for non-experts.
Communicating uncertainty effectively to stakeholders may require additional effort.

#### Limited Excel Integration:
Implementing Bayesian models directly in Excel can be cumbersome due to its limitations in handling probabilistic calculations.
Specialized statistical software (e.g., Python, R) is better suited for Bayesian modeling.

#### Assumption of Stationarity:
Some Bayesian time series models assume stationarity (constant statistical properties over time).
In practice, capacity fluctuations may exhibit non-stationary behavior (e.g., trends, seasonality).

#### Model Complexity vs. Parsimony:
Bayesian models can become overly complex if too many parameters are included.
Balancing model complexity with parsimony is essential to avoid overfitting.

#### Updating Models Over Time:
Incorporating new data into Bayesian models requires re-estimating posterior distributions.
Real-time updates can be computationally intensive.
Despite these limitations, Bayesian models remain valuable tools for handling uncertainty, incorporating prior knowledge, and making informed predictions. When using Bayesian methods, it’s essential to address these challenges appropriately and communicate results transparently. 



**How can I address model misspecification in Bayesian LPA forecasting?
What are the alternatives to MCMC for estimating posterior distributions?
Can you explain how to perform sensitivity analysis on priors in a Bayesian model?What are the legal implications of capacity fluctuations in LPAs?
Can you provide an example of a sensitivity analysis for LPA applications?**



### Model Misspecification in Bayesian LPA Forecasting:
Model misspecification occurs when the chosen Bayesian model does not accurately represent the underlying process (e.g., capacity fluctuations).To address this:

#### Prior Sensitivity Analysis: 
Explore different prior distributions for model parameters. Assess how changes in priors impact the posterior distribution and predictions.

#### Alternative Models: 
Consider alternative Bayesian models (e.g., different likelihood functions, non-parametric models) and compare their performance.

#### Gaussian-Process Approximations: 
Use Gaussian-process approximations to improve posterior estimates12.

#### Alternatives to MCMC for Estimating Posterior Distributions:

#### While MCMC is widely used, other methods exist:
Variational Inference: Solves an optimization problem to approximate the posterior faster than simple MCMC.
Importance Sampling: Estimates properties of posteriors by sampling from an approximation.
Analytical Solutions: In some cases, posterior distributions can be computed analytically34.

#### Performing Sensitivity Analysis on Priors in a Bayesian Model:
Sensitivity analysis assesses how changes in priors affect model outcomes.

##### Steps:
Define a range of prior values (e.g., mean, variance).
Run the model with different priors.
Observe how posterior distributions and predictions vary.
Compare estimated parameters and make conclusions based on context5.
Legal Implications of Capacity Fluctuations in LPAs:
LPAs grant decision-making authority to attorneys when the donor lacks capacity.
Legal implications:
Freezing of Accounts: Without an LPA, banks may freeze accounts if a signatory lacks capacity.
Deputyship Applications: If no LPA exists, a third party can apply to be appointed as a deputy by the Court of Protection.
Business LPAs: For business accounts, lacking an LPA can impact financial operations678.
Example of Sensitivity Analysis for LPA Applications:
Suppose we have an LPA model with priors for mean1 and mean2 (related to capacity).
Vary the priors (e.g., mean1, tau1, tau2) within reasonable ranges.
Observe how estimated parameters (e.g., A, mean1) change.
Conclude based on the impact of different priors on LPA decisions5.
Remember that sensitivity analysis helps assess the robustness of Bayesian models and informs decision-making. 




### Handling missing data in Bayesian models is essential for accurate inference. Let’s explore some approaches:
#### Conceptual Understanding of Missing Data:
Missing data can arise due to various reasons, such as design issues or factors beyond researchers’ control.
We’ll focus on a hypothetical regression problem where we predict voting intention (YY) using people’s age (XX).

### Types of Missing Data Mechanisms:

#### MCAR (Missing Completely at Random):
Missingness is unrelated to any research question.
Example: Interviewer accidentally erases responses (unrelated to age or voting intention).
Under MCAR, using cases with no missing values provides valid inferences and unbiased estimations.

#### MAR (Missing at Random):
Missingness depends on observed variables (e.g., XX) but not the unobserved outcome (YY).
Example: Older people more likely to give a missing response (related to XX).

#### NMAR (Not Missing at Random):
Missingness depends on unobserved factors (e.g., ZZ) related to neither XX nor YY.
Example: People with lower voting intention less likely to respond (related to YY itself).

#### Bayesian Approaches to Handle Missing Data:

##### Treat Missing Data as Parameters:
Assign priors to missing values (kid_score in our example).
Estimate their posterior distributions.
Incorporate all available information in the analysis.

##### Multiple Imputation:
Generate multiple imputed datasets by imputing missing values.
Analyze each dataset separately and combine results.

##### Bayesian origin: 
Impute missing values using predictive distributions.

##### Checking for MCAR:
Compare the distribution of XX for cases with and without missing data on YY.
If means and variances of XX are similar, it suggests MCAR.
Regression lines remain stable with or without missing data.
Remember that Bayesian models allow us to treat missing data as parameters, leveraging all available information. Multiple imputation is another powerful technique to handle missingness. Choose the approach based on the specific context and assumptions about missing data12. 



### Multiple imputation (MI) is a powerful technique for handling missing data, and incorporating it into a Bayesian framework provides a robust and flexible approach. Let’s explore how to perform multiple imputation within a Bayesian context:


#### Conceptual Understanding of Missing Data:
Missing data can arise due to various reasons, such as design issues or factors beyond researchers’ control.
In Bayesian modeling, we treat missing values as unknown parameters and estimate their posterior distributions.

#### Types of Missing Data Mechanisms:
There are three main types of missing data mechanisms:
MCAR (Missing Completely at Random): Missingness unrelated to any research question.
MAR (Missing at Random): Missingness depends on observed variables but not the unobserved outcome.
NMAR (Not Missing at Random): Missingness depends on unobserved factors unrelated to observed variables.

#### Bayesian Approach to Handling Missing Data:
Treat Missing Data as Parameters:
In Bayesian models, we incorporate missing data directly into the model.
Missing values become parameters with prior distributions.
The posterior distribution accounts for both observed and missing data.
This approach leverages all available information and avoids discarding cases with missing values.

#### Multiple Imputation (MI):
MI generates multiple synthetic datasets by imputing missing values.
Each dataset represents a plausible completion of the missing data.

#### Bayesian MI involves the following steps:
Impute Missing Values: Impute missing data using predictive distributions (e.g., regression models).
Analyze Each Imputed Dataset Separately: Perform Bayesian analysis on each imputed dataset.
Combine Results: Combine parameter estimates, credible intervals, and other inferences across multiple imputed datasets.

#### Account for Uncertainty: 
The variability across imputed datasets reflects the uncertainty due to missing data.

#### Benefits of Bayesian MI:
Incorporates Uncertainty: Bayesian methods naturally propagate uncertainty.
Integrates Prior Information: Prior distributions provide additional context.
Flexible and Robust: Handles different missing data mechanisms.
Valid Inferences: Provides valid parameter estimates and credible intervals.

#### Example Application:
Suppose we have a regression model predicting voting intention (YY) based on age (XX).
Impute missing YY values using Bayesian regression models.
Analyze each imputed dataset separately (e.g., compute posterior distributions for regression coefficients).
Combine results across imputed datasets to obtain overall parameter estimates.
Remember that Bayesian MI allows us to handle missing data while maintaining the richness of uncertainty. It’s a powerful tool for robust statistical inference.



### Bayesian multiple imputation is a powerful technique for handling missing data, but it relies on certain assumptions. Let’s explore these assumptions:
#### Missing at Random (MAR):
The MAR assumption is crucial for multiple imputation.
It implies that the probability of missingness depends only on observed variables (not the unobserved outcome) after accounting for other observed variables.
In other words, missingness is related to the available information in the dataset.
If data are MAR, imputing missing values based on observed variables can lead to unbiased parameter estimates.

#### Predictive Model Assumption:
Bayesian multiple imputation imputes missing values using predictive models.
The assumption is that the predictive model accurately captures the relationship between observed and missing data.
If the model is misspecified, imputed values may be biased.

#### Assumption of Ignorable Missingness Mechanism:
Ignorable missingness means that the missing data mechanism does not introduce systematic bias.
If data are MCAR or MAR, the missingness mechanism is considered ignorable.
Ignorable missingness allows valid inferences using multiple imputation.

#### Appropriate Choice of Imputation Model:
Selecting an appropriate predictive model for imputation is essential.
The model should reflect the underlying data-generating process.
Consider linear regression, logistic regression, or other relevant models.

#### Sufficient Number of Imputations:
Multiple imputation generates several imputed datasets.
The number of imputations affects the precision of estimates.
More imputations reduce uncertainty due to missing data.

#### Assumption of Exchangeability:
Exchangeability assumes that the imputed datasets are exchangeable (i.e., interchangeable).
This allows combining results across imputed datasets.
In practice, exchangeability is often reasonable.

#### Sensitivity to Prior Distributions:
Bayesian imputation involves specifying prior distributions for model parameters.
Sensitivity analysis explores how different priors impact results.
Robustness to prior choices is desirable.
Remember that while Bayesian multiple imputation is a powerful tool, understanding and validating these assumptions are critical for reliable results

# ############################################################################################################################################## #
# Incorporating the demands and uncertainties of the COVID period into both long-term and short-term forecasting for LPA applications at the OPG
* how to incorporate covid period demands and uncertainty around the data in long-term and short-term forecasting of demands(Living Power of Authorney (LPA) applications in Office of Public Guardian (OPG)) to provide accurate forecats for the LPA demands?

*Note: By combining these strategies, you can create a more robust and adaptable forecasting model that accounts for the unique challenges posed by the COVID period and beyond; forecasting is not about predicting the future with certainty but about preparing for it with flexibility and insight.

## Data Analysis: 
Begin by analysing historical data, but with a focus on identifying patterns that emerged specifically during the COVID period. 
This includes changes in application rates, processing times, and any other relevant metrics.

## Scenario Planning: 
Develop multiple forecasting scenarios to account for various levels of COVID-19 impact and recovery rates. This approach helps in preparing for different possible futures.

## Continuous Monitoring: 
Set up a system for continuous monitoring of demand signals and indicators that could suggest shifts in LPA application rates.

## Feedback Loop: 
Create a feedback loop where the forecast is regularly compared against actual demand, and adjustments are made accordingly.

## Stakeholder Communication: 
Keep communication open with stakeholders to understand potential changes in demand due to policy shifts or public sentiment.

## Technology Adoption: 
Embrace digital solutions that can streamline the application process and potentially alter demand. 
The OPG has plans to allow for completely online LPA applications, which could change the demand landscape3.

## Resilience Building: 
Invest in building resilience into your models to account for decremental demand causal factors, such as health warnings or other emergencies2.


## Demand Intelligence: 
Utilise demand intelligence tools and data science models to incorporate real-time data and predictive analytics into your forecasts. 
This can help in understanding the impact of current events on demand.

*how to Utilise demand intelligence tools and data science models to incorporate real-time data and predictive analytics into forecasts, to help in understanding the impact of covid period on demand (Living Power of Authorney (LPA) applications in Office of Public Guardian (OPG)) in long-term forecasting model (cohort-based model) and short-term (exponential smoothing). 

*Which machine learning techniques can be used to incorporate the impact of covid period demands (e.g., mortality rate, population projection, number of LPA applications) and uncertainty around the data in long-term and short-term forecasting of LPA demands to provide accurate forecats for the LPA demands?

* ref: https://www.mckinsey.com/capabilities/operations/our-insights/ai-driven-operations-forecasting-in-data-light-environments

Incorporating demand intelligence tools, data science models, and machine learning techniques into your long-term and short-term forecasting for Living Power of Attorney (LPA) demands can significantly enhance your understanding of demand patterns. 



## External Factors: 
Consider external factors that could influence demand, such as changes in legislation, economic conditions, and societal trends. 
The Powers of Attorney Act 2023, for example, aims to digitize the LPA process, which could affect demand patterns1.


**Incorporating external factors into your forecasting model is a multi-step process that enhances the model’s accuracy and robustness.**
* How can I incorporate external factors to deal with covid-period effects on the outcome into a LPA demands long-term forecating model using cohort model in excel as well as LPA demands short-term forecating model using exponentional smoothing model in excel?

*By following the following steps, you can create a forecasting model that not only reflects historical trends but also adapts to the dynamic nature of external influences, providing a more accurate forecast for LPA demands: 

### Identify Relevant Factors: 
Determine which external factors are likely to influence the demand for LPA applications. This could include economic indicators, demographic trends, policy changes, and health advisories.

### Data Collection: 
Gather data on these factors over a period that aligns with your historical demand data. This will help in establishing correlations.

### Feature Engineering: 
Transform these external factors into features that your model can interpret. 
For example, you can create binary flags for events (like a pandemic onset) or continuous variables for economic indicators1.

### Model Integration: 
Use statistical models like ARIMA (Autoregressive Integrated Moving Average) or advanced techniques like machine learning algorithms 
to integrate these features into your forecasting model. This could involve adding the features as additional variables in your dataset2.

### Scenario Analysis: 
Develop scenarios based on different combinations and intensities of external factors to see how they would impact demand.

### Model Training: 
Train your model using the historical data along with the new external features. This will allow the model to learn the relationship between these factors and LPA demand.

### Validation and Testing: 
Validate your model against a separate dataset to ensure it accurately predicts demand considering the external factors.

### Continuous Improvement: 
Regularly update your model with new data and review the external factors to ensure they remain relevant and accurately represented in the model.

### Monitor Real-Time Data: 
Use real-time data to adjust your forecasts promptly. This helps in responding quickly to sudden changes in external conditions3.


## How can I incorporate external factors to deal with covid-period effects on the outcome into a LPA demands long-term forecating model using cohort model in excel as well as LPA demands short-term forecating model using exponentional smoothing model in excel? 

Incorporating external factors to address the effects of the COVID-period on outcomes into both long-term and short-term forecasting models for LPA demands in Excel requires a structured approach. 

### Long-Term Forecasting Using a Cohort Model in Excel

#### Identify External Factors: 
Determine which external factors such as government policies, economic conditions, or public health advisories impacted LPA demands during the COVID period.

#### Data Collection: 
Collect data on these factors for the period you are analysing.

#### Cohort Analysis: 
Group your data into cohorts based on the time period of LPA applications. This could be monthly or quarterly cohorts.

#### Regression Analysis: 
Use regression analysis to understand the impact of external factors on each cohort1.

#### Adjust Cohorts: 
Adjust the cohort data based on the regression analysis to reflect the impact of COVID-period effects.

#### Forecasting: 
Use the adjusted cohort data to forecast long-term demand. You can use Excel’s built-in functions or create a custom model using the cohort data.


### Short-Term Forecasting Using an Exponential Smoothing Model in Excel


#### Time Series Data: 
Organize your LPA demand data in a time series format suitable for exponential smoothing.

#### External Factor Adjustment: 
Integrate external factors by adjusting the smoothing factor or by adding a correction term to the forecast equation based on the impact of these factors2.

#### Forecasting: 
Apply the exponential smoothing formula to forecast short-term demand. The formula in Excel would look something like this:Forecast=α×Actual+(1−α)×Previous Forecast

#### Model Validation: 
Compare your forecasts against actual data to validate the model and adjust as necessary.

*Note: the key to successful forecasting is not only in the technical application of these models but also in the continuous refinement and adjustment based on new data and changing external conditions. 
Regularly update your models to incorporate the latest data and external factors to maintain accuracy in your forecasts.

#### Smoothing Factor: 
Determine the smoothing factor (α) that gives more weight to recent observations.

*How do I choose the right smoothing factor (α)?
Choosing the right smoothing factor (α) for exponential smoothing is crucial as it determines how much weight is given to recent observations in the forecasting model.

**Guidelines to help you select an appropriate α:**

##### Understand the Range: 
The smoothing factor α ranges from 0 to 1. A value close to 1 gives more weight to recent observations, making the forecast more responsive to changes. 
Conversely, a value close to 0 makes the forecast more stable and less sensitive to recent fluctuations1.

##### Historical Data Analysis: Look at your historical data. If the data shows that recent trends are a good predictor of future values, 
consider a higher α. If the data is more random or if older values are also important, consider a lower α2.

##### Error Measurement: 
Use error metrics such as Mean Squared Error (MSE) to evaluate the accuracy of forecasts with different α values. 
The α that minimizes the error is typically the best choice3.

##### Trial and Error: 
Start with a value of α, such as 0.5, and adjust it incrementally. Observe how these adjustments affect the forecast accuracy and adjust accordingly4.

##### Model Validation: 
Validate your chosen α by comparing the model’s forecasts against actual outcomes. Adjust the α if the model’s performance can be improved1.

##### Consider External Factors: 
If your model needs to respond quickly to external shocks, such as those caused by the COVID-period, a higher α might be necessary. 
However, be cautious as a high α can also make the model react to random noise2.

##### Use Optimization Techniques: 
Some software packages can automatically optimize α based on historical data. 
In Excel, need to manually test different α values or use Solver to find the optimal value1.
Remember, there is no one-size-fits-all value for α, and it may need to be adjusted over time as the characteristics of the data change. 
It’s important to regularly review and potentially update the smoothing factor to ensure your forecasts remain accurate.

# Which alternative method works the best for the LPA demands forecasting model to deal with covid-period effects on the outcome?

When considering alternative methods for forecasting LPA demands, especially in the context of the COVID-period effects, 
it’s important to choose a method that can adapt to rapid changes and incorporate various external factors. 

*Note: Each of the following methods has its strengths and can be chosen based on the specific needs of your forecasting model, the availability of data, and the level of complexity you’re willing to manage. It’s also beneficial to combine different methods to create a hybrid model that leverages the advantages of each approach.

## Consumer Sentiment Models: 
Incorporating consumer sentiment into models can be particularly effective. This involves using qualitative data on consumer behavior and attitudes, 
which can be critical during unpredictable periods like the COVID-19 pandemic1.
* ref: https://hbr.org/2020/11/a-better-model-for-economic-forecasting-during-the-pandemic
Scenario Analysis: Create scenarios based on different sentiment trends to understand how extreme changes in consumer sentiment could affect LPA demand.

## SPRINT Re-plan Approach: 
McKinsey suggests a SPRINT re-plan approach for rapidly forecasting demand during crises. 
This involves tracking shifts in consumer behavior across several dimensions and adjusting commercial strategies accordingly2.
* ref: https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/rapidly-forecasting-demand-and-adapting-commercial-plans-in-a-pandemic

## Adaptive Short-Term Models: 
For short-term forecasting, adaptive methods like Generalized Additive Models (GAM) or machine learning algorithms can be useful. 
These models can adjust quickly to new data and are capable of handling non-linear relationships4.
* ref: https://ieeexplore.ieee.org/stampPDF/getPDF.jsp?tp=&arnumber=9382417
* ref: https://hbr.org/2020/11/a-better-model-for-economic-forecasting-during-the-pandemic
* ref: https://www.mckinsey.com/industries/consumer-packaged-goods/our-insights/rapidly-forecasting-demand-and-adapting-commercial-plans-in-a-pandemic

## Simple Models with Lift Adjustment:
In times of disruption, simple models like lift-adjusted seasonal naive methods are recommended. 
These models measure change from the baseline at higher levels of hierarchy and then propagate this lift to lower levels5.

## Enhanced Long-Term Models: 
For long-term forecasting, models that capture the physics of transmission, project human behavioral reactions, 
and reset state variables to account for randomness have been found to correlate with better predictions3.

**How do I incorporate Enhanced Long-Term Models into my cohort forecasting model?**
Incorporating Enhanced Long-Term Models into your cohort forecasting model involves integrating features that have been identified as beneficial for long-term prediction accuracy.
By incorporating these features into your cohort forecasting model, you can enhance its long-term predictive power and 
make it more responsive to the complexities introduced by the COVID-period effects and other external factors.
* ref: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010100
* ref: https://towardsdatascience.com/forecasting-with-cohort-based-models-e71003bc7ecd

### Capture the Physics of Transmission: 
Incorporate mechanisms that reflect the actual process of LPA application and approval.
This could involve understanding and modeling the flow of applications through different stages and the factors that influence transition rates at each stage1.

### Project Human Behavioral Reactions:
Include variables that account for how people’s behaviors might change over time in response to external events, such as policy changes or public health crises.
This can be done by analyzing past behaviors in similar situations or by conducting surveys1.

### Reset State Variables: 
Before making long-term projections, reset the state variables in your model to account for randomness and uncertainty not captured in the model. 
This might involve re-evaluating initial conditions or incorporating stochastic elements into the model1.

### Data Transformation: 
Reformat your time series data into tabular data that aligns with cohorts based on registration or application dates. 
This allows you to apply regression models that can offer additional insights regarding the attribution of future LPA demands to specific cohorts2.

### Model Enhancement: 
Consider using lightweight models enhanced with hierarchical decomposition, which can provide precise forecasting with fewer computations and parameters. 
This approach can be particularly useful when dealing with large datasets or complex systems3.
* ref: https://arxiv.org/abs/2401.11929

### Behavioral Feedbacks: 
Integrate endogenous behavioral responses into your model. 
This means that the model should allow for the perceived risk or awareness of LPAs to continuously change the demand through the adoption and relaxation of various behaviors1.

**How do I incorporate Behavioral Feedbacks into my cohort forecasting model?**
Incorporating enhanced behavioral feedbacks into your cohort forecasting model involves integrating behavioral dynamics that can influence the demand for LPAs. 
By following these steps, you can enhance your cohort forecasting model to more accurately reflect the dynamic nature of human behavior and its impact on LPA demand.
* ref: https://journals.plos.org/ploscompbiol/article?id=10.1371/journal.pcbi.1010100
* ref: https://towardsdatascience.com/forecasting-with-cohort-based-models-e71003bc7ecd

#### Behavioral Data Collection: 
Gather data on behaviors that are likely to impact LPA demand, such as changes in legal advice seeking, public awareness of LPAs, and shifts in health-related behaviors due to COVID-19.

#### Quantify Behaviors: 
Convert qualitative behavioral data into quantitative metrics. 
For example, use survey data to create indices representing the level of public awareness or concern about health issues.

#### Cohort Segmentation: 
Segment your cohorts based on behavioral characteristics. This could mean creating sub-cohorts within your data that reflect different behavioral responses.

#### Modeling Behavioral Trends: 
Use regression analysis or other statistical methods to model how these behaviors have impacted LPA demand historically. 
This will help you understand the relationship between behavior and demand1.

#### Incorporate Feedback Loops: 
Create feedback loops in your model where the demand for LPAs influences future behaviors, which in turn affect future demand. 
This can be done by setting up equations or algorithms that simulate this interaction.

#### Adjust for COVID-19 Effects: 
Specifically adjust your behavioral feedbacks to account for the unique impacts of the COVID-19 period. 
This may involve analyzing how behaviors changed during the pandemic and integrating this into your model.

#### Scenario Analysis: 
Run scenario analyses to see how different behavioral responses could impact LPA demand. 
This helps in understanding the potential range of outcomes and preparing for various possibilities.

#### Continuous Updating: 
Keep your model updated with the latest behavioral data to ensure that the feedbacks remain relevant and accurate.

#### Validation and Testing: 
Regularly validate and test your model against actual data to ensure that the behavioral feedbacks are correctly influencing the forecast.

### How to use SARIMA method for the LPA demands short-term and long-term forecasting model to deal with covid-period effects on the outcome and deal with uncertatinty?
The SARIMA (Seasonal Autoregressive Integrated Moving Average) method is a powerful tool for forecasting time series data that exhibits seasonal patterns. It’s particularly useful for dealing with uncertainties like those introduced during the COVID-period. 
By following these steps, you can create a robust SARIMA forecasting model that accounts for both seasonal patterns and the uncertain effects of the COVID-period on LPA demand outcomes. Remember, the key to effective forecasting is not only in the initial model development but also in ongoing model refinement and adaptation to new data.

**Using SARIMA for both short-term and long-term forecasting of LPA demands:**
Understand SARIMA: 
SARIMA extends the ARIMA model by including seasonal terms. It is represented as SARIMA(p, d, q)(P, D, Q, s), where:
( p, d, q ) are the non-seasonal orders for autoregression, differencing, and moving average, respectively.
( P, D, Q ) are the seasonal orders for autoregression, differencing, and moving average.
( s ) is the number of periods in a season1.

#### Data Preparation: 
Organize your LPA demand data into a time series format. Include a timestamp for each data point to identify seasonal patterns.

#### Stationarity Check: 
Ensure your data is stationary, meaning its statistical properties do not change over time. Use differencing to stabilize the mean if necessary.

#### Identify Seasonality: 
Determine the seasonality in your data (e.g., monthly, quarterly) and use seasonal differencing if required to remove seasonal trends and achieve stationarity.

#### Model Selection: 
Choose the SARIMA model parameters (p, d, q, P, D, Q, s) based on your data’s autocorrelation and partial autocorrelation functions. You may need to experiment with different combinations to find the best fit.

#### Incorporate COVID-period Effects: 
To account for the COVID-period effects, you can include dummy variables representing pre-COVID, during-COVID, and post-COVID periods or use external regressors that capture related impacts.

#### Uncertainty Handling: 
Use the confidence intervals provided by the SARIMA model to understand the range of possible outcomes. This helps in dealing with uncertainty in your forecasts.

#### Model Fitting: 
Fit the SARIMA model to your historical LPA demand data, including any COVID-period effects you’ve identified.

#### Validation: 
Validate your model by comparing its forecasts against actual data. Adjust the model parameters if necessary to improve accuracy.

#### Forecasting: 
Once validated, use the SARIMA model to forecast short-term and long-term LPA demands. The model will provide a point forecast along with confidence intervals for each predicted value.

#### Update Regularly: 
Continuously update your model with new data to refine the forecasts and adjust for any changes in trends or seasonal patterns.

### **How do I choose the right SARIMA parameters?**
Choosing the right parameters for a SARIMA model is a critical step in time series forecasting. , the goal is to find a parsimonious model 
that adequately captures the patterns in the data without overfitting. It’s a balance between model complexity and forecast accuracy123.
Here’s a structured approach to selecting the appropriate parameters:

#### Seasonal Identification: 
Determine if your data exhibits a strong seasonal pattern and identify the length of the season (s). This could be based on domain knowledge or exploratory data analysis.

#### Stationarity Check: 
Ensure that your time series is stationary, as SARIMA requires this. You may need to apply differencing to achieve stationarity.

#### ACF and PACF Analysis: 
Use Autocorrelation Function (ACF) and Partial Autocorrelation Function (PACF) plots to get initial estimates of the parameters. The ACF shows the correlation of the time series with its own lagged values, while the PACF shows the partial correlation of the time series with its own lagged values, controlling for the values of the time series at all shorter lags.

#### Parameter Estimation:
Non-seasonal parameters (p, d, q): Look for the lag after which the PACF cuts off for the AR parameter (p), and the lag after which the ACF tails off for the MA parameter (q). The differencing parameter (d) is determined based on the number of differences required to achieve stationarity.
Seasonal parameters (P, D, Q): Similar to the non-seasonal parameters, but you look at the seasonal lags in the ACF and PACF plots. For example, if your data has a seasonal period of 12, you would look at lags 12, 24, 36, etc.

#### Model Fitting: 
Fit the SARIMA model with the chosen parameters and evaluate its performance. Look at the AIC (Akaike Information Criterion) or BIC (Bayesian Information Criterion) values to compare different models.

#### Grid Search: 
Perform a grid search over a range of parameter values to find the optimal combination that minimizes the AIC or BIC.

#### Residual Analysis: 
After fitting the model, analyze the residuals to ensure that there are no patterns (which would suggest that the model can be improved) and that the residuals are approximately normally distributed.

#### Validation: 
Validate the model using a hold-out sample or cross-validation to ensure that it performs well on unseen data.

#### Iterative Refinement: 
It’s often an iterative process. You may need to go back and forth adjusting the parameters and refitting the model until you find the best parameters for your specific dataset.



### **How to use LSTM method for the LPA demands short-term and long-term forecasting model to deal with covid-period effects on the outcome and deal with uncertatinty?**
Using the LSTM (Long Short-Term Memory) method for forecasting LPA demands can be particularly effective for capturing complex patterns and dealing with uncertainties, 
such as those introduced during the COVID-period. 
Applying LSTM for both short-term and long-term forecasting:

#### Data Preparation: 
Organize your LPA demand data into a sequence that can be used for training the LSTM model. This includes normalizing the data and possibly transforming it into a supervised learning problem.

#### Feature Selection: 
Choose relevant features that could influence LPA demands, including historical demand data, COVID-period indicators, and possibly external factors like economic indicators or policy changes.

#### Model Architecture: 
Design your LSTM network architecture. This typically involves defining the number of layers, the number of neurons in each layer, and the connections between the layers.

#### Incorporate COVID-period Effects: 
Integrate COVID-period effects by including them as input features or by creating a separate model that specifically predicts the impact of COVID-related variables on LPA demands.

#### Train the Model: 
Use historical data to train your LSTM model. This involves feeding the input features into the network and adjusting the weights through backpropagation based on the error between the predicted and actual values.

#### Validation: 
Validate your model using a separate dataset to ensure that it generalizes well to new, unseen data.

#### Uncertainty Handling: 
To deal with uncertainty, you can use techniques like Monte Carlo simulations or Bayesian methods to get a distribution of possible outcomes rather than a single point estimate.

#### Forecasting: 
Use the trained LSTM model to forecast future LPA demands. For short-term forecasting, you might use a smaller window of historical data, while for long-term forecasting, 
you would use a larger window to capture more trends and cycles.

#### Model Updating: 
Regularly update your model with new data to capture the latest trends and improve the accuracy of your forecasts.

#### Interpretation: 
Interpret the model’s outputs carefully, considering the confidence intervals or prediction intervals to understand the range of possible future scenarios.
LSTM models are powerful because they can capture long-term dependencies and are capable of learning patterns in time series data, which is essential when dealing with the irregularities and uncertainties of the COVID-period123. To monitor the performance of your LSTM model and be prepared to adjust the architecture or retrain the model as more data becomes available or as the situation evolves.

### **How do I choose the right architecture for my LSTM model?**
Choosing the right architecture for your LSTM (Long Short-Term Memory) model is essential for effective time series forecasting. 
Select the appropriate architecture for your LPA demands forecasting model:

#### Define Your Problem: 
Understand the specifics of your forecasting task, including the nature of the LPA demand data, the impact of the COVID-period, and the level of uncertainty.

#### Data Preprocessing: 
Prepare your data by normalizing or standardizing it, and structure it into sequences that are suitable for LSTM.

#### Determine Sequence Length: 
The length of the input sequences should capture the relevant temporal dependencies. For LPA demands, consider the typical cycles and seasonality.

#### Select Number of Layers: 
Start with one or two LSTM layers. Deep LSTMs, with more layers, can model more complex patterns but may also require more data and training time.

#### Choose Number of Neurons: 
The number of neurons in each layer should reflect the complexity of the problem. More neurons can capture more information but can also lead to overfitting.

#### Decide on Dropout: 
Implement dropout to prevent overfitting, especially if you have a lot of data or a complex model.

#### Batch Size and Epochs: 
Choose a batch size and number of epochs that balance the speed of learning with the stability of the convergence.
Optimization and Loss Functions: Select an optimizer like Adam or RMSprop, which are generally good choices for LSTMs. 
Use a loss function that matches your specific forecasting objective, such as mean squared error for regression tasks.

#### Regularization: 
Apply L1 or L2 regularization if you’re dealing with overfitting.

#### Hyperparameter Tuning: 
Use techniques like grid search, random search, or Bayesian optimization to systematically explore different model architectures.

#### Validation Strategy: 
Use a hold-out validation set or k-fold cross-validation to evaluate the performance of different architectures.

#### Model Evaluation: 
Assess the model using appropriate metrics for forecasting, such as MAE (Mean Absolute Error) or RMSE (Root Mean Squared Error).

#### Iterative Refinement: 
It’s often an iterative process. You may need to adjust the architecture based on the performance of the model and refine it until you achieve satisfactory results.
There’s no one-size-fits-all architecture for LSTM models. It’s a process of experimentation and refinement to find the architecture that works best for your specific dataset and forecasting needs123. 
Be prepared to iterate and possibly combine different approaches to handle the complexities introduced by the COVID-period effects.


&nbsp;
<a name="ap-detailed"></a> 
# Managing files on the Analytical Platform
- a detailed instructions on setting up AP, Git and s3 access
At the beginning of every session on the AP:

1\. Log into the Analytical Platform

<https://alpha-analytics-moj.eu.auth0.com/login?state=EIOAObXDnk0d1tFgU6fbtnk1ditbmwoc&client=oUb1V330oXKyMpTagAYDzWDY10U4ffWF&protocol=oauth2&prompt=true&scope=openid%20email%20profile%20offline_access&response_type=code&redirect_uri=https%3A%2F%2Fcpanel-master.services.alpha.mojanalytics.xyz%2Fcallback&sessionKey=oidc%3Aalpha-analytics-moj.eu.auth0.com>

2\. Log into AWS:

<https://alpha-analytics-moj.eu.auth0.com/login?state=VqVz4r7DsapzNRWrZ1HqTXJ3SzYoJjVx&client=NpfImg4P3ynU6HFx7ivYmqUZWQHfwi3Y&protocol=samlp>

Log into Github:

<https://github.com/moj-analytical-services>

Guidance on coding standards and platform guidance are pinned to the top of the front page.

```
To create a repo

1\. Log in to Github

2\. Create new repository

3\. Add folders in standard configuration

Clone the repo in Jupyter

1\. Open Jupyter from the Analytical Platform control panel

2\. Clone the Github repo from the shell by typing:

git clone <git@github.com>:moj-anlaytical-services/&lt;your repo&gt;.git

This downloads the repository if not in the local system. It also allows the AP to co-ordinate updates to the Github when you “push” updates to Github. You should see the repo as a folder both in R-Studio and Jupyter.

Or clone the repo in R-Studio

On Github, click the Clone or Download button and copy the SSH key.

In R, go to the Git panel:

File -> New project-> Version control -> Git

Paste SSH key here.

The repo should be seen in the local folder path and a Git tab should appear in the top right window.

Git commands in the Jupyter UNIX shell

git status

Shows a status report of all the files added to the current tracked list as well as any known untracked files.

git branch

Shows all local branches (branches in your UNIX shell)

git branch -a

Shows all available branches

git branch &lt;branch name&gt;

Creates a new local branch with specified name

git branch -d &lt;branch name&gt;

Deletes local branch of specified name

git checkout &lt;branch name&gt;

Makes &lt;branch name&gt; the current branch. Existing adds will be remembered. Any further adds will be to this branch only.

git checkout -b &lt;branch name&gt;

Creates a new branch with the specified name and makes that branch the current branch (i.e. simultaneously performs a branch and a checkout.

git add &lt;filename1&gt; &lt;filename2&gt;

Adds listed files to the tracked list (if not on the list already) and adds the same files to a list for the next commit

git add -u

Adds all tracked files to the list for the next commit

git add &lt;folder name&gt;/\*

Adds the specified folder and all files and folders therein to the tracked list and to the list for the next commit.

git fetch

Checks what changes have been made to your repo at GitHub

git commit -m “&lt;message&gt;”

Commits all adds since the last commit to the bundle to be pushed to GitHub. Specified message to appear on GitHub with this commit.

git push origin &lt;GitHub branch name&gt;

Pushes everything in the latest commit to the specified branch on GitHub (or creates a new branch there, if not already created).

git pull origin &lt;GitHub branch name&gt;

Pulls new content from the specified GitHub branch into the current local branch.

The Git flow

Step 0: Clone an existing repository from GitHub. (See above).

Step 1: Create a new local branch (and optionally view current status report).

git branch tmp1

git checkout tmp1

(git status)

Step 2: Add modified files (and optionally view current status report).

git add -u

(git status)

Step 3: Commit added files to the commit bundle.

git commit -m “This is my latest commit”

git (status)

Step 4: Push commit bundle to GitHub.

git push origin tmp1_GH

Step 5: Login to GitHub, view changes and pull the new branch into the master. (See ‘Compare and Pull Request’ and the ‘Merge Pull Request’ buttons. Delete the temporary branch.

Step 6. Return to Jupyter and leave the local temporary branch.

git checkout master

Step 7: Pull the master from GitHub into the local master clone.

git pull origin master

Step 8: Delete the local temporary branch.

git branch -d tmp1

AP guidance:

<https://moj-analytical-services.github.io/platform_user_guidance/quick-start.html>

AP principles guidance:

<https://github.com/moj-analytical-services/data_warehouse_database_template>

ETL Manager guidance:

<https://github.com/moj-analytical-services/etl_manager>

Robin’s data engineering principles:

<https://docs.google.com/document/d/1tJShbVnZqW8X8ULCAsHVx1y6dbFp1MFsnWFxBBzvpw8/edit?ts=5b90f868#heading=h.h191f44swt4c>

The general Git flow

<https://docs.google.com/presentation/d/1dRhbprKugJUrN39AKdmSitSaw7dnRaAZROJlymXSQ-U/edit?usp=sharing>
```

&nbsp;