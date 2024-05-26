"""
Name: Muhammad Tanveer
Email: muhammad.tanveer93@myhunter.cuny.edu
Resources: https://new.mta.info/coronavirus/ridership, https://github.com/nychealth/coronavirus-data/blob/master/trends/data-by-day.csv, https://github.com/nychealth/covid-vaccine-data/blob/main/doses/doses-by-day.csv, https://newbedev.com/seaborn-annotate-the-linear-regression-equation, https://www.stackvidhya.com/plot-correlation-matrix-in-pandas-python/
https://github.com/nychealth/coronavirus-data/tree/master/trends
https://coronavirus.health.ny.gov/covid-19-testing-tracker
https://new.mta.info/agency/new-york-city-transit/subway-bus-ridership-2019
https://www.cdc.gov/coronavirus/2019-ncov/whats-new-all.html
https://data.cityofnewyork.us/browse

Title: Understanding the Effects of Covid-19 and Vaccination Efforts on MTA Ridership
URL: https://tanveerm176.wixsite.com/data-viz


https://www.gradescope.com/courses/280182

"""

from numpy import fabs, true_divide
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from scipy import stats

from seaborn.utils import ci

#creating Dataframes from src CSV files
dailyCovidCases = pd.read_csv("data-by-day.csv")
vaccinationRates = pd.read_csv("doses-by-day.csv")
mtaRidership = pd.read_csv("MTA_recent_ridership_data_20211207.csv")


#MTA ridership was sorted in most recent date first 
#   reversed the sort
mtaRidership["Date"] = pd.to_datetime(mtaRidership.Date)
mtaRidership.sort_values(by="Date",inplace=True,ascending=True)
vaccinationRates["DATE"] = pd.to_datetime(vaccinationRates.DATE)

#create dataframes to extract needed data from original csv files
mod_vaccinationRates = pd.DataFrame()
mod_mtaRidership = pd.DataFrame()
mod_dailyCovidCases = pd.DataFrame()

#populated dataframes with apporpriate columns from original files
for i in mtaRidership.columns:
    if(i=="Date" or i=="Subways: Total Estimated Ridership"):
        mod_mtaRidership[i] = mtaRidership[i]

for i in dailyCovidCases.columns:
    if(i=="date_of_interest" or i=="CASE_COUNT"):
        mod_dailyCovidCases[i] = dailyCovidCases[i]
# print(mod_dailyCovidCases)

for i in vaccinationRates.columns:
    if(i=="DATE" or i=="ADMIN_ALLDOSES_DAILY"):
        mod_vaccinationRates[i] = vaccinationRates[i]
# print(mod_vaccinationRates)

#drop first row of Cases DF to have all start at 03/01/2020
mod_dailyCovidCases.drop([0],inplace=True)

#reset index of Ridership since it was sorted by Date
mod_mtaRidership.reset_index(drop=True ,inplace=True)


#----------------------------First plot: Ridership and Cases-----------------------------------#
ridershipCase_df = pd.DataFrame()
ridershipCase_df["Date"] = mod_mtaRidership.iloc[:,0]
ridershipCase_df["Daily Case Count"] = mod_dailyCovidCases.iloc[:,1]
ridershipCase_df["Daily Ridership"] = mod_mtaRidership.iloc[:,1]
ridershipCase_df["Date"] = ridershipCase_df["Date"].dt.strftime('%m/%d/%Y')

fig, ax1 = plt.subplots(figsize=(8,8))
ax1 = sns.barplot(x="Date", y ="Daily Case Count", data=ridershipCase_df,palette=["r"])
ax1.set_title('Daily Case Count vs Daily Ridership', fontsize=16)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Daily Case Count', fontsize=16, color="tab:red")

ax2 = ax1.twinx()
ax2 = sns.pointplot(x="Date",y="Daily Ridership", data=ridershipCase_df,color="blue",join=True,scale=0.3)
ax2.set_ylabel('Daily Ridership', fontsize=16, color="blue")

for index, tick in enumerate(ax1.get_xticklabels()):
    if index%40==0:
        tick.set_visible(True)
    else:
        tick.set_visible(False)

plt.show()


#----------------------------Second plot: Ridership and Vaccinations------------------------#
vaccinationRidership_df = pd.DataFrame()
vaccinationRidership_df["Date"] = mod_vaccinationRates.iloc[:,0]
vaccinationRidership_df["Daily Ridership"] = mod_mtaRidership.iloc[:,1]
vaccinationRidership_df["Daily Doses Administered"] = mod_vaccinationRates.iloc[:,1]

DailyVaccCount = vaccinationRidership_df["Daily Doses Administered"]
DailyRidership = vaccinationRidership_df["Daily Ridership"]

vaccinationRidership_df["Date"] = vaccinationRidership_df["Date"].dt.strftime('%m/%d/%Y')

fig, ax1 = plt.subplots(figsize=(8,8))
ax1 = sns.barplot(x="Date", y ="Daily Doses Administered", data=vaccinationRidership_df,color="red")
ax1.set_title('Vaccinations vs Daily Ridership', fontsize=16)
ax1.set_xticklabels(ax1.get_xticklabels(), rotation=40, ha="right")
ax1.set_xlabel('Date', fontsize=16)
ax1.set_ylabel('Daily Doses Administered', fontsize=16, color="tab:red")

ax2 = ax1.twinx()
ax2 = sns.pointplot(x="Date",y="Daily Ridership", data=vaccinationRidership_df,color="blue",join=True, scale=0.3)
ax2.set_ylabel('Daily Ridership', fontsize=16, color="blue")

for index, tick in enumerate(ax1.get_xticklabels()):
    if index%15==0:
        tick.set_visible(True)
    else:
        tick.set_visible(False)
plt.show()

#-----------------------------------Accurate Code for Figure 2-----------------------------------------------#
#This code relies on a miz of Excel, pandas and seaborn. However it is commented out.

# vaccRidership_Accurate = pd.DataFrame()
# vaccRidership_Accurate["Date Ridership"] = mod_mtaRidership.iloc[:,0]
# vaccRidership_Accurate["Daily Ridership"] = mod_mtaRidership.iloc[:,1]
# vaccinationRidership_df["Date Vaccinations"] = mod_vaccinationRates.iloc[:,0]
# vaccinationRidership_df["Daily Doses Administered"] = mod_vaccinationRates.iloc[:,1]

# vaccRidership_Accurate.drop(vaccinationRidership_df.index[0:288], inplace=True)



# vaccinationRidership_df.to_csv("testing.csv", index=False)
"""
The excel file "testting.csv" was manipulated in the following manner:
1. Cut and paste the rows of the Daily Doses Administered based on the start date of the Date Vaccinations.
    So that data for both of these columns would match the Daily Ridership and Date Ridership.
2. Delete the Date Vaccinations column and fill the cells of Daily Doses Administered with 0 for dates that 
    have no vaccination data (any date before 12/14/2020)
"""

# vaccRidership_Accurate = pd.read_csv("testing.csv")



#-------------------------------------Correlation Section------------------------------------#
#Caculate correlations based on dataset columns: Cases, Ridership, and Vaccinations
DailyCaseCount = ridershipCase_df["Daily Case Count"]
DailyRidership = ridershipCase_df["Daily Ridership"]

Case_Ridership_Corr = DailyCaseCount.corr(DailyRidership)
Vacc_Ridership_Corr = DailyVaccCount.corr(DailyRidership)
Vacc_Case_Corr = DailyVaccCount.corr(DailyCaseCount)

print("Correlation between Daily Cases and Daily MTA Ridership:" )
print(Case_Ridership_Corr)

print("Correlation between Daily Vaccinations and Daily Ridership:" )
print(Vacc_Ridership_Corr)

print("Vaccination/Case Count Correlation:")
print(Vacc_Case_Corr)

corr_df = pd.DataFrame()
# corr_df["Dates"] = mod_vaccinationRates.iloc[:,0]
corr_df["Ridership"] = mod_mtaRidership.iloc[:,1]
corr_df["Cases"] = mod_dailyCovidCases.iloc[:,1]
corr_df["Vaccinations"] = mod_vaccinationRates.iloc[:,1]

# corr_df = corr_df.fillna(0)
# print(mod_vaccinationRates.iloc[:,1])

# corr_df.to_csv("Correlation.csv", index=False)

#diplay correlations on Heatmap
corrPlot = sns.heatmap(corr_df.corr(), annot = True)
corrPlot.set_title("Correlation Matrix: Ridership, Cases, Vaccinations")
plt.show()

#Run linear regression and plot for each Cases/Ridership and Vaccinations/Ridership
slope,intercept, r_value, p_value, std_err = stats.linregress(corr_df["Cases"],corr_df["Ridership"])
casesRider_corr = sns.regplot(x="Cases", y="Ridership",data=corr_df)
casesRider_corr.set_title("Linear Regression: Cases and Ridership")
plt.show()

slope,intercept, r_value, p_value, std_err = stats.linregress(corr_df["Vaccinations"],corr_df["Ridership"])
vaccRider_corr = sns.regplot(x="Vaccinations", y="Ridership",data=corr_df)
vaccRider_corr.set_title("Linear Regression: Vaccinations and Ridership")
plt.show()
