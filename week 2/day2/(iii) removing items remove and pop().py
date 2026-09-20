# remove() deletes the first item in the list that matches the value you give it.
# remove finds by value.

habits = ["8 glasses water", "cold shower", "OMAD fast", "workout", "cold shower"]
print("Before:", habits)

habits.remove("cold shower") # Removes only the first one
print("After:", habits)
print()

# pop() removes an item by its index position and gives you back the item it removed. 
# With no index, it removes the last item.

weekly_steps = [9200, 10500, 8800, 11000, 7600]
print("Before:", weekly_steps)

removed = weekly_steps.pop() # Removes last item. unnamed
print("Removed:", removed)
print("After:", weekly_steps)

removed2 = weekly_steps.pop(1) # Removes item at index 1
print("Removed:", removed2)
print("After:", weekly_steps) 


