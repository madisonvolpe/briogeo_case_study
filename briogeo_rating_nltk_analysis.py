#!/usr/bin/env python
# coding: utf-8

# In[5]:


# import libraries
import pandas as pd
import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.corpus import stopwords


# In[6]:


# create SentimentIntensityAnalyzer 
sia = SentimentIntensityAnalyzer()
# create stopwords object
stop_words = stopwords.words('english')


# In[3]:


# load dataframe
brio = pd.read_csv("./data/briogeo_rating_ulta.csv")


# In[113]:


# create long dataframe of each review tokenized

w_dict = {'Review_ID': [],'Rating_Submit_Dt': [],'Words': []}

for i in range(len(brio.Review)):
    # save review id
    w_dict['Review_ID'].append(brio.Review_ID[i])
    # save review submit date
    w_dict['Rating_Submit_Dt'].append(brio.Rating_Submit_Dt[i])
    # tokenize each review
    review = brio.Review[i]
    review = review.replace("'", "")
    review = review.lower()
    review = nltk.word_tokenize(review)
    review = [w for w in review if not w in stop_words]
    review = [w for w in review if w.isalpha()]
    w_dict['Words'].append(review)    


# In[116]:


# convert dictionary to dataframe
w_df = pd.DataFrame(w_dict)
# create a long dataframe - each review id is repreated for each word in review
w_df_final = w_df.explode('Words')
# save dataframe 
w_df_final.to_csv("./data/briogeo_ulta_rating_wordlist.csv")


# In[48]:


# create bigrams of the reviews

bigrams_dict = {'Review_ID': [],'Rating_Submit_Dt': [],'Bigrams': []}

for i in range(len(brio.Review)):
    # save review id
    bigrams_dict['Review_ID'].append(brio.Review_ID[i])
    # save review submit date
    bigrams_dict['Rating_Submit_Dt'].append(brio.Rating_Submit_Dt[i])
    # tokenize each review
    review = brio.Review[i]
    review = review.replace("'", "")
    review = review.lower()
    review = nltk.word_tokenize(review)
    review = [w for w in review if not w in stop_words]
    review = [w for w in review if w.isalpha()]
    bigrams = nltk.bigrams(review)
    bigrams = [' '.join(tup) for tup in bigrams]
    bigrams_dict['Bigrams'].append(bigrams)  


# In[51]:


# convert dictionary to dataframe
bigrams_df = pd.DataFrame(bigrams_dict)
# create a long dataframe - each review id is repreated for each word in review
bigrams_df_final = bigrams_df.explode('Bigrams')
# save dataframe 
bigrams_df_final.to_csv("./data/briogeo_ulta_rating_bigrams.csv")


# In[124]:


# run VADER sentiment analysis and save pos, negative, neutral, compound scores to dataframe for each review
brio["Positive"] = [sia.polarity_scores(i)["pos"] for i in brio["Review"]]
brio["Negative"] = [sia.polarity_scores(i)["neg"] for i in brio["Review"]]
brio["Neutral"] = [sia.polarity_scores(i)["neu"] for i in brio["Review"]]
brio["Compound"] = [sia.polarity_scores(i)['compound'] for i in brio["Review"]]


# In[126]:


# save dataframe with scores 
brio.to_csv("./data/briogeo_ulta_rating_sentiment_scores.csv")

