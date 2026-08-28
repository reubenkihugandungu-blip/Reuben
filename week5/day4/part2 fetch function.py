# The fetch function makes the API call and returns clean data or raises an exception.
# It does not process, print, or save. It only fetches. Keep it focused.

# FETCH FUNCTION PATTERN
# Simulates what a fetch function does in a script
def fetch_members(city="Nairobi", limit=50):
    """
    Fetches member data from the SMP API.
    Returns a list of member dicts or raises RuntimeError.
    In production: uses requests.get() with headers and params.
    """
    # Simulate the API response
    mock_response_status = 200
    mock_data = [
        {"id": 1, "name": "James Omondi", "city": "Nairobi", "steps": 9200, "protocol": "OMAD"},
        {"id": 2, "name": "Sandra Weru", "city": "Nairobi", "steps": 10500, "protocol": "2MAD"},
        {"id": 3, "name": "Patrick Njiru", "city": "Mombasa", "steps": 8100, "protocol":"OMAD"},
        {"id": 4, "name": "Grace Achieng", "city": "Nairobi", "steps": 11000, "protocol": "OMAD"},
        {"id": 5, "name": "Brian Kamau", "city": "Kisumu", "steps": 7400, "protocol": "2MAD"},
        {"id": 6, "name": "Kevin mwangi", "city": "Nairobi", "steps": 10800, "protocol": "OMAD"},
    ]

    if mock_response_status != 200:
        raise RuntimeError(f"API error: status {mock_response_status}")# the error message tells us the API failed and shows the status code

# Filter by city
# 👇 this list is a comprehension. means take each member m 
# in mock data and keep only the ones whose city matches the function argument
# So if city is Nairobi only Nairobi Members stay.   

    filtered = [m for m in mock_data if m["city"] == city] 
    return filtered[:limit] # returns up to 50 Nairobi Members

# call the function
members = fetch_members(city="Nairobi")# calls the function with city='Nairobi' the function returns a list of member dict for Nairobi. That list is saved in members
print(f"Fetched {len(members)} members from Nairobi")
for m in members: # Starts a loop it goes through each member in the members list one by one
    print(f" {m['name']}: {m['steps']} steps")
