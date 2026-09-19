# sometimes there are more than two possible outcomes.
# you do not just want to know if you hit the goal or not.
# you want to know how close you were.

# That is what elif is for. It stands for "else if" and lets you check multiple conditions one after the other.
# Python reads them from top to bottom. The moment it finds one that is true, it runs that block and skips all the rest.

# IF + ELIF + ELSE: GRADED STEP CHECK

steps = 10000

if steps >= 10000:
    print("Excellent! 10,000 steps. Target exceeded!")
elif steps >= 8000:
    print("On target, 8,000 steps hit.")
elif steps >= 5000:
    print("Halfway there. Below target but moving.")
else:
    print("Below 5,000. Today was sedentary.")

# Try these values one at a time: 11000, 9500, 6000, 3000. Each one triggers a different branch.
#  Only one branch ever runs per execution.