# In Vs code (requires: pip install requests)
# then: call requests.get(url).
#The response object has a .status_code attribute and a .json() method that converts the JSON body
#  into a Python dictionary or list.

import requests

# Example: fetch a user's profile from an API
url = "https://api.example.com/users/amerix"
response = requests.get(url)

print(response.status_code) # 200
data = response.json()  # converts JSON body to Python dict
print(data["followers"]) # 1200000 