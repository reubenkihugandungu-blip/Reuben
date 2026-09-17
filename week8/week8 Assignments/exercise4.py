# CHALLENGE 

import urllib.request, json
# Build a simple data fetcher that returns formatted output
# Like a mini backend endpoint would
def fetch_data(url):
    try:
        with urllib.request.urlopen(url, timeout=5) as r:
            return json.loads(r.read())
    except Exception as e:
        return {"error": str(e)}

result = fetch_data('https://httpbin.org/json')
print(json.dumps(result, indent=2))
