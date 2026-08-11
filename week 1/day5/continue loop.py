# continue skips the rest of the current loop iteration and jumps straight to the next one.
#  The loop does not stop. It just skips the current item.

daily_steps = [3200, 7100, 9800, 4100, 10500, 6400] # a list of step counts for each day.
minimum = 7000 # threshold for a valid day.

total = 0 # 0 means starts at 0
valid_days = 0

for steps in daily_steps:
    if steps < minimum: # if the steps are below minimum, it prints a skip message and continue.
        print(f"Skipping {steps} (below minimum)")
        continue # stops the current iteration immediately and jumps to the next day.
    total += steps # if the day is valid it adds steps to total.
    valid_days += 1 # if the day is valid it adds the day to valid days.

print((f"\nValid days: {valid_days}")) # prints the number of valid days
print(f"Total steps (valid days): {total}")# the total steps for valid days.
print(f"Average: {total // valid_days}") # the average using integer division. 
