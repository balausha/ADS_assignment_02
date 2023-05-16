# -*- coding: utf-8 -*-
"""
Created on Mon Mar 20 18:28:52 2023

@author: Lenovo
"""
#required libraries
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from scipy import stats
#import stats


def loadexcel(file):
    '''This is used to  read csv file and it accept file name as a parameter'''
    sd = pd.read_excel(file, header=3)
    return sd

sd = loadexcel("API_19_DS2_en_excel_v2_5360124.xlsx")

sd=sd.drop(['Country Code', 'Indicator Code'], axis=1)

def cleaningData(df):
    df.set_index(['Country Name', 'Indicator Name'], inplace=True)
    df=df.T
    df=df.fillna(0) 
    return df
sd1=cleaningData(sd)

Spain = sd1.loc[:, 'Spain']
India = sd1.loc[:, 'India']
China = sd1.loc[:, 'China']
Pakistan = sd1.loc[:, 'Pakistan']
Mali = sd1.loc[:, 'Mali']
Peru = sd1.loc[:, 'Peru']
Canada = sd1.loc[:, 'Canada']
United_States = sd1.loc[:, 'United States']
Sri_Lanka = sd1.loc[:, 'Sri Lanka']

Spain = Spain.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
India = India.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
China = China.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Pakistan = Pakistan.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Mali = Mali.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Peru = Peru.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Canada = Canada.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
United_States = United_States.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)','Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]
Sri_Lanka = Sri_Lanka.loc[('1980', '1985', '1990', '1995', '2000', '2005', '2010'), ('Renewable energy consumption (% of total final energy consumption)', 'Other greenhouse gas emissions (% change from 1990)', 'Arable land (% of land area)', 'Forest area (% of land area)', 'Population growth (annual %)', 'Urban population growth (annual %)','Agricultural land (% of land area)','Cereal yield (kg per hectare)','CO2 emissions (kt)')]

plt.plot(Spain.index, Spain.loc[:, 'Arable land (% of land area)'], label='Spain')
plt.plot(India.index, India.loc[:, 'Arable land (% of land area)'], label='India')
plt.plot(China.index, China.loc[:, 'Arable land (% of land area)'], label='China')
plt.plot(Pakistan.index, Pakistan.loc[:, 'Arable land (% of land area)'], label='Pakistan')
plt.plot(Mali.index, Mali.loc[:, 'Arable land (% of land area)'], label='Mali')
plt.plot(Peru.index, Peru.loc[:, 'Arable land (% of land area)'], label='Peru')
plt.plot(Canada.index, Canada.loc[:, 'Arable land (% of land area)'], label='Canada')
plt.plot(United_States.index, United_States.loc[:, 'Arable land (% of land area)'], label='United States')
plt.plot(Sri_Lanka.index, Sri_Lanka.loc[:, 'Arable land (% of land area)'], label='Sri Lanka')
plt.xlabel('Years')
plt.ylabel('Land Percentage')
plt.title('Arable Land')
plt.ylim(0, 70, 10)
plt.legend(bbox_to_anchor=(1.0, 1.05))
plt.show()


plt.plot(Spain.index, Spain.loc[:, 'Forest area (% of land area)'], label='Spain')
plt.plot(India.index, India.loc[:, 'Forest area (% of land area)'], label='India')
plt.plot(China.index, China.loc[:, 'Forest area (% of land area)'], label='China')
plt.plot(Pakistan.index, Pakistan.loc[:, 'Forest area (% of land area)'], label='Pakistan')
plt.plot(Mali.index, Mali.loc[:, 'Forest area (% of land area)'], label='Mali')
plt.plot(Peru.index, Peru.loc[:, 'Forest area (% of land area)'], label='Peru')
plt.plot(Canada.index, Canada.loc[:, 'Forest area (% of land area)'], label='Canada')
plt.plot(United_States.index, United_States.loc[:, 'Forest area (% of land area)'], label='United States')
plt.plot(Sri_Lanka.index, Sri_Lanka.loc[:, 'Forest area (% of land area)'], label='Sri Lanka')
plt.xlabel('Years')
plt.ylabel('Land Percentage')
plt.title('Forest Land')
plt.xlim(1, 6, 1)
plt.ylim(0, 65, 10)
plt.legend(bbox_to_anchor=(1.0, 1.05))
plt.show()

sns.heatmap(India.corr(), cmap='Reds', center=0, annot=True, linewidths=0.05)
plt.title("India")
plt.show()

sns.heatmap(China.corr(), cmap=sns.cubehelix_palette(as_cmap=True), center=0, annot=True, linewidths=0.05)
plt.title("China")
plt.show()

sns.heatmap(Canada.corr(), cmap='crest', center=0, annot=True, linewidths=0.05)
plt.title("Canada")
plt.show()

spain = stats.skew(Spain)

ind = stats.skew(India)

