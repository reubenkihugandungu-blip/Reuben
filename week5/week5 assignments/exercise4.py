import urllib.request, json
# Fetch a joke from a public API and print it
url = "https://official-joke-api.appspot.com/random_joke" # Stores the API address in the variable url
try: # begins a block of code that might produce an error
    with urllib.request.urlopen(url, timeout=5) as r:# opens the URL and sends a request,waits uo to 5 secs for a response stores the response inr
        joke = json.loads(r.read()) # stores the python dict in variable joke
    print(joke['setup']) # prints the joke's setup using the dict key 'srtup'
    print(joke['punchline'])
except Exception as e: # catches errors that occur in the try block and stores the error in e
    print(f"Could not fetch joke: {e}")# prints the error message, including the specific error details