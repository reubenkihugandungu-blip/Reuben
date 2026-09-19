# Exercise

# Create a file called day2.py. Build a personal stats summary for one day of the SMP.
#  Store each value as the correct data type:

# Your name (string)
# Steps walked today (integer)
# Hours of sleep (float)
# Water glasses (integer)
# Cold shower completed (boolean)
# Current skill being learned (string)

# Then print a formatted summary using f-strings.
#  One line per metric. End with a line that says how many steps are left to reach 10,000.

name = "Reuben"
steps_walked_today = 8421
hours_of_sleep = 7.5
water_glasses = 4
cold_shower_completed = True
current_skill = "Python"

print(f"Name: {name}")
print(f"Steps walked today: {steps_walked_today}")
print(f"Hours of sleep: {hours_of_sleep}")
print(f"Water glasses: {water_glasses}")
print(f"Cold shower completed: {cold_shower_completed}")
print(f"Current skill being learned: {current_skill}")
print(f"Steps left to reach 10,000: {10000 - steps_walked_today}")
print(f" My name is {name}, I walked {steps_walked_today} steps today and slept {hours_of_sleep} hours.")
      