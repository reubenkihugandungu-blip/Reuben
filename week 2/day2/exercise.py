# Start with this list of step counts: [8800, 6500, 11000, 9200, 7300]. 
# Do the following steps in order: 
# add 10500 to the end, remove 6500, sort the list from highest to lowest, 
# then print the final list and print how many days exceeded 9000 steps.

steps = [8800, 6500, 11000, 9200, 7300]

steps.append(10500)
steps.remove(6500)
steps.sort(reverse=True) # sorts the list in descending order.

print("Final list:", steps) # prints final lists followedby steps.

high_days = 0 # creates  a counter variable high_days initialized to 0.
for s in steps: # starts a loop that goes through each value in steps.
    if s >= 9000: # checks whether the current step count is 9000 or more.
        high_days += 1 # if the check is true, increases high days by 1.
print("Days over 9000 steps:", high_days)
