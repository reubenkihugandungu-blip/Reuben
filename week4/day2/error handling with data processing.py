# In practice, you use error handling when processing data that may have gaps or inconsistencies.
#  Here is a list of daily logs with some missing or bad values:

daily_logs = [
    {"day": "Monday", "steps": 9200},
    {"day": "Tuesday", "steps": "not recorded"},
    {"day": "Wednesday", "steps": "10500"},
    {"day": "Thursday", "steps": None},
    {"day": "Friday", "steps": "8800"},
]

valid_steps = [] # creates an empty list to store only the successfully parsed step counts.
for log in daily_logs: # loops through each daily log dictionary
    try:  # attempts to cenvert log [steps] into an integer with int(log[steps]), stores the integer in steps appends it to valid_steps
        steps = int(log["steps"])
        valid_steps.append(steps)
        print(f"{log['day']}: {steps} steps")
    except: (ValueError, TypeError) # intended to catch invalid conversions caused by bad data
    print(f"{log['day']}: invalid data - skipped")

if valid_steps: # checks whether any valid step values were collected.
    avg = sum(valid_steps) / len(valid_steps)
print(f"\nAverage from valid days: {round(avg)} steps") 