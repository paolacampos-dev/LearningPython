from urllib.request import urlopen
# urlopen is a context manager which with opens the connection to the URL, as response give us the opened connection response.read() reads the data and when python leaves with the with block, the connection is automatically closed


with urlopen ("https://www.example.com") as response:
    body = response.read()

    print(body[:15]) # to see the body  up to 15 = b'<!doctype html>' it re b
