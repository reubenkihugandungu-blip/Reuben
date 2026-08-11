# A comprehension can also transform each item. Without a filter, it applies the transformation to every item.
#  Here: convert steps to kilometres (assuming 1.3 km per 1000 steps).

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Convert each step count to km
km_walked = [round(s * 1.3 / 1000, 2) for s in weekly_steps]# creates a new list  called km_walked, uses a list comprehension to process every s value from weekly_steps
print("Steps:", weekly_steps)
print("km :", km_walked)

# Convert each step to calories
calories_per_step =[round(s * 0.04, 2) for s in weekly_steps]
print("Steps:", weekly_steps)
print("Calories burnt:", calories_per_step)