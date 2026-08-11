# A list comprehension is a one-line way to build a new list from an existing one.
#  The format is: [expression for item in iterable if condition]. 
# The if condition part is optional. It creates a new list without changing the original.

# [...] the outer brackets creates a new list.
# steps - the value to put in the new list & each step count that passes the test.
# for steps in weekly_steps loop through the original list
# if steps >= 8000 Only include if this is True

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = [steps for steps in weekly_steps if steps >= 8000]

print(goal_days)