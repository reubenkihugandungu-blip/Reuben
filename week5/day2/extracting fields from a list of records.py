# A common pattern: the API returns a list of records.
#  Loop through each one and pull only the fields you want. Build a clean list from the raw data.

# Extract specific fields
# Raw API response: list of full user records
raw = [
    {"id": 1, "name": "James Omondi", "email": "james@smp.ke", "steps": 9200, "protocol": "OMAD", "sleep": 7.5, "active": True},
    {"id": 2, "name": "Sandra Weru", "email": "sw@smp.ke", "steps": 10500, "protocol": "2MAD", "sleep": 8.0, "active": True},
    {"id": 3, "name": "Patrick Njiru", "email": "pn@smp.ke", "steps": 8100, "protocol": "OMAD", "sleep": "OMAD", "sleep": 6.5, "active": False},
    {"id": 4, "name": "Grace Achieng", "email": "ga@smp.ke", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "active": True},
    {"id": 5, "name": "Brian Kamau", "email": "bksmp.ke", "steps": 7400, "protocol": "2MAD", "sleep": 9.0, "active": True},
]

# Extract only active users with name, steps, protocol
# starts of a list comprehension that creates a new clean list. # line 15 to 19 dict definition inside the comprehension
# for each record, create a new dict with only 3 fields: name,steps, and protocol.
# The variable r represents each raw record.
clean = [   
    { 
        "name": r["name"],
        "steps": r["steps"],
        "protocol": r["protocol"]
    }
    for r in raw if r["active"] # loop through each record in the raw list(calling it r), but only include records where r[active] is true filters inactive users
]

for record in clean: # loop through each record in the newly created clean list
    print(f"{record['name']:20} {record['steps']:6} steps {record['protocol']}")