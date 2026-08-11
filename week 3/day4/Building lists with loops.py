# standard loop approach
#  Suppose you have a list of step counts for the week and you want a new list that contains only
#  the days where you hit 8,000 steps, The standard way uses a loop.

weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600] # Creates a list called weekly steps

goal_days = [] # creates an empty list called goal_days to store step counts that meet the goal
for steps in weekly_steps:
    if steps >= 8000:
        goal_days.append(steps)# if the condition is true adds that steps value to the goal_days list.

print(goal_days) # prints the list of step counts that reached or exceeded 8000.