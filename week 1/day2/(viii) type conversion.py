# Type conversion is changing a value from one data type to another. int() converts to an integer,
#  float() converts to a decimal, str() converts to a string, and bool() converts to True or False.
#  You will use these whenever data comes in as the wrong type.

 # CONVERTING BETWEEN TYPES

steps_as_string = "9400" # this is a str, not a number
steps_as_int = int(steps_as_string) # now it is an int

print(type(steps_as_string)) 
print(type(steps_as_int))

# you can now do maths with it
target = 10000
gap = target - steps_as_int
print (f"You need {gap} more steps to hit your target.")

# If you try to do maths on a string, Python will throw a TypeError.
#  For example: "9400" - 1000 causes an error. Convert the string to an int first with int("9400") and you are good.
