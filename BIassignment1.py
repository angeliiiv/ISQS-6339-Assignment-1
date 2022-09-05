# -*- coding: utf-8 -*-
"""
Created on Sun Sep  4 16:36:32 2022

@author: eddie
"""

#Task 1

#request library
import requests as r

#request a page
res=r.get('http://drd.ba.ttu.edu/isqs6339/assign/assign_1/')


print('Values for Task #1')
print('Status Code of Call: ', res.status_code)
print('Page is Redirecting: ', res.is_redirect)
print('Current Page Encoding: ', res.encoding)
print('Returned Header for Page: ', res.headers)


#Task 2

#request library
import requests as r
from bs4 import BeautifulSoup

#request a page
res=r.get('http://drd.ba.ttu.edu/isqs6339/assign/assign_1/')
soup=BeautifulSoup(res.content, 'lxml')
print('***Task #2***')
print('The following are values for the IPhone 11 pro: ')
results=soup.find_all('li')[6]
for l in results:
    print(l.text)
results=soup.find_all('li')[5]
for l in results:
    print(l.text)