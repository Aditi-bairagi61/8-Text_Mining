# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


from bs4 import BeautifulSoup
import requests
link='https://m.imdb.com/title/tt0068646/reviews?ref_=tt_urv'
page=requests.get(link)
page
page.content
soup=BeautifulSoup(page.content,'html.parser')
print(soup.prettify())

#################################################################################

title=soup.find_all('a',class_="title")
title
review_title=[]
for i in range(0,len(title)):
    review_title.append(title[i].get_text())
review_title
review_title[:]=[title.strip('\n') for title in review_title]
review_title
len(review_title)

################################################################

rating=soup.find_all('div',class_='inline-rating')

rating
rate=[]
for i in range(0,len(rating)):
    rate.append(rating[i].get_text())
rate[:]=[r.strip('/') for r in rate]
rate
len(rate)
rate.append('')
rate.append('')
len(rate)
print(soup.prettify())  # This will print the HTML content in a readable format

##########################################

#lets scrap the review body
review = soup.find_all('div', class_='text')

review_body = []
for i in range(0, len(review)):
    review_body.append(review[i].get_text())

review_body
len(review_body)


#################################################################################

import pandas as pd
df=pd.DataFrame()
df['review_title']=review_title
df['rate']=rate
df['review']=review_body
df

df.to_csv('C:/8-text_Mining/GodFather_reviews.csv')

###################################################################################
#sentiment analysis
import pandas as pd
from textblob import TextBlob
import textblob
textblob.download_corpora()


sent = "this is very excellent garden"
pol = TextBlob(sent).sentiment.polarity
pol

df=pd.read_csv('C:/8-text_Mining/GodFather_reviews.csv')
df.head()
df['polarity']=df['Review'].apply(lambda x:TextBlob(str(x)).sentiment.polarity)
df['polarity']











