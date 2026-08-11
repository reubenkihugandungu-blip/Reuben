#  type conversion is changing a value from one data type to another.

steps_as_string = "9400" # this is a str, not a number
steps_as_int = int(steps_as_string) # now it is an int

print(type(steps_as_string)) 
print(type(steps_as_int))

# you can now do maths with it
target = 10000
gap = target - steps_as_int
print (f"You need {gap} more steps to hit your target.")
