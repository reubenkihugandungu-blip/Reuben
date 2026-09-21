# A function is a named block of code. You define it once. 
# You call it as many times as you want. When you call it, Python runs the code inside it.

# A function is a reusable block of code with a name. 
#  You create it using def followed by the name and parentheses. 
# The code inside is indented. You run it by writing the function name followed by parentheses.

# DEFINING AND CALLING A FUNCTION

# Two steps:
#  define the function with def, then call it by name.
#  Defining does not run the code.Calling does.

# Step	                What happens
# Define: def greet():	Python stores the function. Nothing runs yet.
# Call: greet()	        Python runs the code inside the function.

def show_daily_goal():
    print("Step goal: 8,000 steps")
    print("Water goal: 8 glasses")
    print("Cold_shower: yes")

# Calling the function

show_daily_goal()
print("---")
show_daily_goal() # calling the function again

# Important: The function definition must come before the call. 
# Python reads top to bottom. If you call a function before it is defined, you get an error.