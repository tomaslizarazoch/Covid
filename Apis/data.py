import pandas as pd
import json
import requests
import numpy as np



url = 'https://covid.ourworldindata.org/data/owid-covid-data.csv'
def covid(url):
    
    data = pd.read_csv(url)
    data = data.drop(['iso_code', 'continent','total_cases','total_deaths', 'new_deaths', 'total_cases_per_million',
       'new_cases_per_million', 'total_deaths_per_million',
       'new_deaths_per_million', 'new_tests', 'total_tests',
       'total_tests_per_thousand', 'new_tests_per_thousand',
       'new_tests_smoothed', 'new_tests_smoothed_per_thousand', 'tests_units',
       'stringency_index', 'population', 'population_density', 'median_age',
       'aged_65_older', 'aged_70_older', 'gdp_per_capita', 'extreme_poverty',
       'cardiovasc_death_rate', 'diabetes_prevalence', 'female_smokers',
       'male_smokers', 'handwashing_facilities', 'hospital_beds_per_thousand',
       'life_expectancy'], axis= 1)
    data = data[data['location'].isin(['Argentina','Chile','Colombia','Russia','Spain'])]
    data.dropna(subset =['new_cases'], axis = 0, inplace = True)
    data.rename(columns={'new_cases':'c_average'},inplace = True)
    json1 = data.groupby('date').mean()
    


    return json1

    