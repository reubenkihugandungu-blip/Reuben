# full parse and flatten
raw_members = [
    {
        "profile": {"name": "James Omondi", "city": "Nairobi"},
        "metrics": {"steps": 9200, "sleep_hours": 7.5, "bench_press_kg": 80},
        "discipline": {"cold_shower": True, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Grace Achieng", "city": "Mombasa"},
        "metrics": {"steps": 11000, "sleep_hours": 7.0, "bench_press_kg": 60},
        "discipline": {"cold_shower": False, "protocol": "OMAD"}
    },
    {
        "profile": {"name": "Brian Kamau", "city": "Kisumu"},
        "metrics": {"steps": 7400, "sleep_hours": 9.0, "bench_press_kg": 70},
        "discipline": {"cold_shower": True, "protocol": "2MAD"}
    },
]

# Flatten each nested record into one clean dict
flattened = [] # creates an empty list for the cleaned records
for m in  raw_members: # loops through each member m represents one nested member dict
    record = {
        "name": m["profile"]["name"], # extracts values from the nested profile dict
        "city": m["profile"]["city"],
        "steps": m["metrics"]["steps"],
        "sleep": m["metrics"]["sleep_hours"],# extracts values from metrics and gives them shorter names
        "bench": m["metrics"]["bench_press_kg"],
        "protocol": m["discipline"]["protocol"],
        "cold_shower": m["discipline"]["cold_shower"],
    } 
    flattened.append(record) # adds the new flat dict to the flattened list

for r in flattened: # loops through each flattened record
    shower = "yes" if r["cold_shower"] else "no" # uses conditional expression True becomes "yes"
    print(f"{r['name']}, {r['city']}: {r['steps']} steps, {r['protocol']}, shower={shower}")