from bs4 import BeautifulSoup
from urllib.request import urlopen

url = "http://olympus.realpython.org/profiles/dionysus"
page = urlopen(url) # fetches the content from the internet and save it in the page variable
html = page.read().decode("utf-8") # to be able to read without problems
soup = BeautifulSoup(html, "html.parser") # "html.parser" is the parser included in py (other external ones as lxml, html5lib)


# in the terminal python3 -i soupy.py to interact directly in the terminal instead of working with print to be able to see:

# soup (press enter) 
# <html>
# <head>
# <title>Profile: Dionysus</title>
# </head>
# <body bgcolor="yellow">
# <center>
# <br/><br/>
# <img src="/static/dionysus.jpg"/>
# <h2>Name: Dionysus</h2>
# <img src="/static/grapes.png"/><br/><br/>
# Hometown: Mount Olympus
# <br/><br/>
# Favorite animal: Leopard <br/>
# <br/>
# Favorite Color: Wine
# </center>
# </body>
# </html>

#in the terminal: >>>
# >>>soup.title
# <title>Profile: Dionysus</title>

# >>> type(soup.title)
# <class 'bs4.element.Tag'>

# >>> soup.title.get_text()
# 'Profile: Dionysus'

# >>> soup.img   --> it will give me just the first image
# <img src="/static/dionysus.jpg"/>

# >>> soup.title.parent
# <head>
# <title>Profile: Dionysus</title>
# </head>

# >>> soup.center
# <center>
# <br/><br/>
# <img src="/static/dionysus.jpg"/>
# <h2>Name: Dionysus</h2>
# <img src="/static/grapes.png"/><br/><br/>
# Hometown: Mount Olympus
# <br/><br/>
# Favorite animal: Leopard <br/>
# <br/>
# Favorite Color: Wine
# </center>

# >>> soup.center.children
# <generator object Tag.children.<locals>.<genexpr> at 0x710629df5000>

# >>> list(soup.center.children)
# ['\n', <br/>, <br/>, '\n', <img src="/static/dionysus.jpg"/>, '\n', <h2>Name: Dionysus</h2>, '\n', <img src="/static/grapes.png"/>, <br/>, <br/>, '\nHometown: Mount Olympus\n', <br/>, <br/>, '\nFavorite animal: Leopard ', <br/>, '\n', <br/>, '\nFavorite Color: Wine\n']

# Get the value of some of those attributes using dictionaries:
# >>> soup.img["src"]
# '/static/dionysus.jpg'

# Search the parse tree:
# >>> soup.find("img")
# <img src="/static/dionysus.jpg"/>

# >>> soup.find_all("img")
# [<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]

# >>> soup.find_all("img")[1]
# <img src="/static/grapes.png"/>

# >>> soup.select("img")
# [<img src="/static/dionysus.jpg"/>, <img src="/static/grapes.png"/>]
# >>> soup.select_one("img")
# <img src="/static/dionysus.jpg"/>

# >>> soup.select_one("img:nth-of-type(2)")
# <img src="/static/grapes.png"/>

# How to modify a parse with been working with  --> lets change the name of a profile pict:
# >>> profile_image = soup.find("img")
# >>> profile_image
# <img src="/static/dionysus.jpg"/>
# >>> profile_image["src"]
# '/static/dionysus.jpg'
# >>> profile_image["src"] = '/static/poseidon.jpg'
# >>> profile_image
# <img src="/static/dionysus.jpg"/>

# if we want to create a new HTML with that new content to save it into a file
# >>> with open("output.html", "w", encoding="utf-8") as file:
# ...     file.write(str(soup.prettify()))
# ... 
# 390
# exit()

# in the terminal: cat output.html
# <html>
#     <head>
#         <title>
#             Profile: Dionysus
#         </title>
#     </head>
#     <body bgcolor="yellow">
#         <center>
#             <br/>
#             <br/>
#             <img src="/static/poseidon.jpg"/>
#             <h2>
#                 Name: Dionysus
#             </h2>
#             <img src="/static/grapes.png"/>
#             <br/>
#             <br/>
#                 Hometown: Mount Olympus
#             <br/>
#             <br/>
#                 Favorite animal: Leopard
#             <br/>
#             <br/>
#                 Favorite Color: Wine
#         </center>
#     </body>
# </html>