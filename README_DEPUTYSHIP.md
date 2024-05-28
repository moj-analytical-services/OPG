# Demand Forecasts for Deputyship

What we initially need to do is get an update of the available deputyship data. What we need to know is:
1. The current active caseload ie those cases under active supervision
we we needed the database of the active caseload so yeah caseload is it those people who've got deputyships who were there still active and they all subject to active supervision by OPG.
So they're the people that well either be being charged a fee supervision of affair cases some of the well received full exemptions or missions but not all of them and that is one of the things that we need to try and forecast.

The reason for forecasting is that OPG needs to estimate the income generated from their fees. In addition, it affects the balance between LPA fees and deputyship fees. The reason behind this is that one of tasks that OPG currently do is the deputyship is partly subsidised by the LPA fee so depending on what that kind of balance is and kind of how much they subsidise e.g., the deputyship fee. Also the other reason they need to forecast is because they need to make sure they hve got enough staff in order to bond supervise the 50,000 plus deputyships are kind of and under active supervision.


2. The trend in the number of new deputyship orders

The active caseload there isn't a reason they need to forecast bar is because they obviously generating come from that

It the same time we need to forecast the numbers of new orders. It is a bit like the sort of stopped-flow module. In which, basically it is a bit like the bath where the active caseload is the bath of water when they got new orders (new cases deputyships) that are flooding into it.

The deputyships are made by the Court of Protection. It is usually cases where people cannot apply for a power of attorney so because they did not have one.

There are three kind of way that we could get a deputyships: 
1. Adults who lost their mental capacity because they did not have a power of attorney in which case the Court of Protection would order a deputy to act on your behalf.
2. Adults who never had have mental capacity. They have some sort of disability or some mental disability but did not have the capacity to make power of attorney and again the Court of Protection can order a deputy to act on your behalf and often in this case might be a local authority.
3. Childern born with a disability and they do not have anybody there especially make the Court of Protection to act on their behalf and have a deputyships. The deputyship can be a family member or power of atherney or local authority, financial advisor, and soliciter to act on behalf and mange their affairs. The difference in here is that the Court of Protection made the decision for ordering the deputyship and they do not have any choice about it.

## Deputyship Forecasting Model
Basically, the way the deputyships is forecasted is similar to a stopped-flow model, essentially we have got the active caseload in the middle, which is the kind of expert thank OPG synchronising it and we have got he got new cases flowing in aa new orders that the Court of Protection is making and then you got those cases that are terminated. They might terminate for a number of reasons, generally the people die and sometimes it might not be it might just simply be that the order is not renewed.  It is unlike the power of authorny which is lasting, e.g., if they have got a power of attheney unless they seek to remove that, which they can do e.g., if they divorced or just they do not want it anymore or their attorney dies or needed a new one. Thus, with the deputyship, they have to be renewed so the Court of Protection has to renew it and it has generally done about every three years. People could flow off the active caseload for number reasons: that is generally when people die but it could also be the court order is not renewed but you know the reasons why that would happen and they are pretty limited so this would normally give a deputyship to somebody unless they really lost capacity, so I suppose they could have a situation where somebody is in a coma or something else and when they recover and regain their consciousness or something else and then they do not need one anymore. Thus, they could have a situation like that and those cases that are flowing off and the balance between those cases coming on and those cases are flowing off is what is really the active caseloads in the middle. The model, the essence of the way it works is a basic assumption that if they have a power of attorney they do not need a deputyship and when they do not have a power attorney, they are at risk of needing a deputyship.  That assumptions is probably reasonable for most deputyships. Having said that, it does not cover every cases because it does not cover for those adults who could never get a power attorney so they are then at risk of needing her attention or for those children because they could never have a power of attorney as well in both cases they tend to be younger so again unlike power of attorney which tend to be very skewed towards older people. However, you could see the same sort of similarity in deputyships as well that they tend to be much older because most of the cases are people who have already taken out a deputyship but it is a bit bimodal as we could get a lot of deputyships for younger adults and not so many children. Thus, there is a bit of bimodality in there as well simply because and others younger people do nt have power of attorney often said of engaging more risky type behaviour OK I can binding motorbikes or jumping out aeroplanes or something and so berries he got a bit of bimodality around people are kind of in their early 20s because they had some sort of injury or life limiting injury that means they also require a deputyship.  The way the model is working at most cases is simply trying to obtain that estimate of how many living people have got power attorney away from the subtract that from the population to work out what is the population that do nt have have a power attorney and therefore might be at risk of needing a deputyship and in the other cases for the younger groups, and for the children, it it just sort of naive extrapolation. 


### Control Assuptions and Sensitivity Analysis:

* ref: SUPERVISION CONTROL ASSUMPTIONS (tab) in the excel model

To find out what data is available and how to access that, we would need to dig into new data to populate the model.

To simply the model, as there's a lot of redundancy in the excel model as there is as there was with the the LPA

The current model is expressing the numbers of new deputyship, this is trying to work out numbered of deputyship orders as a rate 1000 of the population without an LPA. 

The model is also looking at whatever the trend was in deputyship orders and calculating that as a rate per thousand population without an LPA.

In most the cases, it is generally going down. An explanation for this could be based on the assumption at the time (although we did not really know what happened subsequently) because more of the population of got LPA's that number is such a growing each year and it would reduce the population at risk of needing a deputyship and therefore we would expect the numbers of deputyship for the remaining rate is to go down.

We would need to adjust these control assupmtions and play around with what looks like a set of four sensitivity tests.

Manily on this controller is really what the key survival rates when we have got the deputyship data we can work now what are termination rates, when the order was made when somebody left the active caseload and on other orders were made and we can work out the period of time and how old they were when the order was made and when the case was terminated. In other words, we can work out what is the termination rate and it is a bit like mortality rate. So we can see the order that those termination rates tend to increase. 

Initially, it then sort of reflects something about the difference in the type of population because somebody in their 50s or 60s requiring a deputyship, probably because they have had an accident or something and they may be quite ill and so it's likely that they died quickly whithin the order was made. However, in some other reasons, they might have lost their mental capacity through dementia illness, thus, that was not terminal then there would live and bunch of other people who would survive for many years. Also, there are people who have had their deputyship for decades.

Because of these difference between cases, it could be very difficult to apply sort of simple mortality rates (as we did in LPA) to this deputyship dataset, because it's not the same sort of population.

We could simplify the model, so rather than putting such complexity of this a bit and made this a bit too complicated whereas the model, at the moment, tries to again treat the data as a cohort type of way where we sort of terminate people turning on their age overtime, 

but in reality it might be better as there is an argument that we could look a simple age-specific termination rate as that is not time-dependant, e.g., we simply consider if somebody is aged 50 or 60, what percentage of them terminate in any one year, rather than doing it in the sort of the cohort-based fashion and the reason for doing that might be that we could then track them over time better, so we can look if there are trends in the sort of termination rates which is much harder to pick out if we do it in this sort of cohort type of way so again there's sort of room for simplification in this.


*these are some extra assumptions that Paul must have put in here I could have come back to that 'cause I'm not quite sure what volumes of active caseload terminations that you deputyship has to come back to that*

We are trying to forecast new deputyship and the active caseload, to forecast the new deputyship before we can forecast the active case we need to know how many active so how many new deputyship are gonna flow into the active caseload.


Basically, the starting point is the population forecast, so this is the population minus living LPA holders so this is the whole point of calculating how many living LPA holders there are so for anybody aged 18+. It is basically taking the population and subtracting from it what the current estimate for the number of living out LPA holders is. 

and what's the relevance of forecasting and the number of living LPA holders, because this is obviously starting from 2018 but we would need to update this.

The LPA model is making a forecast of how many living LPA holders, so there will be obviously future LPA holders, so over time the numbers obviously go overtime that number will change.

There is nothing here for anyone under the age of 18 and that's because there are no LPA holders under the age of 18 or they shouldn't be that might be something or erroneously given at a younger age but that's that shouldn't be correct so there should be none.

This part of the sheet is just doing is simply taking that that information here about LPA holders minus living MBA holders and then categorising them into age groups see go population 18 plus minus living LPA holders sort of categorised by age and the reason and the reason for doing that is because it makes it obviously if you're trying to build some control assumptions around deputyships as a proportion of remaining people without an LPA and break that down down some age categories as it is been very hard to do it by single year of age.

this is a summary of the numbers of new deputyships each year by age group and this is really a summation of those two sheets, which Paul was using to try to estimate some of these figures, where we be good to kind of find out what the current status of the data is and whether it includes better historical data, so do we just need to rely on the information that we had after 2019 and we are just park that and added new data then or actually do we have that historical data now, so it might mean that we just need to park this historical data and then kind of add on to it if we've got new data since 2019 yeah, we could review this once once we have been able to kind of review the status of the day so that we have what it what it tells us.

To date this is a sort of summation of new deputyships orders, that there are obviously unde of age 18 are less than 200 so it is not a large number, it is the mother or obviously children born who need deputyships and volumes tend to increase with age the same way that kind of LPA do. 

As can be seen, there is a bit of a bimodal peak in the sort of 18 to 24, that may be partly due to risky behaviour, but it also could be whether one of the very first things the soldiers join the forces in the UK is that you are required to fill out their well and power attorney because if they go into if they were going into a compat zone and injured or died or they might lose mental capacity so they need somebody to act on their behalf and if they do not do that then obviously that might require them to have deputyship as well so that may be why there's also a peek here but it's probably more to do with the fact that you know 18 to 24 year olds often show more risky behaviour that's why they have you know they that's the group that has the highest accident rate with driving for example we don't you crash your car and they have a brain injury such that they called the column to self anymore then we know they're gonna require deputyships and we can see that in the data here. 

Essentially all what is happening here is working out this, how many deputyships there are here as a ratio or percentage of rate compared to the number of non LPA holders and this is information that's used in the controlled assumptions so this is when we're looking at these charts this is where that information is coming from it's over what that does is then generates a forecast for the number of new deputyships per 100,000 of the population without an LPA so if you if you generate that as a rate then you could then apply that for the LPA so create forecasts the size of population without an LPA. We have got rate and population to be multiplied with each other and to estimate the number of new deputyships. If there are estimsting there are 4 new deputyships in 2030, 100 thousand of polulation without LPA and we can work out how many new deputyships we expecting in 2030 and how many left without LPA?

In fact, for childern up to age 18 is more a nive extracolation of this figures and not worth doing much more coplicated work on that, as the number are very small. and so it is a simple exponential smoothing forecasting.

## Data Sources
The new deputyship data is now being recorded in Sirius. Previously, the deputyship “orders” had been recorded in the Sirius data that we received but this no longer seems to be the case, and what was recorded was not the level of detail previously available from CASREC (the database that previously captured deputyship data). 

For the previous data, please look at a file called “order1” derived from CASREC to give you an indication of the data fields actually required. 
 
We would need to find useful information like when the order was made whether, it's still active or not and we could work out the age of a **P: Protective People**.

The data should enables us to work out what the size of the active caseload is but also to work out the termination rate, how quickly people flow off the active caseload, so this whole issue with mortality rates. The termination refer to those records whether somebody dies or just leaves but the order is just not renewed. Thus, we would need to bounce calculator as well and that was very age dependent, generally the younger somebody is that termination rate is going to be lower.


## Deputyship Meta-data for the lagacy order data:

### The current CASRAC old Variables are listed below
1. Create: date of order was placed.

2. Order No: a ref that the Court of Protection is using.

3. Case: a unique identifier for one person and should be for a specific individual (same dob and postcode).

4. AppNo: nuber of orders for an individual and so the corrsponding case number.

5. Ord Stat
6. Ord Type
7. Desc
8. Made Date
9. Issue Date
10. Caseload Date
11. Sex
12. DOB
13. Postcode
14. Term Date
15. Term Type
16. Desc
17. Ord Risk Lvl
18. Remis
19. Exempt
20. Exempt Desc
21. Award Date
22. Order Cnt


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


### Active Caseloads (Under Active Supervision): Ord Stat = Active/Closed

So in other words, under active supervision by OPG and that is one of the things that we are trying to **forecast over the next sort of five to 10 years, how many active cases were there and how old are the people under active supervision?**

E.g., somebody was 20 years old when the original order was made, they've had an order for 15 years before they took before that order was terminated. So in other words, you can work out what is the probability that somebody aged 20 is going to have that order terminated after so many years.

1. When the order status (Ord Stat) is **Active**:
This is to answer the follwoing research question:
**1. The current active caseload ie those cases under active supervision**

This records are used to calculate how many active cases were there in the historical data. The the previous orders that were made is because what that tells you is when the original order was made and the reason that is useful is because you could then **cross reference that with the termination date**.


2. When the order status (Ord Stat) is **Closed**. 
This is to answer the follwoing research question:
**2. The trend in the number of new deputyship orders**

This records are used to calculate how old are the people under active supervision in the historical data. So in other words, we can work out how old the person was when.


In theory, these variables are used to identify all those cases with a complete record of all deputyships made, and you ought to be able to identify when the first order was made for that person, and in what year? So in other words, you ought to then be able to count how many new orders were made each year. The possible flaw with this has been, because there is often a delay in OPG recording in the legacy database (CASRAC), and when tried before with the current estimate of that figure, it is not clear how many order have been made in the last six months or 12 months for example, unless we have had to rely in the past on OPG giving us a separate account for that because it exists somewhere else on a separate database.

*Note: we get updated data and understand how currently being curated in Sirius?*

Here we break down how the stopped-flow technique can be related to the bathtub model and how it might apply to understanding and calculating the rate of new deputyships orders in the Office of Public Guardian (OPG) for active supervision with termination dates due to death or order closure. In summary, the stopped-flow technique and the bathtub model analogy provide insights into dynamic systems, whether in chemical reactions or administrative processes like managing deputyships orders. By applying these concepts, the OPG can better understand and manage its caseload, ensuring effective supervision and timely responses to changing circumstances.

##### Application of Bathtub Model Analogy to OPG Deputyships Orders:
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

##### Application of stopped-flow to OPG Deputyships Orders:
- Imagine using the stopped-flow technique to monitor the rate of new deputyships orders entering the OPG system.
- The “mixing chamber” in this case would represent the OPG’s processes for handling new orders.
- By observing the rate of incoming orders and the rate of terminated orders (due to death or closure), the OPG can calculate the net rate of change in active orders.
- This information is crucial for active supervision and resource allocation within the OPG.
- The analogy helps us understand how the system dynamics (flow rates, order numbers) impact the overall process.
* Ref: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_%28Physical_and_Theoretical_Chemistry%29/Kinetics/02%3A_Reaction_Rates/2.01%3A_Experimental_Determination_of_Kinetics/2.1.06%3A_Stopped_Flow
* Ref: https://chem.libretexts.org/Bookshelves/Physical_and_Theoretical_Chemistry_Textbook_Maps/Supplemental_Modules_%28Physical_and_Theoretical_Chemistry%29/Kinetics/02%3A_Reaction_Rates/2.01%3A_Experimental_Determination_of_Kinetics/2.1.06%3A_Stopped_Flow


It is exactly analogous to basically a bath that is being filled up with water with a tap, and water is flowing out of the bath at the same time. So what we have got is the active caseload, which is the water in the bath. The water that is flowing into the bath is the new deputyships. So these are the new cases that are being added to the active case load. So that's why we need to know to understand the trend in the active caseload is. So we can **predict how many new deputyships they are going to be? What is the flow of water going to be into this bath over the next five years?** And that generally there has been the assumption built into the model, which is how it links to the LPA stuff. The rate at which new Deputyships are generated. Is is going to be related to how many people do not have an LPA. 

For the vast majority of people, a deputyship is generated because they do not have an LPA. It is not entirely the case because obviously you have children, so you have children under the age of 18 who could never take out an LPA, but that number is quite small. However, there might also be adults, who do not have mental capacity, who may be required to take out or have a deputyship once they reached the age of 80. 

So anyway, just to complete that analogy with the bath the the other side of that of course is that if you imagine that water is flowing out of the bar through the plug hole, that's what the the termination bit is. So we have these people here who.

##### Control Assumption
The number of the deputyship cases should be equivalent to the subtracted the LPA number of the LP as from the population. So that is why we are subtracting the number, the cumulative total number of people, that have an LPA from the population, because that then tells us **what is the population at risk of needing a deputyship and how likely it is to generate a new, and at which rate?** e.g., if we know the rate in whitch from 100,000 people without an LPA generates 20,000 deputyships, we can work out what that rate is and how that rate is changing over time, as can be seen in the control assumptions. So the assumption is, if we dropped from 100,000 people without an LPA down to 50,000 people without an LPA, then we would expect the number of new deputyships to drop as well because the the population at risk of needing an LPA is less.
