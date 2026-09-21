import requests
from getpass import getpass

# By using a context manager, you can be sure the session  (with)
# will be released after use.

with requests.Session() as session:
    session.auth = ('bestExampleUserEver', getpass())

    # Instead of requests.get(), you'll use session.get()
    response = session.get('https://api.github.com/user')
    response2 = session.get('https://api.github.com/user/repos')

# You can inspect the response just like before
print(response.headers)
print('This is my first repo!:')
print(response.json()[0]['url'])