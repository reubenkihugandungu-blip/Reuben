# Write a function called weekly_report(name, steps_list, goal=8000) 
# that takes a name, a list of step counts, and an optional goal.
#  The function should calculate
#  how many days hit the goal and print a summary including the name, total days, days on target, and average steps. 
# Test it with two different names and step lists.

def weekly_report(name, steps_list, goal=8000):
    days_on_target = 0 # creates a counter variable days_on_target and initializes it to 0
    for steps in steps_list:# starts a loop to process each steps value in steps_list
        if steps >= goal:
            days_on_target += 1# if condition is true, increments the days_on_target counter by 
    avg = sum(steps_list) // len(steps_list)
    print(f"---- {name}'s week ----")
    print(f"Days tracked : {len(steps_list)}")
    print(f"Days on goal : {days_on_target}")
    print(f"Average steps: {round(avg, 0)}")
    print()

weekly_report("James", [9200, 7500, 10500, 8800, 8800, 6900, 11000, 9600])
weekly_report("Sandra", [10000, 10200, 9800, 11000, 10500], goal=10000)

# 19 calls the weekly_report for james with 8 step values and the default goal of 8000.
# 20 calls the weekly_report for sandra with 5 step values and a custom goal of 10000.