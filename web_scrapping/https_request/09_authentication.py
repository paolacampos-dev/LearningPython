import requests
from getpass import getpass #

url = 'https://api.github.com/user'
token= getpass() # must be created in github
headers = {
    "Authorization": f"Bearer {token}",   # barer is a way of sending a token
    "Accept": "application/vnd.github+json"
}

response = requests.get(url, headers=headers)

print(response.status_code)
print(response.json())


#another way is with:
from requests.auth import HTTPBasicAuth