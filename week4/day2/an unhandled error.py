# This will crash
steps = "nine thousand"
goal = 8000
if steps >= goal: # can't compare string to a number
    print("Goal hit")

# Python shows TypeError and stops. Nothing after the error runs.