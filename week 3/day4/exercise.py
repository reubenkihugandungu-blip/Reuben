# You have a list of weekly step counts for four different people. 
# Use list comprehensions to: (1) build a list of all step counts that are above 10,000 from any person.
#  (2) build a list of names of people whose average steps for the week is above 9,000.

people = [
    {"name": "James", "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200]},
    {"name": "Sandra", "steps": [7000, 7500, 6800, 8000, 7200, 8500, 7800]},
    {"name": "Mwangi", "steps": [8500, 9000, 8800, 9200, 8600, 9400, 9100]},
    {"name": "Patrick", "steps": [10000, 11500, 9800, 12000, 10500, 11000, 10800]},
]

# 1. All step counts above 10,000 across all people
all_steps = [s for p in people for s in p["steps"]]
high_steps = [s for s in all_steps if s > 10000]
print("Steps above 10,000:", high_steps)

#2. names with average steps above 9,000
high_avg_names = [p["name"] for p in people if sum(p["steps"]) / len(p["steps"]) > 9000]
print("High average performers:", high_avg_names)