# HEADERS AND AUTH

import urllib.request, json
# 👇Make a request with a custom header
req = urllib.request.Request( # Creates a request object instead of just using a URL string. This allows you to add custom headers.
    "https://httpbin.org/headers", # this is API endpoint
    headers={"X-Custom-Header": "AmerixMasterclass"}# adds a custom HTTP header with key X....
)
with urllib.request.urlopen(req) as r:# opens the HTTP request created above and stores the response in variable r, with closes the connection when done
    data = json.loads(r.read())# reads the raw response data and converts it from JSON into a python dict, storing it in data
print(data["headers"])#Accesses the "Headers" key from the response dict and prints it, which will show all the headers that the server received(including your custom header)