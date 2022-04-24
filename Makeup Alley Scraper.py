
# coding: utf-8

# In[41]:


# import libraries
from bs4 import BeautifulSoup
import pandas as pd
import re
import html5lib
from urllib import request
import os


# In[32]:


# create list of urls
urls = ["https://www.makeupalley.com/product/showreview.asp/ItemId=174309/Briogeo-Dont-Despair,-Repair!--Deep-Conditioning-Mask/Briogeo/Hair-Treatments?page=1#reviews",
        "https://www.makeupalley.com/product/showreview.asp/ItemId=174309/Briogeo-Dont-Despair,-Repair!--Deep-Conditioning-Mask/Briogeo/Hair-Treatments?page=2#reviews",
        "https://www.makeupalley.com/product/showreview.asp/ItemId=174309/Briogeo-Dont-Despair,-Repair!--Deep-Conditioning-Mask/Briogeo/Hair-Treatments?page=3#reviews",
        "https://www.makeupalley.com/product/showreview.asp/ItemId=174309/Briogeo-Dont-Despair,-Repair!--Deep-Conditioning-Mask/Briogeo/Hair-Treatments?page=4#reviews",
        "https://www.makeupalley.com/product/showreview.asp/ItemId=174309/Briogeo-Dont-Despair,-Repair!--Deep-Conditioning-Mask/Briogeo/Hair-Treatments?page=5#reviews"
       ]


# In[33]:


# create function to scrape Makeup Alley Website
def MakeupAlleyScrape(url):
    
    page = request.urlopen(url)
    soup = BeautifulSoup(page, 'lxml')
    
    # pull rating from website
    ratings_raw = soup.findAll('span', {'class': 'rating-value'}, limit = 10)
    ratings_raw = [str(i) for i in ratings_raw]
    ratings = [re.search('\d{1}\.\d{1}', i).group(0) for i in ratings_raw]
    
    # pull date of rating from website
    rate_yr = soup.findAll('div', {'class': 'date'}, limit =10)
    rate_yr = [i.p.text for i in rate_yr]
    
    # create dataframe 
    brio_dat = {'Rating': ratings, 'Rating Date': rate_yr}
    brio_df = pd.DataFrame(brio_dat)
    
    return brio_df


# In[37]:


# Loop through list of urls and apply MakeupAlleyScrape function
brio_rating_df = [MakeupAlleyScrape(url) for url in urls]


# In[38]:


# Convert list of dataframes to one dataframe
brio_rating_df = pd.concat(brio_rating_df)


# In[39]:


# Reset row index in list of dataframes
brio_rating_df = brio_rating_df.reset_index(drop = True)


# In[46]:


# Write dataframe to csv
path = os.getcwd() + '/data/briogeo_rating_makeupalley.csv'
brio_rating_df.to_csv(path)

