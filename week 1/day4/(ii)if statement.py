# The simplest form of conditional logic is just an if. It says: if this condition is true, run the code below it.
#  If it is not true, skip it entirely.

# The pattern
# if condition:
    # this runs only when condition is True
    # must be indented

# The indentation matters. Python uses it to know which lines belong inside the if block. 
# Anything indented under the if is part of it. Anything back at the left margin runs regardless.

steps = 9000
if steps >= 8000:
    print("Step target hit.")
    
print("Daily check complete.")



