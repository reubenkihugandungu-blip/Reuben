# json.dumps(): python to JSON text
# json.dumps() takes a Python dictionary or list and converts it into a JSON-formatted string. 
# The s stands for "string".

import json # loads python's built in json module so you can use functions like json.dumps().

daily_log = { # creates a python dict with keys like steps & water glasses, values include numbers, boolean
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}
# convert to JSON string - converts the python dict into json-formatted string
json_text = json.dumps(daily_log) # JSON is a text format so the result is stored in json_text
print("Type:", type(json_text))# shows that json_text is a str not  a dict
print("JSON:", json_text) # prints the JSON string produced from the dict

# pretty print with indentation
pretty = json.dumps(daily_log, indent=2)# converts the dict to JSON again but with indent 2
print("\nPretty JSON:") # prints a blank line then the label.
print(pretty) # prints the nicely formatted JSON string

# indent=2 adds line breaks and indentation to make the output readable.
# Use it when printing JSON for humans.
# Leave it out when sending data to an API.