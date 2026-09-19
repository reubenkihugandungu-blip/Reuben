# Starting from 1 instead of 0
# If you want to count from 1 to 5, you give range() two numbers: where to start, and where to stop.
#  Python stops just before the second number:

# Count from 1 to 7: one week of discipline

for day in range(1, 8):
    print("Day", day, "- Step goal: 8,000 steps")

# Print the first 10 even numbers using a loop

for i in range(1, 21): # means repeat for each number from 1 up to 20
    if i % 2 == 0: # checks whether the number is even
        print(i) # shows the number if it is even