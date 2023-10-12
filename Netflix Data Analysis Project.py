#!/usr/bin/env python
# coding: utf-8

# In[6]:


#Imported necessary packages and dataset used for the analysis
import pandas as pd
import numpy as np
netflix_dataset= pd.read_csv("C:/Users/Captain Joe/Downloads/archive (5)/netflix1.csv")

#Generated a summary of the dataset to be used
summary= netflix_dataset.describe()
print(summary)
netflix_dataset.info()
head_of_netds= netflix_dataset.head(100)
print(head_of_netds)


# In[21]:


#Created a dataframe that consisted of the total amount of entertainment media released over the years
total_number_of_media_per_year= netflix_dataset.groupby('release_year')['type'].value_counts().unstack(fill_value=0)
total_number_of_media_per_year.rename(columns={'type': 'Total Number of Media'}, inplace= True)
total_number_of_media_per_year.rename(columns={'release_year': 'Release Year'}, inplace= True)
total_number_of_media_per_year.reset_index(inplace= True)
print(total_number_of_media_per_year)


# In[12]:


#Created a dataframe that consisted of the total amount of entertainment media according to their ratings
total_number_of_media_per_rating= netflix_dataset.groupby('rating')['type'].value_counts().unstack(fill_value=0)
total_number_of_media_per_rating.rename(columns={'type': 'Total Number of Media'}, inplace= True)
total_number_of_media_per_rating.rename(columns={'rating': 'Rating'}, inplace= True)
total_number_of_media_per_rating.reset_index(inplace= True)
print(total_number_of_media_per_rating)


# In[15]:


#Created a dataframe that consisted of the total amount of entertainment media consumed by each country
total_number_of_media_consumed_per_country= netflix_dataset.groupby('country')['type'].value_counts().unstack(fill_value=0)
total_number_of_media_consumed_per_country.rename(columns={'type': 'Total Number of Media'}, inplace= True)
total_number_of_media_consumed_per_country.rename(columns={'county': 'Country'}, inplace= True)
total_number_of_media_consumed_per_country.reset_index(inplace= True)
print(total_number_of_media_consumed_per_country)


# In[25]:


#Created a dataframe that consisted of the amount of entertainment media according to their categories
total_number_of_media_per_category= netflix_dataset.groupby('listed_in')['type'].value_counts().unstack(fill_value=0)
total_number_of_media_per_category.rename(columns={'type': 'Total Number of Media'}, inplace= True)
total_number_of_media_per_category.rename(columns={'listed_in': 'Category'}, inplace= True)
total_number_of_media_per_category.reset_index(inplace= True)
print(total_number_of_media_per_category)


# In[38]:


#Imported necessary packages for visuaizations
import matplotlib.pyplot as plt
import seaborn as snss

#Generated two scatter plots
plt.scatter(total_number_of_media_per_year['release_year'], total_number_of_media_per_year['Movie'], label='Movie', color='blue', marker='o', s=30)
plt.scatter(total_number_of_media_per_year['release_year'], total_number_of_media_per_year['TV Show'], label='TV Show', color='red', marker='x', s=30)

# Add labels and a title
plt.xlabel('Release Year')
plt.ylabel('Total Media Types')
plt.title('Scatter Plot of Movies and TV Shows Over The Years')
plt.legend()
plt.show()


# In[67]:


#Generated bar charts with different categories
plt.bar(total_number_of_media_per_rating['rating'], total_number_of_media_per_rating['Movie'], label='Movie', color ="blue")
plt.bar(total_number_of_media_per_rating['rating'], total_number_of_media_per_rating['TV Show'], label='TV Show', color="orange")

# Add labels and a title
plt.xlabel('Types of Rating')
plt.ylabel('Total Number of Media')
plt.legend()
plt.xticks(rotation=90)
plt.title('Total Number of Media per Rating Type')


# In[42]:


#Installed necessary packages for map visualizations
get_ipython().system('pip install pygal geopandas')


# In[63]:


#Imported necessary packages
import geopandas as gpd

# Loaded the world map shapefile
world = gpd.read_file('C:/Users/Captain Joe/Downloads/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp')

# Merged your data with the world map using a common column (e.g., 'Country')
merged_data = world.set_index('SOVEREIGNT').join(total_number_of_media_consumed_per_country.set_index('country'))

# Created the map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_title('Netflix World Map for Movies')

# Plot the map with your data (e.g., 'Value' column)
merged_data.plot(column='Movie', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_aspect('auto')

# Show the map
plt.show()


# In[64]:


# Load the world map shapefile
world = gpd.read_file('C:/Users/Captain Joe/Downloads/ne_10m_admin_0_countries/ne_10m_admin_0_countries.shp')

# Merged the data with the world map using a common column
merged_data = world.set_index('SOVEREIGNT').join(total_number_of_media_consumed_per_country.set_index('country'))

# Create the map
fig, ax = plt.subplots(1, 1, figsize=(12, 8))
ax.set_title('Netflix World Map for TV Shows')

# Plot the map with your data (e.g., 'Value' column)
merged_data.plot(column='TV Show', linewidth=0.8, ax=ax, edgecolor='0.8', legend=True)
ax.set_aspect('auto')

# Show the map
plt.show()


# In[ ]:




