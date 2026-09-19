steps = [8200, 5100, 11300, 6800, 9400, 4200, 10100] # this creates a list of 7 daily step counts for the week.

print("==Daily step review==") # this prints a heading so the output is easier to read.
for day, count in enumerate(steps, start=1): # for loop over the list, enumerate gives both the position and value.
    hit_target = count >= 8000                # start=1 makes the first day number be 1 instead of 0, 
    status = "hit" if hit_target else "missed" # 
    print(f"Day {day}: {count} steps - {status} the 8000-step target") # this prints each days number and whether it reached the target.

total_steps = 0 # this sets the total of valid step counts to 0 before adding values.
valid_days = 0 # counts how many days are included in the average calculation.

for count in steps: # starts another loop to process each daily count.
    if count < 5000: # checks if the day is below 5000 steps.
        continue # if the day is below 5000, steps loop skips it. means it will not added to the average.
    valid_days += 1 # if the day is not skipped this increases the count of valid days by 1.
    total_steps += count # this adds the day's step count to the total

average_steps = total_steps / valid_days if valid_days > 0 else 0
# calculates average, divides if there is at least one valid day.uses 0 to avoid division by zero
streak = 0 # starts the consecutive streak counter at 0
index = 0 # starts the loop at the first item in the list
while index < len(steps) and steps[index] >= 8000: # starts the loop it keeps going while current day reaches 8000 steps and there are still days left
    streak += 1 # each time the condition is true the streak increases by 1
    index += 1 # this moves to the next day in the list

print("\nWeekly summary:") # prints the heading
print(f"Total valid days: {valid_days}") # this prints how many days were used in the average.
print(f"Average steps: {average_steps:.2f}") # prints the average with2 decimal places
print(f"Consecutive streak count: {streak}")# this p how many days in a row from the start reached the target before the first miss.