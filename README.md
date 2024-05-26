## Analyzing COVID-19 Impact on NYC Public Transit
View [website](https://tanveerm176.wixsite.com/data-viz) for a more comprehensive analysis and breakdown of the project.

### Overview
The purpose of this project was to try to determine how the Covid-19 pandemic impacted subway ridership in NYC, and if the vaccination efforts were helping to bring the ridership numbers to pre-pandemic levels. My hypothesis was that the pandemic affected subway ridership in a negative way, however that the vaccination efforts would help bring it to what the MTA would consider normal levels. I gathered vaccination and coronavirus cases data and daily ridership number from the MTA website. I then cleaned the data because the method of data collection varied depending on which agency it was collected from. I then applied linear regression and correlation and plotted those as well. I also created preliminary plots to showcase the data to understand how Vaccinations and Cases played in Daily Ridership from the start of the pandemic. Finally I used the SARIMA model to predict how ridership numbers would change in the next 6 months.

These techniques/methods were accomplished using the following libraries: Matplotlib, SciPy, seaborn, Pandas, and Scikit-Learn.

### Visualizations

Cases and NYC Ridership:
![Cases and NYC Ridership](https://github.com/tanveerm176/Covid-Subway-Analysis/blob/main/images/fig1.png)

Vaccines and NYC Ridership:
![Vaccines and NYC Ridership](https://github.com/tanveerm176/Covid-Subway-Analysis/blob/main/images/fig2.png)

Fitting the SARIMA model to the data:
![SARIMA Model fit](https://github.com/tanveerm176/Covid-Subway-Analysis/blob/main/images/sarima_forecast_21.png)

The final SARIMA model forecasting:
![SARIMA Forecasting](https://github.com/tanveerm176/Covid-Subway-Analysis/blob/main/images/comapare_forecast.png)
