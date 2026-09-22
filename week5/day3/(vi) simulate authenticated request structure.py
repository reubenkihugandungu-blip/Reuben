import os # OS module  lets the program interact with environment variables

# Simulate: load key from environment

os.environ["SMP_API_KEY"] = "smp_live_abc123xyz"# creates an environment variable named SMP_API_KEY and assigns it a sample API key
api_key = os.getenv("SMP_API_KEY")# reads the smpapikey environment variable and stores its value in api_key

# Build request components (what you would pass to requests.get)
url = "https://api.smptracker.com/v1/members"# stores the API endpoint URL
params = {"city": "Nairobi", "limit": 10}# Defines query parameters. A real request might produce:
headers = { # starts a dict containing HTTP headers.
    "Authorization": f"Bearer {api_key}",# creates an authorization header using an f string
    "Content-Type": "application/json"# says that the request or response uses JSON-formatted data.
} # ends headers dict
print("URL:", url)
print("Params:", params) # prints the query parameters
print("Auth header:", "Bearer " + api_key[:8] + "...")# p only the first eight characters of the API key, followed by ...

# Simulate  a 200 response
print()
print("Response status: 200")# prints HTTP status code 200, which conventionally means the request succeeded
print("Response body: {'members': [...], 'total': 42}")
# ☝️prints a simulated response body containing members and a total count.
# 👉 the script does not send a real request. It only builds the URL, parameters,
#  and headers that could later be passed to something like requests.get(),
#  then prints a fake successful response.