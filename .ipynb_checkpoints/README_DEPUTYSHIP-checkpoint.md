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




CASREC


## Data Sources
The response from Stuart Stach was suggesting that the deputyship data is now being recorded in Sirius . Previously I had noted that deputyship “orders” had been recorded in the Sirius data that we received but this no longer seems to be the case, and what was recorded was not the level of detail previously available from CASREC (the database that previously captured deputyship data). 
 For the previous data, please look at a file called “order1” derived from CASREC to give you an indication of the data fields actually required. 
 What is needed is to go back to Stuart and others and obtain all of the data required to update the model.
 
We would need to find useful information like when the order was made whether it's still active or not and we could work out the age of a **P: Protective People**.

The data should enables us to work out what the size of the active caseload is but also to work out the termination rate, how quickly people flow off the active caseload, so this whole issue with mortality rates. The termination refer to those records whether somebody dies or just leaves but the order is just not renewed. Thus, we would need to bounce calculator as well and that was very age dependent, generally the younger somebody is that termination rate is going to be lower.

### Control Assuptions and Sensitivity Analysis:

* ref: SUPERVISION CONTROL ASSUMPTIONS (tab) in the excel model

To find out what data is available and how to access that.
We need to dig into new data to populate the model.

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

This part of the sheet is just doing is simply taking that that information here about LPA holders minus living MBA holders and then categorising them into age groups see go population 18 plus minus living LPA holders sort of categorised by age and the reason and the reason for doing that is because it makes it obviously if you're trying to build some control assumptions around deputyships as a proportion of remaining people without an LPA and break that down down some age categories as it is been very hard to do it by single year of age

this is a summary of the numbers of new deputyships each year by age group and this is really a summation of those two sheets, which Paul was using to try to estimate some of these figures, where we be good to kind of find out what the current status of the data is and whether it includes better historical data, so do we just need to rely on the information that we had after 2019 and we are just park that and added new data then or actually do we have that historical data now, so it might mean that we just need to park this historical data and then kind of add on to it if we've got new data since 2019 yeah, we could review this once once we have been able to kind of review the status of the day so that we have what it what it tells us.

To date this is a sort of summation of new deputyships orders, that there are obviously unde of age 18 are less than 200 so it is not a large number, it is the mother or obviously children born who need deputyships and volumes tend to increase with age the same way that kind of LPA do. 

As can be seen, there is a bit of a bimodal peak in the sort of 18 to 24, that may be partly due to risky behaviour, but it also could be whether one of the very first things the soldiers join the forces in the UK is that you are required to fill out their well and power attorney because if they go into if they were going into a compat zone and injured or died or they might lose mental capacity so they need somebody to act on their behalf and if they do not do that then obviously that might require them to have deputyship as well so that may be why there's also a peek here but it's probably more to do with the fact that you know 18 to 24 year olds often show more risky behaviour that's why they have you know they that's the group that has the highest accident rate with driving for example we don't you crash your car and they have a brain injury such that they called the column to self anymore then we know they're gonna require deputyships and we can see that in the data here. 

Essentially all what is happening here is working out this, how many deputyships there are here as a ratio or percentage of rate compared to the number of non LPA holders and this is information that's used in the controlled assumptions so this is when we're looking at these charts this is where that information is coming from it's over what that does is then generates a forecast for the number of new deputyships per 100,000 of the population without an LPA so if you if you generate that as a rate then you could then apply that for the LPA so create forecasts the size of population without an LPA. We have got rate and population to be multiplied with each other and to estimate the number of new deputyships. If there are estimsting there are 4 new deputyships in 2030, 100 thousand of polulation without LPA and we can work out how many new deputyships we expecting in 2030 and how many left without LPA?

In fact, for childern up to age 18 is more a nive extracolation of this figures and not worth doing much more coplicated work on that, as the number are very small. and so it is a simple exponential smoothing forecasting.
