# -*- coding: utf-8 -*-
"""
Created on Fri Sep  2 13:22:46 2022

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
    

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
                          Task 2: Print iPhone Details
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

res1 = r.get(url)
soup = BeautifulSoup(res1.content, 'lxml')

#using find to single out the area of code that has the details for the three phones
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

#from what I can see we can hardcode this task
iphone_url = 'http://drd.ba.ttu.edu/isqs6339/assign/assign_1/phone.php?id=1341'
res3 = r.get(iphone_url)
soup3 = BeautifulSoup(res3.content, 'lxml') 

#getting storage 
iphone_storage_code = soup3.find('div',attrs={'id':'Phoneinitial'}).find_all('td')
iphone_storage = iphone_storage_code[2].text.rstrip() +' '+ iphone_storage_code[3].text.rstrip()

#getting front camera features
front_camera_code = soup3.find('div',attrs={'id':'Phoneotherstuff'}).find_all('span',attrs={'class':'tag'})
front_camera_features = soup3.find('div',attrs={'id':'Phoneotherstuff'}).find('ul').find_all('li')
#printing
print('***Task #3***')
print(iphone_storage)
print('Front Camera Features: ')
for li in front_camera_features:
    print(li.text)




























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
            
    


