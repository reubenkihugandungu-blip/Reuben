# You rarely want everything an API returns. Filter using the list comprehension pattern from Week 3.

# Filter API results
logs = [
    {"name": "James Omondi", "steps": 9200, "protocol": "OMAD"},
    {"name": "Sandra Weru", "steps": 10500, "protocol": "2MAD"},
    {"name": "Patrick Njiru", "steps": 8100, "protocol": "OMAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau", "steps": 7400, "protocol": "2MAD"},
    {"name": "Kevin Mwangi", "steps": 10800, "protocol": "OMAD"},
]

# OMAD users who hit 10,000 steps
goal_hitters = [
    r for r in logs
    if r ["protocol"] == "OMAD" and r["steps"] >= 8000
]

print("OMAD users who hit 8k steps:")
for r in goal_hitters:
    print(f" {r['name']}: {r['steps']} steps")

# Try this:
# Change the filter to show only 2MAD users. Then change the step threshold to 8000 and see who qualifies.