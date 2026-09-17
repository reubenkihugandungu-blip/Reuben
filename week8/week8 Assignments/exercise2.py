# FETCH LOGIC

import urllib.request, json
# Replicate what the Fetch API does in Python
# Make a GET request and handle the response
url = 'https://httpbin.org/get'
with urllib.request.urlopen(url) as r:
    data = json.loads(r.read())
print('Status: 200 OK')
print('Origin IP:', data.get('origin', 'unknown'))