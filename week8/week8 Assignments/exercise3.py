# JSON SERIALISATION

import json
# Practise converting between Python objects and JSON strings
# This mirrors what JS does with JSON.stringify and JSON.parse
obj = {"tool": "AI Summariser", "version": 1, "active": True}
js_string = json.dumps(obj)
print("Serialised:", js_string)
parsed = json.loads(js_string)
print("Tool name:", parsed['tool'])

