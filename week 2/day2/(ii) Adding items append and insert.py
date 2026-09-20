# append() adds one item to the end of the list.
#  This is the most common way to grow a list.

skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)

skills.append("phone repair")
print("After:", skills)

skills.append("graphic design")
print("Final:", skills)
print()
print()

# insert() adds an item at a specific position. Everything after it shifts one place to the right.

skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)

# Insert "copywriting" at position 1 (second slot)

skills.insert(1, "copywriting")
print("After:", skills)

# Tip: Use append() when you want to add to the end. Use insert() only when the position matters.