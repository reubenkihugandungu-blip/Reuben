# HTTP REQUESTS

import urllib.request, json# imports two python modules urllib.request(for making HTTP requests) and json for working with json data
# Fetch a public API and print the response
url = "https://httpbin.org/json"# stores a URL string in the variable url. this is a public API endpoint that returns JSON data
# 👇 Opens a connection to the URL and gets the response.
# The with statement automatically closes the connection when done.
# the response object is stored in the variable response.
with urllib.request.urlopen(url) as response:
    print(f"Status Code: {response.status}")
    data = json.loads(response.read())# reads the raw response data using .read(), then converts it from JSON format into a python dict/object using json.loads() the results is stored in data
print(json.dumps(data, indent=2))# converts the python dict back into JSON format using json.dumps
# print(data) # prints python dict