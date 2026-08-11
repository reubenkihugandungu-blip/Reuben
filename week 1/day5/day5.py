daily_steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100] #creates a list named daily steps
minimum_for_average = 5000 # sets threshold of 5000 steps. days above this count to be included in the average calculation.
target = 8000 # sets the daily goal to 8000 steps for determining hits vs misses.

print("Daily step report:") # Prints header text.
for day_index, steps in enumerate(daily_steps, start=1): # loops through dailysteps giving daily index values starting at 1 and steps for each day
    hit_target = "HIT" if steps >= target else "MISS"
    print(f"Day {day_index}: {steps} steps - {hit_target}") # prints the day number, step count and whether it was hit

# Calculate weekly average only for valid days above the minimum threshold.
total = 0 # initializes a running total valid days' steps
valid_days = 0 # initializes a counter for how many days qualify as valid
for steps in daily_steps:# starts a loop over each day's step count
    if steps < minimum_for_average: # checks if the current day's steps are below valid minimum
        continue # Skips this day and moves to the next loop iteration if it is below threshold
    total += steps # Adds the current day's steps if it is valid
    valid_days += 1 # increments the count of valid days.

average = total // valid_days if valid_days else 0 # calculates average when atleast one day is valid. otherwise sets the average to 0 to avoid division by zero

# Count the consecutive target streak from the start.
streak = 0
index = 0 # starts an index at 0 to examine days from the beginning of the list.
while index < len(daily_steps) and daily_steps[index] >= target: # repeats   while the index is in range and the current day's steps are at or above the target
    streak += 1 # increments the streak count for each consecutive qualifying day
    index += 1 # moves to the next day.

print("\nWeekly summary:") # prints a blank line and the summary header
print(f"Valid days: {valid_days}") # p how many days were included in the average calculation.
print(f"Average steps: {average}") # p the computed average step count for valid days.
print(f"Consecutive target streak from start: {streak}")# p how many days in row from the first day met the target.
