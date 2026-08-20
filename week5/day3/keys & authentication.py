# An API key is a unique string that identifies your application to an API. 
# It tells the server who is making the request, lets the provider track and limit usage,
#  and prevents unauthorized access to paid or sensitive data.

# The key safety rule
# Never put an API key directly in your code.
# If you paste a key as a string in your script and push that script to GitHub, the key becomes public. 
# Automated bots scan GitHub continuously for leaked keys and will use or sell them within minutes.
#  Always load keys from outside your code.

# This is what you must never do:
# wrong: key harscoded in script
api_key = "sk-abc123yourrealkeyhere"
response = requests.get(url, headers={"Authorization": f"Bearer {api_key}"})