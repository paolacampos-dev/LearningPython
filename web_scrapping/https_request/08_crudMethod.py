import requests
url = "https://httpbin.org/"

# As DATA:======================================================================================
# Sent as DICTIONARY ---------------------------------------------------------------------------
# response = requests.post(url + 'post', data={'key': 'value', 'brand':'Ford', 'year': '2007'})
# print(response.status_code) # 200
# print(response.headers) # {'Date': 'Sat, 19 Sep 2026 04:24:15 GMT', 'Content-Type': 'application/json', 'Content-Length': '478', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
# print(response.headers['content-type']) # application-json

# response = requests.put(url + 'put', data={'key': 'value'})
# print(response.status_code) # 200

# response = requests.delete(url + 'delete', data={'key': 'value'})
# print(response.status_code) # 200
# json_response = response.json()
# print(json_response) # {'args': {}, 'data': '', 'files': {}, 'form': {'brand': 'Ford', 'key': 'value', 'year': '2007'}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '30', 'Content-Type': 'application/x-www-form-urlencoded', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.2', 'X-Amzn-Trace-Id': 'Root=1-6aae12f2-29ec645e007abe7d309da723'}, 'json': None, 'origin': '188.29.127.4', 'url': 'https://httpbin.org/post'}
#print(json_response['headers']['Content-Type']) # application/x-www-form-urlencoded

# Sent as List of TUPLES
# response = requests.post(url, data=[('key', 'value'), ('brand', 'Ford'), ('year', '2007')])
# print(response) # 405 method not allowed for that url/endpoint
# json_response = response.json()
# print(json_response)
# print(json_response['headers']['Content-Type'])
# print(json_response['form'])

# as JSON ====================================================
response = requests.post(url + 'post', json={'key': 'value', 'brand':'Ford', 'year': '2007'})
print(response) # 200
json_response = response.json()
print(json_response) # {'args': {}, 'data': '{"key": "value", "brand": "Ford", "year": "2007"}', 'files': {}, 'form': {}, 'headers': {'Accept': '*/*', 'Accept-Encoding': 'gzip, deflate', 'Content-Length': '49', 'Content-Type': 'application/json', 'Host': 'httpbin.org', 'User-Agent': 'python-requests/2.34.2', 'X-Amzn-Trace-Id': 'Root=1-6aae1666-5209645a0184418864589574'}, 'json': {'brand': 'Ford', 'key': 'value', 'year': '2007'}, 'origin': '188.29.127.4', 'url': 'https://httpbin.org/post'}
print(json_response['headers']['Content-Type']) # application/json
print(json_response['form']) # {}