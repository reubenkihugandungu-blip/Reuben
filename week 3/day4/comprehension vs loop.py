#Use comprehension when you are building a new list from an existing one with a simple transformation or filter.
#Use a regular loop when the logic is complex, when you need to do multiple things per item, 
#or when readability would suffer.

# Build a status list
weekly_steps = [9200, 7500, 10500, 8800, 6900, 11000, 9600]

# Build a list of status strings for each day
statuses = ["Goal hit" if s >= 8000 else "Below goal" for s in weekly_steps]

# enumerate(statuses) loops over the statuses list and returns each item together with its index
# i gets the current index(0,1,2,3...)
# status gets the current element from statuses("goal hit" or "Below goal")
# Below line means for each status in statuses also keep track of its position
# in the list so you can print Day {i+1} with the matching step count.

for i, status in enumerate (statuses):
    print(f"Day {i+1}: {weekly_steps[i]} steps - {status}")


