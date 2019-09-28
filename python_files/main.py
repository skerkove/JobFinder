# -*- coding: utf-8 -*-
"""
Created on Sat Sep 28 15:21:07 2019

@author: d
"""

from jobsByCity import cityJobs
from cityList import locList

language = 'python'
cityDict = {}

cityList = locList(cities)
#print(cityList)

for city in cityList:
    totalJobs = cityJobs(city, language)
    cityDict[city]= totalJobs

print(cityDict)
