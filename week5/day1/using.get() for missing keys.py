# Not every response includes every field. A user might not have logged water intake today.
#  If you access a key that does not exist, Python raises a KeyError. 
# Use .get() with a default to handle it safely.

# Safe key access with.get()
records = [
    {"name": "Patrick Njiru", "steps": 9100, "water_glasses": 7},
    {"name": "Grace Achieng", "steps": 8400},  # no water logged
    {"name": "Brian Kamau", "steps": 10200, "water_glasses": 9},
]

for r in records:
    water = r.get("water_glasses", "not logged")
    print(f"{r['name']}: steps={r['steps']}, water={water}")
    
# The second argument to .get() is the default. If the key exists you get its value.
#  If it does not, you get the default instead of a crash.
# 