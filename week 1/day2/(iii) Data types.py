## THE FOUR MAIN DATA TYPES 

# int: whole numbers
# Any number without a decimal point. Steps, glasses of water, reps, sets, pages read, hours of sleep
#  All of these are whole numbers.

steps = 9200
water_glasses = 8
pages_read = 30
sleep_hours = 7
bench_press_reps = 12

# float: decimal numbers
# Any number with a decimal point. Body weight, distances, percentages. When precision matters, 
# use a float.

body_weight_kg = 82.5
km_walked = 7.3
body_fat_percent = 14.2

# str: text
# Any text: words, sentences, names, protocols. Always wrap it in quotes.
# Single or double quotes both work.

fasting_protocol = "OMAD"
skill_of_the_day = "Welding"
name = "Amerix Student"
morning_goal = "8,000 steps before 9 AM"

# bool: True or False
# A yes or no value. Did you do the cold shower? True or False. Is the workout complete? True or False.
#  Did you fast today? True or False. The capital T and F matter.
#  Python will not recognise true or false in lowercase.

cold_shower = True
workout_done = False
fasting_active = True

# ALL FOUR DATA TYPES

steps = 9200 # int
body_weight_kg = 64.6 # float
skill_of_the_day = "Data entry" # str
cold_shower = True # bool

print("Steps today:", steps)
print("Body weight:", body_weight_kg)
print("Skill of the day:", skill_of_the_day)
print("Cold shower:", cold_shower)

print(type(steps))
print(type(body_weight_kg))
print(type(skill_of_the_day))
print(type(cold_shower))
