# The key advantage of NumPy is that math operations apply to every element at once, without a loop. 
# This is called vectorization.

# VECTORIZED MATH OPERATIONS
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
goal = 10000

# All at once, no loop needed
deficit = steps - goal
print("Steps vs 10k goal:", deficit)

# Percentage of goal achieved
percent = (steps / goal * 100).round(1)
print("Percent of goal achieved:", percent)

# Boolean mask: which days hit the goal?
hit = steps >= goal
print("Hit goal:", hit)
print("Days hitting goal:", steps[hit])

# Using a boolean array inside brackets filters the array.
# steps[steps >= goal] returns only the values where the condition is True. No loop, no list comprehension needed.