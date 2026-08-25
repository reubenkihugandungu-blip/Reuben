import os

# Step 1: load the token from environment (never hardcode it)
os.environ["FB_ACCESS_TOKEN"] = "EAADemo_token_never_hardcode_real_ones"
token = os.getenv("FB_ACCESS_TOKEN")

# Step 2: This is what the graph API returns for facebook.com/amerix041
fb_response = {
    "id": "100044385041",
    "name": "Amerix",
    "about": "Reproductive health | Men's Health and Wellness",
    "fan_count": 284000,
    "followers_count": 2915000,
    "category": "Health & Wellness Website",
    "link": "https://www.facebook.com/amerix041"
}

#Step 3: Parse it exactly as you have learned
name = fb_response['name']
about = fb_response["about"]
fans = fb_response["fan_count"]
followers = fb_response["followers_count"]
page_link = fb_response["link"]

print("FACEBOOK PAGE DATA")
print(f" page: {name}")
print(f" About: {about}")
print(f"Page likes: {fans:,}")
print(f" Followers: {followers:,}")
print(f" Link: {page_link}")
print()
print(f"Token loaded: {token[:12]}...(never log a live token)")
print()
print("Note: In production, replace the mock response with:")
print(" response = requests.get(url, params={'access_token': token, 'fields': '...'})")
print(" data = response.json()")

# The pattern is always the same. Load the token from an environment variable. Build the URL. 
# Pass the token as a query parameter or header. Parse the JSON response. 
# The Facebook Graph API, the X API, the OpenAI API: they all follow this exact sequence.
#  Handle 401 and 403 errors explicitly so your scripts fail clearly instead of silently.
#  Day 24 puts all of this together into a structured, production-style API script