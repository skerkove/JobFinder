    
import requests
import json


def cityJobs(city, language):
    host = 'https://jobs.github.com/positions.json?'
    desc = 'description=' + language
    loc = '&location=' + city
    url = host + desc + loc
    req = requests.get(url)
    jsonResp = req.json()
    #print(type(jsonResp))
    count = 0
    for elem in jsonResp:
        #print(elem['location'])
        count+=1
    return count


