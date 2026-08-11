# Parameters - passing information in.
# A parameter is a variable in the function definition, that receives a value when you call it. 
# In this example, the parameter is steps.
# The function will check the value of steps and print a message based on the value.
# An argument is the value you provide when calling the function. The argument goes into the parameter.

def check_steps(steps):
    if steps >= 10000:
        print(steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print(steps, "steps - Goal hit")
    else:
        print(steps, "steps - Below goal")
        
# call with different values.
check_steps(9200)
check_steps(7500)
check_steps(11000)
