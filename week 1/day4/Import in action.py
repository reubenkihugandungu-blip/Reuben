# import is a Python keyword that loads a module into your script. 
# A module is a file of pre-written code that adds extra capabilities. 
# Python ships with many modules built in. When you write import math,
#  you are telling Python: "load the math module so I can use its tools."
#  After that line, you can call functions like math.sqrt() or math.floor() anywhere in your script.
import math

steps = 9578
target = 10000

progress_pct = (steps / target) * 100
rounded = math.floor(progress_pct)  # math.floor rounds DOWN to nearest whole number

print("Steps today:", steps)
print("Progress:", rounded, "%")

if progress_pct >= 100:
    print("Target hit.")
elif progress_pct >= 80:
    print("Close. Push the last", target - steps, "steps")
else:
    print("Still", target - steps, "steps to go.")
# The pattern is always the same: import module_name at the top of your file,
#  then module_name.function() wherever you use it.