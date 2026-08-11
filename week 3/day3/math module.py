# A module is a collection of functions and tools packaged into a single file.
#  Use import module_name to load it into your program. 
# Then call functions from it using the format module_name.function_name().
# math gives you mathematical functions beyond basic arithmetic: 
# square roots, rounding, powers, and constants like pi.

import math

# Square root
print("Square root of 144:", math.sqrt(144))

# Round down and round up
print("Floor of 7.9:", math.floor(7.9)) # calls math.floor(7.9) to round 7.9 down to the nearest integer
print("Ceiling of 7.1:", math.ceil(7.1))

#pi- a comment indicating the next line uses the constant pi
print("Pi:", math.pi) # constant pi

# Power: 2 to the power of 10
print("2 to the 10th:", math.pow(2, 10)) # 2 to the power of 10
