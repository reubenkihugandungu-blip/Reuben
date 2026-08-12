# json.loads(): JSON Text to Python
# json.loads() takes a JSON string and converts it back into Python data (a dictionary or list). 
# This is what you use when you receive data from an API.

import json

# This is what an API response might look like
api_response = '{"steps": 9200, "water_glasses": 8, "cold_shower": true, "protocol": "OMAD"}' #  defines a JSON string

# Convert JSON string to python dictionary stored in data
data = json.loads(api_response)

print("Type:", type(data)) # p the type of data
print("Steps:", data["steps"]) # Reads the steps value from the dictinary and prints it.
print("Cold shower:", data["cold_shower"]) # reads the cold shower value and prints it Json true becomes python True after conversion
print("Protocol:", data["protocol"])