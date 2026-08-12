# Write a function called safe_log_entry(data)
#  that takes a dictionary and tries to extract steps, water, and protocol.
#  If steps is not a valid integer, print an error and return None. If water is missing, use a default of 0.
#  If protocol is missing, use "Unknown". Print a clean report for each valid entry.

def safe_log_entry(data):
    try:
        steps = int(data["steps"])
    except (ValueError, TypeError, KeyError):
        print("Invalid steps data. Skipping entry.")
        return None
    
    water = data.get("water", 0)
    protocol = data.get("protocol", "Unkwown")
    print(f"Steps: {steps} | Water: {water} glasses | Protocol: {protocol}")
    return steps

entries = [
    {"steps": "9200", "water": 8, "protocol": "OMAD"},
    {"steps": "bad", "water": 7, "protocol": "2MAD"},
    {"steps": "8800", "protocol": "OMAD"},
    {"steps": "11000", "water": 9},
]

results = [safe_log_entry(e) for e in entries]
valid = [r for r in results if r is not None]
print(f"\nValid entries: {len(valid)}")