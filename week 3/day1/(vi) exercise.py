# Write a function called day_report(steps, water, protocol) that prints a formatted report of
#  a day's discipline data. Then write a second function called hit_goal(steps) 
# that returns True if steps is 8000 or more, and False if not. 
# Call both functions with at least three different sets of values.
# this exercise involves dictionary, multiple parameters, and return.

def day_report(steps, water, protocol):
    print("--- Daily Report ---")
    print(f"Steps   : {steps}")
    print(f"Water   : {water} glasses")
    print(f"Protocol: {protocol}")

def hit_goal(steps): # declares a function called hit_goal that takes one parameter, steps
    return steps >= 8000

day_report(9200, 8, "OMAD")
day_report(7500, 6, "2MAD")
day_report(11000, 10, "Autophagy Marathon")

print("Goal hit (9200)?", hit_goal(9200))
# calls the hit_goal function with 9200 as the argument and prints the result
# it also evaluates to True because 9200 is greater than or equal to 8000 and 
# then prints a boolean result of True
print("Goal hit (7500)?", hit_goal(7500))
print("Goal hit (11000)?", hit_goal(11000))



