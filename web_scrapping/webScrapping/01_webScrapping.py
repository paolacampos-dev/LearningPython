import requests

url = "realpython.github.io/fake-jobs"
response = requests.get(url)

print(response.content[1000:2000])

loc = str(response.content0.find('python'))
print(loc)
print(response.content[loc-10: loc+10])

# also regex can be use to scrap, but still tedius work:
# import re
# re.findall(r'python', str(response.content))