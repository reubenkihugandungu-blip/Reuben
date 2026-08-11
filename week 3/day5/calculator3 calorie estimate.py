# Estimates calories burned from walking. Uses approximately 0.04 calories per step.

import math

def estimate_calories(steps, calories_per_step=0.04):# defines a function named estimate calories with parameters steps and an optional calories per step defaulting to 0.04
    calories = steps * calories_per_step
    return math.floor(calories) # returns the floor(integer part) of the calculated calories.
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]
daily_cals = [estimate_calories(s) for s in weekly_steps] # list comprehension: converts each step count to estimated calories using the function

print("Estimated daily calories burned from walking:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"] # list of day labels corresponding to weekly steps
for day, cals in zip(days, daily_cals): # loops over paired day label and daily calorie values
    print(f" {day}: {cals} kcal")
print(f" Total: {sum(daily_cals)} kcal")