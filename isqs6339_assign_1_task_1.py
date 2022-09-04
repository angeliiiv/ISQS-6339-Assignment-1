# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 18:37:44 2022

@author: CRiley
"""

#Request Library
import requests as r


url = 'http://drd.ba.ttu.edu/isqs6339/assign/assign_1/'

res = r.get(url)

print('Values for Task #1')

#Check HTML Status Code
print('Status Code of Call:  ',res.status_code)

#Check for page redirecting
print('Page is Redirecting:  ',res.is_redirect)

#Return current page encoding
print('Current Page Encoding:  ',res.encoding)

#Returns server response headers
print('Returned Header for Page:  ',res.headers)