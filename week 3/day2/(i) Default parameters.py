# A default parameter has a value already set in the function definition. 
# If you call the function without providing that argument, Python uses the default.
#  If you do provide it, Python uses what you gave.

# A default parameter is written as parameter=value in the function definition. 
# It gives the parameter a fallback value.
#  You only need to pass an argument for that parameter when you want a different value.

# defines a function named check_steps that takes two parameters: steps and goal.
# goal has a default value of 8000. If the caller does not provide a value for goal, it will default to 8000.

def check_steps(steps, goal=8000): # goal has a default parameter value of 8000
    if steps >= goal:
        print(f"{steps} steps - Goal of {goal} hit!")
    else:
        print(f"{steps} - Goal of {goal} missed.")

# A call that uses the default goal of 8000 steps
check_steps(9200) # calls check_steps with steps=9200 and goal=8000 (default
check_steps(7500) # calls check_steps with steps=7500 and goal=8000 (default)

# Override the default goal
check_steps(9200, goal=10000) # calls check_steps with steps=9200 and goal=10000
check_steps(11500, goal=10000) # calls check_steps with steps=11500 and goal=10000

# Rule: Default parameters must come after non-default parameters in the definition.
#  def func(a, b=10) works. def func(a=10, b) does not.
