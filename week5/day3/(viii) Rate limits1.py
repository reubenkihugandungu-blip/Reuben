import time

# Simulate making multiple API calls with a delay
member_ids = [1, 2, 3, 4, 5]

def fetch_member(member_id):
    # Simulates what requests.get would return
    mock_data = {
        1: {"name": "James Omondi",  "steps": 9200},
        2: {"name": "Sandra Weru",   "steps": 10500},
        3: {"name": "Patrick Njiru", "steps": 8100},
        4: {"name": "Grace Achieng", "steps": 11000},
        5: {"name": "Brian Kamau",   "steps": 7400},
    }
    return mock_data.get(member_id)

results = []
for mid in member_ids:
    data = fetch_member(mid)
    results.append(data)
    print(f"Fetched: {data['name']} ({data['steps']} steps)")
    # In production: time.sleep(0.5) to avoid rate limits

print(f"\nTotal fetched: {len(results)}")