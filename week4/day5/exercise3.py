import json
# Create a Python dictionary and convert it to JSON
# Then parse it back and access a value

data  = {"name": "Eric", "age": 30, "city": "Nairobi"}
json_str = json.dumps(data, indent=2)# converts the dictionary to a JSON string, jsondumps serializes python data into jason format & indent 2 formats it with 2space indentation for readability
print(json_str)
parsed = json.loads(json_str)# converts the JSON string back into a python dict, jsonloads( deserializes json text into a python object)
print(f"Name: {parsed['name']}")# accesses the 'name' key from the parsed dict and prints it with an f string