# You can raise exceptions yourself using raise. 
# This is useful when you want to enforce rules inside a function, such as a step count that must be a positive number.

def log_steps(steps):# defines a function named log_steps and takes one argument steps.
    if not isinstance(steps, int):# checks whether steps is not an integer, returns True only for integer values.
        raise TypeError("Steps must be an integer.") # raises a exception when steps is not an integer. this stops normal excecution and signals that the input type is wrong.
    if steps < 0:# checks whether steps is a negative number. This enforces the rule that step counts must be non-negative. 
        raise ValueError("Steps cannot be negative.")
    print(f"Steps logged: {steps}") # Prints a confirmation message showing the valid step count. This runs only if no error was raised.

try:# starts a block where exceptions can be caught and handled. The code inside is tested for errors.
    log_steps(9200) # calls log_steps with a valid integer, this should print steps logged: 9200.
    log_steps('nine thousand')# calls logsteps with a negative integer, this triggers the ValueError inside the function.
except ValueError as e:# catches ValueError exceptions raised in the try block. The exception is stored in the variable e
    print("valueError:", e)
except TypeError as e:
    print("TypeError:", e)# prints the error type and its message, this would run if logsteps received a non-integer value

# Change log_steps(-500) to log_steps("nine thousand") and run it again. 
# Notice that the TypeError block catches it this time.