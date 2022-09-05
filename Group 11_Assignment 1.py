# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 13:28:39 2022

@author: DStrawma
"""
#Request Library
import requests as r
from bs4 import BeautifulSoup
import csv
import time as t
import random as rnd
import pandas as pd

#scrape variables
url = 'http://drd.ba.ttu.edu/isqs6339/assign/assign_1/'
fp = 'C:\\Users\\dstrawma\\Downloads\\'
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
                          Task 1: Print Web Server and Web Call Info
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

print('Values for Task #1')

#Check HTML Status Code
print('Status Code of Call:  ',res1.status_code)

#Check for page redirecting
print('Page is Redirecting:  ',res1.is_redirect)

#Return current page encoding
print('Current Page Encoding:  ',res1.encoding)

#Returns server response headers
print('Returned Header for Page:  ',res1.headers)


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
                          Task 2: Print iPhone Details
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""

#using find to single out the area of code that has the details for the three phones
phone_details = soup.find('div', attrs={'id' : 'phonelist'}).find_all('li')  

#indexing to get required iPhone details
iphone_os = phone_details[6].text
iphone_color = phone_details[5].text
print('***Task #2')
print('The following are values for the iPhone 11 Pro')
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



"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""         
                 Task 4: Export data to csv
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
###****This is a Work in Progress

url = 'http://drd.ba.ttu.edu/isqs6339/assign/assign_1/'
filepath = 'C:\\Users\Dstrawma\Downloads' 
filename = 'assignemnt_1_group_11.csv'
lowval = 5
highval = 7

#aseembling the list of url we will need for the entire assignent.
res1 = r.get(url)
soup1 = BeautifulSoup(res1.content, 'lxml')

pager1 = soup1.find('div', attrs={'id' : 'phonelist'}).find_all('a')
#for p in pager1:
    #print(p['href'])

#Create URL list
urllist1 = [url]

#append URL list
for p in pager1:
    urllist1.append(url + p['href'])
    #print(p['href'])

for page in urllist1:
    res1 = r.get(page)
    soup1 = BeautifulSoup(res1.content, 'lxml')
    
    phonelist = soup1.find_all('li', attrs={'class' : 'root'})
    #print(phonelist)
    

    
    for span in phonelist:
        phonenames = span.find_all('span')
        if len(phonenames) == 1:
            print('product_name', phonenames[0].text)
    for li in phonelist:
        phoneinfo = li.find_all('li')
        if len(phoneinfo)==3:
            print('color', phoneinfo[0].text.split('Color: ')[1])
            print('os', phoneinfo[1].text.split('OS: ')[1])  
            childhref1 = url + phoneinfo[2].find('a')['href']
            
            childres1 = r.get(childhref1)
            childsoup1 = BeautifulSoup(childres1.content, 'lxml')
            
            phonetr = childsoup1.find('div', attrs={'id' : 'Phoneinitial'}).find('table').find_all('tr')
            print(phonetr)


            for phonedetails in phonetr:
                phonetds = phonedetails.find_all('td')
                print(phonetds)
    ###still need to split out the additional details from the chlid page.
    break






