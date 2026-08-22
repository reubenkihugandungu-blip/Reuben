# APIs accept keys in two main ways. Check the documentation for the specific API you are using.
#Method A: Query Parameter in the URL

# Key passed as a URL parameter
url = f"https://api.weatherprovider.com/current?city=Nairobi&apikey=(api_key)"
response = requests.get(url)

# Or using the params dict(cleaner)
params = {
    "city": "Nairobi",
    "apikey": api_key
}
response = requests.get("https://api.weatherprovider.com/current", params=params)

# Method B: Authorization Header
# A Bearer token is a type of access credential sent in an HTTP request header to prove you are allowed to use an API.
#  "Bearer" means the person holding (bearing) this token is authorised to make the request.
#  You pass it in the Authorization header with the format Bearer YOUR_TOKEN_HERE. 
# This is the authentication pattern used by OpenAI, X (Twitter), and most modern APIs. 
# Your Bearer token is just as sensitive as a password: 
# keep it in your .env file and never paste it into code you push to GitHub.

# Bearer token (used by OpenAi, many modern APIs)
headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}
response = requests.get(url, headers=headers)

# Or as a custom header(varies by API)
headers = {"X-API-KEY": api_key}
response = requests.get(url, headers=headers)
