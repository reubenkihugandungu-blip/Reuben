# a list called week_log with 5 dictionaries.
#  Each dictionary should have keys for day, steps, and protocol.
#  Write a loop that prints each day's details. 
# After the loop, calculate and print the average step count across all five days.

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD"}, 
    {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marathon"},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD"},
]

total = 0 # creates a variable total and sets it to 0. this will accumulate the sum of steps.
for log in week_log: # begins a for loop, each iteration sets log to one dictionary from week log.
    print(log["day"], "|", log["steps"], "steps |", log["protocol"])# p the current dictionary's day,step count and protocol in a readable format.
    total += log["steps"] # adds the current day's step count to the running total.

average = total / len(week_log)# calculates the average steps by dividing the total steps by the number of days in week_log
print()
print("Average steps:", average)
