import requests
from bs4 import BeautifulSoup  # Helps to drill down into HTML

url = "https://realpython.github.io/fake-jobs"
response = requests.get(url)
soup = BeautifulSoup(response.content)
print(soup)  #html page content (very long)  is the same as going to the dev tools and look for page source

# Find elements by id:
result = soup.find(id="search in the devs tool in inspect and find the id you need") # still a big column then we need id class name
print(result)

#find elements by HTML Class Name:
jobs = result.find_all('div', class_='whatever the class appears on our id finding') # find_all classes
len(jobs) # how many
jobs[0] #lets inspect one of them

title = jobs[0].find('h2') # find ehe element we want from jobs[0]
print(title)

#Extract Text from HTML Elements:
title_link = title.find('a')
link_text = title_link.text # gives us just the text of the link
#clean it up at the begining and at the end:
link_text.strip()

# for all jobs, in a list:
job_titles = [job.find('h2').find('a').text.strip() for job in jobs]
print(job_titles)

# Extract Attributes from HTML Elements:
link = title_link['href'] # that will give me a relative url we need to add the base url
base_url = "https://www.indeed.com"
job_url =  base_url + link  # with this we are now able to access the specific job posting with request:

job_site = requests.get(job_url)
job_soup = BeautifulSoup(job_site.content)
job_soup.text

