# Boolean filtering selects rows where a condition is True. You write a condition that compares a column to a value. 
# Pandas evaluates it for every row and returns only the matching ones. 
# The result is a new DataFrame, not a modification of the original.

# EXAMPLE
# Think of sorting tiles on a workbench.
# You have 100 tiles laid out. You pick up only the ones that are uncracked and 30x30cm. 
# You do not change the tiles. You just choose which ones to work with.
#  Boolean filtering works the same way: the original data stays untouched, 
# and you get back only the rows that pass the condition.

import pandas as pd

df = pd.DataFrame({ # Creates a data frame named df
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"], # this creates the day column it stores the name of the days
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
})

# Days where step goal was hit
#👇this is the main boolean filter, df['steps'] selects the steps column
# >= 10000 compares each value to 10000
# that creates a True/False result for every row
# df[...] keeps only the rows where the condition is True
# So goal_days becomes only the rows where steps were at least 10,000
goal_days = df[df["steps"] >= 10000]
print("Days with 10k+ steps:")
print(goal_days[["day", "steps", "protocol"]].to_string())

print()
# Days with less than 7.5 hours sleep
low_sleep = df[df["sleep_hr"] < 7.5]# Another boolean filter
print("Days with under 7.5 hours sleep:")
print(low_sleep[["day", "sleep_hr"]].to_string())

# Boolean filtering means:
# check a condition for each row
# keep only rows where the condition is True
# ignore the rest