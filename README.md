# Case Study of Briogeo's "Don't Despair, Repair!" Deep Conditioning Mask

## Motivation & Analysis Summary

I frequently use Briogeo's "Don't Despair, Repair!" deep conditioning mask in my own hair. I have loved the results, but I have heard and read online that the formula for the mask changed. As a result, some customers are not as happy with the mask as they once were. As a "Hair Care Guru" in my spare time and Data Analyst for my day job, I decided to look at the reviews for this product and see if the ratings for this product have changed overtime. 

For the analysis, I webscraped reviews for this product from Ulta's website. I conducted exploratory analysis and analyzed the product ratings overtime. Likewise, I also analyzed the sentiment of the written reviews overtime. 

In sum, I found the following: the average rating on Ulta.com for this mask has decreased since 2020. Likewise, the positive sentiment of the reviews for this product have decreased since 2020.

## Data Sources 
- Reviews from Ulta (Webscraped reviews from Ulta's website, n = 2958 reviews, spanning from November 2014 to May 2022)
  - data/**_briogeo_rating_ulta.csv_** - N = 2958 reviews. Each review is one row. The following attributes are included: Unique ID for Review (Review_ID), Rating [1-5] for the Review (Rating), Location of customer that submitted the review (Location), Submission date of review (Rating_Submit_Dt), Username of customer that submitted the review (Username), Full text of Review (Review).
  
  - data/**_briogeo_ulta_rating_sentiment_scores.csv_** - Same attributes and number of rows as the **_briogeo_rating_ulta.csv_** dataset, but this dataset also includes the addition of the VADER sentiment analysis. The additional attributes are the Postive Score, Negative Score, Neutral Score, and Compound Score.
  
  - data/**_briogeo_ulta_rating_wordlist.csv_** - Long dataset with each Review_ID repeated for the words within each review. Stop words are excluded. 
  
  - data/**_briogeo_ulta_rating_bigrams.csv_** - Long dataset with each Review_ID repeated for the bigrams within each review. Stop words are excluded. 
  
  - data/**_briogeo_ulta_rating_trigrams.csv_** - Long dataset with each Review_ID repeeated for the trigrams within each review. Stop words are excluded.

## Analysis
- **_Ulta Scraper.py_** - Web scraping script 
- **_briogeo_rating_nltk_analysis.py_** - VADER sentiment analysis and create wordlists (bigrams & trigrams) for further analysis in Tableau
- **!TABLEAU WORKBOOK HERE!**

## Final Product & Conclusions
Link to Tableau Public workbook

#### Extra
In addition to Ulta reviews, I also webscraped reviews for this product from Makeup Alley. However, I did not end up using them in my analysis. The dataset and code for the Makup Alley reviews are in this repository as: data/**_briogeo_rating_makeupalley.csv_** & **_Makeup Alley Scraper.py_**.
