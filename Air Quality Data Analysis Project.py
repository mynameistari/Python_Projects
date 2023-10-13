#!/usr/bin/env python
# coding: utf-8

# In[2]:


#Imported the necessary packages for analysis
import pandas as pd
import numpy as np

#Loaded the dataset
air_dataset= pd.read_csv('C:/Users/Captain Joe/Downloads/archive (6)/c4_epa_air_quality.csv')
print(air_dataset)


# In[4]:


summary= air_dataset.describe()
print(summary)


# In[7]:


air_dataset.head(20)


# In[8]:


air_dataset.tail(20)


# In[18]:


#Created a dtaframe that contained the average number of co emissions per state
average_number_of_co_emissions_per_state= air_dataset.groupby('state_name')['arithmetic_mean'].mean().reset_index()

average_number_of_co_emissions_per_state.rename(columns={'state_name': 'State Name'}, inplace= True)
average_number_of_co_emissions_per_state.rename(columns={'arithmetic_mean': 'Average'}, inplace= True)

average_number_of_co_emissions_per_state.reset_index(inplace= True)
average_number_of_co_emissions_per_state.head(52)


# In[33]:


#Created a dtaframe that contained the average number of co emissions per county
average_number_of_co_emissions_per_county= air_dataset.groupby('county_name')['arithmetic_mean'].mean().reset_index()

average_number_of_co_emissions_per_county.rename(columns={'county_name': 'County Name'}, inplace= True)
average_number_of_co_emissions_per_county.rename(columns={'arithmetic_mean': 'Average'}, inplace= True)

average_number_of_co_emissions_per_county.reset_index(inplace= True)
average_number_of_co_emissions_per_county.head(101)


# In[6]:


total_aqi_per_state= air_dataset.groupby('state_name')['aqi'].sum().reset_index()

total_aqi_per_state.rename(columns={'state_name': 'State Name'}, inplace= True)
total_aqi_per_state.rename(columns={'aqi': 'AQI'}, inplace= True)

total_aqi_per_state.reset_index(inplace= True)
total_aqi_per_state.head(52)


# In[10]:


#Imported necessary packages for visualization
import matplotlib.pyplot as plt
import seaborn as sns

#Generated bar charts with different categories
plt.bar(total_aqi_per_state['State Name'], total_aqi_per_state['AQI'], color ="maroon")

# Add labels and a title
plt.xlabel('State Names')
plt.ylabel('AQI (Air Quality Index )')
plt.xticks(fontsize=6, rotation=90)
plt.title('AQI values per State in 2017')


# In[41]:


#Generated bar charts with different categories
plt.bar(average_number_of_co_emissions_per_state['State Name'], average_number_of_co_emissions_per_state['Average'], color ="maroon")

# Add labels and a title
plt.xlabel('State Names')
plt.ylabel('Average')
plt.xticks(fontsize=6, rotation=90)
plt.title('Average CO Emissions per State in 2017')


# In[11]:


#Created a visualization that one can interact with
#Imported the necessary packages 
import ipywidgets as widgets
from ipywidgets import interact

# Create a function to update the bar chart
def update_bar_chart(selected_state):
    filtered_df = air_dataset[air_dataset['state_name'] == selected_state]
    county_avg = filtered_df.groupby('county_name')['arithmetic_mean'].mean()

    # Create the bar chart
    plt.figure(figsize=(10, 6))
    plt.bar(county_avg.index, county_avg, color='maroon')
    plt.xlabel('County')
    plt.ylabel('Average')
    plt.xticks(rotation=90)
    plt.title(f'Average CO Emissions in {selected_state} in 2017')
    plt.show()

# Get unique states for the dropdown options
state_options = air_dataset['state_name'].unique()

# Create the interactive dropdown widget
@interact(state_name=widgets.Dropdown(options=state_options, description='Select State:'))
def update_chart(state_name):
    update_bar_chart(state_name)


# In[ ]:




