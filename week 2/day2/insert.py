# insert() adds an item at a specific position. use it when position matters.
#  Everything after it shifts one place to the right.

skills = ["welding", "tiling", "upholstery"]
print("Before:", skills)

skills.insert(1, "copywriting") # insert "copywriting" at postion 1 (second slot)
print("After:", skills)

skills.insert(2, "painting")
print("After:", skills)
