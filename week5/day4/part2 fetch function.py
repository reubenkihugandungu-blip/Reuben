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
        raise RuntimeError(f"API error: status {mock_response_status}")

    # Filter by city
    filtered = [m for m in mock_data if m["city"] == city] 
    return filtered[:limit]

# call the function
members = fetch_members(city="Nairobi")
print(f"Fetched {len(members)} members from Nairobi")
for m in members:
    print(f" {m['name']}: {m['steps']} steps")
