from urllib.request import urlopen
from pprint import pprint

# url1 = "https://www.example.com"
# with urlopen (url1) as response:
    #pass

#pprint(response.headers.items())
# [('Date', 'Sat, 12 Sep 2026 06:52:53 GMT'),
#  ('Content-Type', 'text/html'),
#  ('Transfer-Encoding', 'chunked'),
#  ('Connection', 'close'),
#  ('Server', 'cloudflare'),
#  ('last-modified', 'Fri, 11 Sep 2026 17:42:00 GMT'),
#  ('allow', 'GET, HEAD'),
#  ('Accept-Ranges', 'bytes'),
#  ('Age', '6827'),
#  ('cf-cache-status', 'HIT'),
#  ('CF-RAY', 'a39cfdf4495111ce-LHR')]

#pprint(response.getheader("Server"))    #'cloudflare'
#pprint(response.headers["Server"])   #'cloudflare' 

#     body = response.read()

# #Passing from bytes to strings ------------------------------------------------
# #decoded_body = body.decode("utf-8")
# #print(decoded_body[:30]) # <!doctype html><html lang="en"

# #character_set = response.headers.get_content_charset() #currently this website no longer includes explicit character_set. instead now returns a header
# #decoded_body = body.decode(character_set)

# # Converting bytes into files:
# with open("example.html", mode="wb") as html_file:
#     html_file.write(body) #nothing happens then type ls in the terminal, returning all the files in the parent folder(current dir)

# then write in the terminal cat.example.html

#the same for images:
# body = response.read()
# with open("image.jpg", "wb") as image_file:
#     image_file.write(body)

#write bytes to file
url2 = "https://www.google.com"
with urlopen (url2) as response:
    body = response.read()

character_set = response.headers.get_content_charset()
content = body.decode(character_set)

with open("google.html", encoding="utf-8", mode="w") as file:
    file.write(content) # to see it after running the .py command run cat.google.html to see what is on the file