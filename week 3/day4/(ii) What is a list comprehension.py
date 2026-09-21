# A list comprehension is a one-line way to build a new list from an existing one.
#  The format is: [expression for item in iterable if condition]. 
# The if condition part is optional. It creates a new list without changing the original.

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

goal_days = [steps for steps in weekly_steps if steps >= 8000]

print(goal_days)

# Same result. One line instead of four.

# Breaking Down the Syntax

# Part	                       What it means	                    In the example
# [...]	                    Creates a new list	                  the outer brackets
# steps	                The value to put into the new list	      each step count that passes the test
# for steps in weekly_steps	Loop through the original list	        goes through each of the 7 days
# if steps >= 8000	      Only include if this is True	           keeps only days with 8000 or more steps