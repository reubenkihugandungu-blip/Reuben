# Slicing NumPy arrays uses the same syntax as Python lists. 
# The difference is that slices of NumPy arrays are views, not copies. Changing a slice changes the original.

# SLICE AND INDEX ARRAYS
import numpy as np

steps = np.array([9200, 10500, 8800, 11000, 7600, 9400, 10200])
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

print("First 3 days:", steps[:3])
print("Last 2 days:", steps[-2:])
print("Weekdays (Mon-Fri):", steps[:5])
print("Weekend:", steps[5:])

print()
# Best week start: first day above 10k steps
first_10k = np.argmax(steps >= 10000) # index of first True value
print(f"First 10k+ day: {days[first_10k]} with {steps[first_10k]:,} steps")

# Sort and show progression
sorted_steps = np.sort(steps)
print("Steps sorted low to high:", sorted_steps)