# Local scope: a variable created inside a function. It only exists while the function is running. 
# It disappears when the function ends. Global scope: a variable created outside all functions. 
# It exists for the entire program and can be read inside functions.

step_goal = 8000 # global variable
def check_today(steps):
    result = "hit" if steps >= step_goal else "missed" # result is a local variable
    print(f"Goal {result}: {steps} steps")

check_today(9200) # calls check_today with steps=9200
check_today(7000) # calls check_today with steps=7000

# This will throw an error because result is a local variable and cannot be accessed outside the function.
# print(result)