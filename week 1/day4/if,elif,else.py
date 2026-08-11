# elif lets you check multiple conditions.
# sometimes there are more than two possible outcomes.
# you do not just want to know if you hit the goal or not.
# you want to know how close you were.

steps = 10000

if steps >= 10000:
    print("Excellent! 10,000 steps. Target exceeded!")
elif steps >= 8000:
    print("On target, 8,000 steps hit.")
elif steps >= 5000:
    print("Halfway there. Below target but moving.")
else:
    print("Below 5,000. Today was sedentary.")
