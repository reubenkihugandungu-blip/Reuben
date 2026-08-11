# A for loop through a list of dictionaries gives you one dictionary per iteration.
# Inside the loop, use the key names to get what you need.
# below is a code that loops through the weekly log, checks whether each day reached at least 8000 steps,
#  and prints the day, step count, and goal status.
week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD"},
    {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marthon"},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD"},
]
for log in week_log: # each loop iteration assigns one dictionary from week_log to the variable log.
    status = "Goal hit" if log["steps"] >= 8000 else "Below goal" # checks the "steps" value inside the current log dictionary.
    print(log["day"], log["steps"], status) # log["day"] day name log["steps"] the step count, status either goal hit or below goal.

