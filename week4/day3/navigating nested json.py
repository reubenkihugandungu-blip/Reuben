# Real API responses often have nested data: dictionaries inside dictionaries, or lists inside dictionaries. 
# Navigate them by chaining square brackets.

import json

# Simulated API response with nested data
api_json = '''
{
"client": "James Omondi",
"week": 1,
"daily_logs": [
{"day": "Monday", "steps": 9200, "protocol": "OMAD"},
{"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
{"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
{"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon"},
{"day": "Friday", "steps": 7600, "protocol": "OMAD"}
]
}
'''

data = json.loads(api_json)

print("Client:", data["client"])
print("week:", data["week"])
print()

for log in data["daily_logs"]:
    status = "OK" if log["steps"] >= 8000 else "low"
    print(f" {log['day']} {log['steps']} steps ({status})")
    