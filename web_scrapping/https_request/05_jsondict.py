from urllib.request import urlopen
import json

url2 = "https://www.google.com"

with urlopen(url2) as response:
    print(response.status)

#httpbin is a server that allows us to experiment with different of requests of responses (similates an API)
with urlopen("https://httpbin.Sorg/json") as response:
    body = response.read()

#character_set = response.headers.get_content_charset()
#print(character_set) 
print(type(body)) #bytes
data = json.loads(body)
print(type(data))
print(data)