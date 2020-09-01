# -*- coding: utf-8 -*-
"""
Created on Sat Aug 29 13:03:37 2020

@author: Jeff Nania
"""


"""
BFOR 516 Lab 1: Data Exploration

In this lab we will explore the COVID-19 data from the NY Capital Region

"""

#%%

#Python Imports

import pandas as pd
import datetime

#%%

#Import/Clean data

county = pd.read_csv('https://raw.githubusercontent.com/nytimes/covid-19-data/master/us-counties.csv')

#%%

#Setting variables

today = datetime.date.today()
print(today)
output = 'output/capital_comparison_' + str(today) + '.jpg'
date_title = 'COVID-19 Cases In The Capital Region (' + str(today) + ')'

#%%

#Convert dates

county['date'] = pd.to_datetime(county['date'])                                                     

#%%

#Column summaries

print(county.describe(include='all'))

#%%

#This week's lab

#Set the names of the County

cr = ['Albany', 'Columbia', 'Fulton', 'Greene', 'Montgomery', 'Rensselaer', 'Saratoga', 'Schenectady', 'Scoharie', 'Warren', 'Washington']

#Select only the data from NY where the county names are in the list above

alb = county[(county['state'] == 'New York') & (county['county'].isin(cr) & (county['cases']) > 0)]

#Create a plot of cases by county

county_plot = alb.groupby(['date', 'county'])['cases'].sum().unstack().plot(logy=False, figsize=(10,5))
county_plot.set(xlabel='Date', ylabel='Number of Cases', title=date_title)
county_plot.get_figure()

#Save the figure

county_plot.get_figure().savefig(output, bbox_inches='tight', dpi=300)

#%%

#For Submission via Slack

#Plot the total number of deaths.
total_deaths = alb.groupby(['date'])['deaths'].sum()
print (total_deaths)

#total_deaths_plot = 

#Create a plot showing the total number of cases in the Capital Region.

total_cases_plot = alb.groupby(['date'])['cases'].sum().plot()
print(total_cases)

total_cases_plot['date'].plot.line(logy=True, legend=True)
total_cases_plot['cases'].plot.line(logy=True, legend=True)
total_cases_plot.get_figure()
total_cases_plot.get_figure().savefig(output, bbox_inches='tight', dpi=300)
