import requests

def get_jobs(year):
    url = "https://jobs.github.com/positions.json?"
    params = {'title': title}
    r = requests.get(url, params=params)
    jobs = r.json()
    jobs_list = {'jobs':jobs['results']}
    return jobs_list