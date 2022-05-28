
# coding: utf-8

# In[1]:


# import libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import re
import pandas as pd
import requests
import html5lib
import sys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.firefox.firefox_binary import FirefoxBinary
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time
import numpy as np
import os


# In[2]:


url = "https://www.ulta.com/p/dont-despair-repair-deep-conditioning-hair-mask-pimprod2021375"
driver = webdriver.Firefox() 
driver.get(url)


# In[3]:


ulta_bsObjs = []

for i in range(306):
    try: 
        # scroll to bottom of page
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # collect html 
        html = driver.page_source
        # "BeautifulSoup" the html and append to ulta_bsObjs list
        ulta_bsObjs.append(BeautifulSoup(html, "html.parser"))
        # Wait...
        time.sleep(3)
        # Click next button
        next_btn = driver.find_element_by_xpath('//a[@class="pr-rd-pagination-btn" and contains(text(),"Next")]')
        next_btn.click()
    except NoSuchElementException:
        pass


# In[66]:


def create_ulta_ds(bsObj):
    
    # ratings
    ratings_raw = bsObj.findAll('div', {'class': 'pr-snippet-rating-decimal'})
    ratings_raw = ratings_raw[3:13]
    ratings = [rating.text for rating in ratings_raw]
    
    # locations
    locs_raw = bsObj.findAll('p', {'class': 'pr-rd-details pr-rd-author-location'})
    locs = [loc.text for loc in locs_raw]
    locs = [loc.replace('From\xa0', "") for loc in locs]
    
    # submit_dts
    submit_dts = bsObj.time.attrs['datetime']
    
    # user name
    usernames_raw = bsObj.findAll('p', {'class': 'pr-rd-details pr-rd-author-nickname'})
    usernames = [username.text for username in usernames_raw]
    usernames = [username.replace('By', "") for username in usernames]
    
    # review paragraph 
    review_pars = bsObj.findAll('p', {'class': 'pr-rd-description-text'})
    reviews = [review.text for review in review_pars]

    # create dataframe 
    brio_dat = {'Rating': ratings, 'Location': locs, 'Rating_Submit_Dt': submit_dts, 'Username': usernames, 'Review': reviews}
    brio_ulta_df = pd.DataFrame(brio_dat)
    
    return brio_ulta_df


# In[67]:


# Loop through list of urls and apply create_ulta_ds function
brio_ulta_rating_df = [create_ulta_ds(ulta_bsObj) for ulta_bsObj in ulta_bsObjs]


# In[68]:


# Convert list of dataframes to one dataframe
brio_ulta_rating_df = pd.concat(brio_ulta_rating_df)
brio_ulta_rating_df = brio_ulta_rating_df.reset_index(drop = True)


# In[69]:


# drop duplicates
brio_ulta_rating_df = brio_ulta_rating_df.drop_duplicates()


# In[71]:


# Write dataframe to csv
path = os.getcwd() + '/data/briogeo_rating_ulta.csv'
brio_ulta_rating_df.to_csv(path)

