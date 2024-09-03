# -*- coding: utf-8 -*-
"""
Created on Fri Aug 30 08:56:56 2024

@author: Lenovo
"""
#--------------- sample_doc.html ---------------------
from bs4 import BeautifulSoup
soup = BeautifulSoup(open("sample_doc.html"),'html.parser')
print(soup)
#It's going to show all the html content. 
soup.text
#It will show only text
soup.contents
#It's going to show all the html content extracted
soup.find('address')
soup.find_all('address')
soup.find_all('q')
soup.find_all('b')
table = soup.find('table')
table

for row in table.find_all("tr"):
    columns=row.find_all('td')
    print(columns)
#It will show all the rows except first row 
#Now we want to display M.Tech which is located in third row
#I needto give [3][2]
    table.find_all('tr')[3].find_all('td')[2]
    
#--------------- SanjivaniCOE.org -------------------------

from bs4 import BeautifulSoup as bs
import requests
link = "https://sanjivanicoe.org.in/index.php/contact"
page= requests.get(link)
page
#If you get Response[200] then page is succefully found .
page.content
#You will get all html sourse code but very crowdy text
#Let us apply html parser
soup = bs(page.content,'html.parser')
soup
print(soup.prettify())
# The Text is display in clean and neat format
list(soup.children)
#Finding all contents using tab
soup.find_all('p')
#Suppose you want to extract contents from first row

#-------------- Amazon.com -----------------------------

from bs4 import BeautifulSoup as bs
import requests
link = "https://www.amazon.in/Vendoz-Women-Stylish-Casual-Sneakers/dp/B0B5VFLR68/ref=asc_df_B0B5VFLR68/?tag=googleshopdes-21&linkCode=df0&hvadid=610186779037&hvpos=&hvnetw=g&hvrand=16512439340853383867&hvpone=&hvptwo=&hvqmt=&hvdev=c&hvdvcmdl=&hvlocint=&hvlocphy=1007780&hvtargid=pla-1696229204540&psc=1&mcid=7223dd89be8b3025a76a510c23bc993d"
page= requests.get(link)
page
#You get Response [503] means page is successfully added
page
#If you get Response[200] then page is succefully found .
page.content
#You will get all html sourse code but very crowdy text
#Let us apply html parser
soup = bs(page.content,'html.parser')
soup
print(soup.prettify())
# The Text is display in clean and neat format
list(soup.children)
#Finding all contents using tab
title = soup.find_all('div',class_="a-section a-spacing-none review-views celwidget.span")
title
