import requests

url =  "https://httpbin.org/get" # specific endpoint provided by httpbin
response = requests.get(url)
data = response.json()
print(data) # {'args': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.2', 'X-Amzn-Trace-Id': 'Root=1-6ac4a334-412f9b9943f561d57ab523a6'}, 'origin': '188.29.127.40', 'url': 'https://httpbin.org/get'}