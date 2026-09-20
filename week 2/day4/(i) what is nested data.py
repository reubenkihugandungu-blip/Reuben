# Nested data means putting one data structure inside another. 
# A list can contain dictionaries. A dictionary can contain lists. 
#  The outer structure holds the inner one.
#  You access the inner values by chaining square brackets together.

#  A list of dictionaries.

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD", "cold_shower": True},
    {"day": "Tuesday", "steps": 10500, "protocol": "OMAD", "cold_shower": True},
    {"day": "Tuesday", "steps": 8800, "protocol": "OMAD", "cold_shower": False},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon", "cold_shower": True},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": True},
]
print(week_log)
