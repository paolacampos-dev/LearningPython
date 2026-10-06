import urllib.request
# urllib is a built in py library
# Better to use import requests library (ext dep)


url =  "https://httpbin.org"
response = urllib.request.urlopen(url)

print(response.status)  # 200
print(response.headers) # Date: Tue, 06 Oct 2026 06:31:59 GMT
                        # Content-Type: text/html; charset=utf-8
                        # Content-Length: 9593
                        # Connection: close
                        # Server: gunicorn/19.9.0
                        # Access-Control-Allow-Origin: *
                        # Access-Control-Allow-Credentials: true

print(response.headers['Content-Type']) # text/html; charset=utf-8, but if it doesnt exist will return a KeyError
print(response.headers.get('Content-Type')) # text/html; charset=utf-8, but if the value doesnt exist will return None