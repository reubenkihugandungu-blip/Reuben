# Create a list called week_steps with 7 numbers representing step counts for each day of the week. 
# Write a loop that prints each count and says whether you hit 8,000 steps.
#  After the loop, print the total number of days tracked using len().

week_steps = [9200, 7400, 10500, 8800, 6900, 11000, 9600]

for steps in week_steps:
    if steps >= 8000:
        print(steps, "- Goal hit")
    else:
        print(steps, "- Below goal")

print("Days tracked:", len(week_steps))
