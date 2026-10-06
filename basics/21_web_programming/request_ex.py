import requests
# giving a a requests.Response object

# url = "https://api.example.com"
url =  "https://httpbin.org"

# query_parameters = {}
response = requests.get(url)

# response has:
print(response.url) # https://httpbin.org/
print(response.status_code) # 200
print(response.ok)  # True
print(response.headers) # {'Date': 'Tue, 06 Oct 2026 07:06:47 GMT', 'Content-Type': 'text/html; charset=utf-8', 'Content-Length': '9593', 'Connection': 'keep-alive', 'Server': 'gunicorn/19.9.0', 'Access-Control-Allow-Origin': '*', 'Access-Control-Allow-Credentials': 'true'}
print(response.headers.get('Content-Type')) # text/html; charset=utf-8
# print(response.text)    # decoded text (str) as html
# print(response.content) # Response body as bytes



