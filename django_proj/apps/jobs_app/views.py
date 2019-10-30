
from django.shortcuts import render, HttpResponse, redirect
from django.contrib import messages
from .models import *
import requests

def index(request):
    return render(request,'jobs_app/index.html')

def process(request):
    if request.method =='POST':
        if request.POST['language']=='python':
            request.session['language']= request.POST['language']
        if request.POST['language']=='javascript':
            request.session['language']= request.POST['language']    
        if request.POST['language']=='java':
            request.session['language']= request.POST['language']  
        if request.POST['language']=='php':
            request.session['language']= request.POST['language']  
    return redirect('/python')

def python(request):
    Job.objects.all().delete()
    show_cities = ['Seattle, WA', 'Chicago, IL', 'Phoenix, AZ', 'New York, NY', 'San Francisco, CA', 'Los Angeles, CA', 'Miami, FL', 'Minneapolis, MN', 'Dallas, TX', 'Washington, DC', 'Kansas City, MO']
    for city in show_cities:
        cityName = city.split(",")[0]
        state = city.split(",")[1]
        searchLoc = cityName.replace(" ", "+") + state
        language = request.session['language']
        host = 'https://jobs.github.com/positions.json?'
        desc = 'description=' + language
        loc = '&location=' + searchLoc
        url = host + desc + loc
        req = requests.get(url)
        jsonResp = req.json()
        for posting in jsonResp:
            obj, created = Job.objects.update_or_create(jtitle = posting['title'],jcompany = posting['company'],location =cityName, jtype = posting['type'],jpost_url = posting['url'],jcompany_url = posting['company_url'])
    show_job = Job.objects.all()
    actLocations = list(Job.objects.values_list('location').distinct())
    actLocations= [i[0] for i in actLocations]

    context = {
        "html_show_job": show_job,
        "html_locations": actLocations
    }
    return render(request, 'jobs_app/api_test.html', context)


