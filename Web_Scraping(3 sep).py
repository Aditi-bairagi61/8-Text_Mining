# -*- coding: utf-8 -*-
"""
Created on Tue Sep  3 08:34:36 2024

@author: HP
"""

#web scraping 
#3 sep 2024
from bs4 import BeautifulSoup as bs
import requests
 link='https://www.imdb.com/title/tt0068646/reviews?ref_=tt_urv'
page=requests.get(link)
page
page.content
Soup=bs(page.content,'html.parser')
print(Soup.prettify())