# Nested data is when lists and dictionaries contain other lists or dictionaries as values.
#  The outer structure holds the inner one.
#  You access the inner values by chaining square brackets together.

# a list of dictionaries.

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD", "cold_shower": True},
    {"day": "Tuesday", "steps": 10500, "protocol": "OMAD", "cold_shower": True},
    {"day": "Tuesday", "steps": 8800, "protocol": "OMAD", "cold_shower": False},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon", "cold_shower": True},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD", "cold_shower": True},
]
print(week_log)
