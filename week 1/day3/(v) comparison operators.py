# Operator	        Meaning                   Example	                             Result
# ==	           Is equal to	              steps == 8000	                       True or False
# !=	           Is not equal to	          fasting != "None"	                   True or False
# >	               Is greater than	           steps > 8000	                       True or False
# <	               Is less than	               sleep_hours < 7	                   True or False
# >=	           Greater than or equal	steps >= 8000	                       True or False
# <=	           Less than or equal	     water <= 8	                           True or False

# The double equals == checks if two things are equal. 
# The single equals = stores a value. They look similar but do completely different things. 

# Comparison operators in action

steps = 9200
water_glasses = 8
sleep_hours = 5
fasting = "OMAD" # fasting != "None"  True or False

print(steps >= 8000) # Did I hit my step target?
print(water_glasses == 8) # Did I drink exactly 8 glasses?
print(sleep_hours < 6) # Did I sleep under 6 hours?
print(fasting != "None")  # Am I on a fasting protocol?
print(steps > 10000) # Did I exceed- 10,000 steps?