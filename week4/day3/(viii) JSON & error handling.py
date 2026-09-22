# Always wrap JSON parsing in a try-except block. 
# If the JSON string is malformed, Python raises a json.JSONDecodeError.

import json

responses = [
    '{"steps": 9200, "protocol": "OMAD"}',
    'not valid json at all',
    '{"steps": 10500, "protocol": "2MAD"}'
]

for r in responses:
    try:
        data = json.loads(r)
        print(f"Parsed OK: {data['steps']} steps")
    except json.JSONDecodeError:
        print(f"Invalid JSON: {r[:30]}...")