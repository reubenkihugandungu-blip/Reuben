import math

total_days = 50
training_days_per_week = 5
weeks = total_days / 7

print(f"Total days: {total_days}")
print(f"Full weeks: {math.floor(weeks)}") # takes the value of weeks and rounds down to the nearest whole number

# Distance calculation using pythagoras
walk_east = 3.0 # km
walk_north = 4.0 # km
distance = math.sqrt(walk_east**2 + walk_north**2)
print(f"Direct distance: {distance} km")