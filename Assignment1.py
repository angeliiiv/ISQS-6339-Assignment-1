# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:22:46 2022

@author: angel
"""

# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 10:18:27 2022

@author: angel
"""
#imports
import requests as r
from bs4 import BeautifulSoup
import csv
import time as t
import random as rnd
import pandas as pd

#scrape variables
url = 'http://drd.ba.ttu.edu/isqs6339/assign/assign_1/'
fp = 'C:\\Users\\angel\\Downloads\\'
filename = 'assignemnt_1.csv'
lowval = 5
highval = 7

#aseembling the list of url we will need for the entire assignent. 
res1 = r.get(url)
soup = BeautifulSoup(res1.content, 'lxml')

#singles out the href links that leads to further details for the three phones
pager = soup.find('div', attrs={'id' : 'phonelist'}).find_all('a')

#creating a list with the original list and then use a for loop to append the additional urls from pager
urllist = [url]
for p in pager:
    urllist.append(url + p['href']) 
    



m   
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
                          Task 2: Print iPhone Details
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

res1 = r.get(url)
soup = BeautifulSoup(res1.content, 'lxml')
#I was able to use the div for phone list to get to the phone details. 
phone_details = soup.find('div', attrs={'id' : 'phonelist'}).find_all('li')  

#indexing to get required iPhone details
iphone_os = phone_details[6].text
iphone_color = phone_details[5].text
print('***Task #2')
print('The following are values for the Iphone 11 Pro')
print(iphone_os)
print(iphone_color)



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
                 Task 3: Extract storage & camera features
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""





# urllist = [url]
# for p in pager: 
#     urllist.append(url + p['href']) 
    
# for url in urllist:
#     res = r.get(url)
#     soup = BeautifulSoup(res.content, 'lxml')

#     userlist = soup.find('div', attrs = {'id':'UsrIndex'}).find_all('tr')
#     for tr in userlist:
#         usertds = tr.find_all('td')
#         if len(usertds) ==7:
#             #print user info
#             print('Rank:',usertds[1].text)
#             print('ID: ',usertds[0].find('a')['href'].split('id=')[1].split('&page')[0])
            
#             break
            
    


    