from urllib.request import urlopen


with urlopen ("https://www.example.com") as response:
    body = response.read()

    print(body[:15]) # to see the body  up to 15 = b'<!doctype html>' it re b
