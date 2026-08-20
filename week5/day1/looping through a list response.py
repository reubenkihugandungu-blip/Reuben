# When an API returns a list of records, response.json() gives you a Python list of dictionaries. 
# Loop through it like any list.
# List of API Records
# Simulates: response.json() from /api/weekly-logs
weekly_logs = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD"},
    {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
    {"day": "Thursday", "steps": 11000, "protocol": "OMAD"},
    {"day": "Friday", "steps": 7600, "protocol": "2MAD"},
]

for log in weekly_logs:
    status = "Goal met" if log["steps"] >= 10000 else "short"
    print(f"{log['day']:10} {log['steps']:10} steps {status}")

# {log['day']: 10} prints the day name, padded to 10 characters wide (right-aligned)
