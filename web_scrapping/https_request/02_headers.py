# If the request is not behaving as expected, we inspect headers 
# The server may need additional information to decide how to respond. (headers)

    # Header ---------> What it tells the server:
    # User-Agent	    What client/browser is making the request
    # Accept	        What type of response you want
    # Content-Type	    What format your request body is
    # Authorization	    Credentials/token for accessing something
    # Cookie	        Information stored from previous interactions
    # Accept-Language	Preferred language

from urllib.request import Request, urlopen

url = "https://example.com"

with urlopen(url) as response:
    pass
print(response.headers.items())
# [('Date', 'Fri, 11 Sep 2026 09:08:19 GMT'), ('Content-Type', 'text/html'), ('Transfer-Encoding', 'chunked'), ('Connection', 'close'), ('Server', 'cloudflare'), ('last-modified', 'Thu, 10 Sep 2026 21:00:47 GMT'), ('allow', 'GET, HEAD'), ('Accept-Ranges', 'bytes'), ('Age', '10387'), ('cf-cache-status', 'HIT'), ('CF-RAY', 'a39586f4bc8d243d-LHR')]

#------------------------------------------------------------------------------

# once you know your headers we can use them in the request:

# request = Request(
#     url, 
#     headers={
#         "User-Agent": "Mozilla/5.0",
#         "Accept": "application/json",
#         "Accept-Language": "en-US"
#     })

# or:
# headers = {
#     "User-Agent": "Mozilla/5.0",
#     "Accept": "application/json",
#     "Accept-Language": "en-US"
# }

# request = Request(url, headers=headers)

