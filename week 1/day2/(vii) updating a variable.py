# Variables Can change

#  A variable is not fixed forever. You can update it any time.
#  Python always uses the most recent value assigned to a name.

steps = 7200
print("Morning count:", steps)

print()

steps = 120 # updating this variable
print("End of day count:", steps)

print()

# adds 600 to the current value
steps = steps + 500
print(f"After evening walk: {steps}")

