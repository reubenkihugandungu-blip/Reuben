# Use the (in) keyword to check whether a specific value is in a list.
#  It gives you True or False.

skills_learned = ["welding", "tiling", "copywriting", "phone repair",]

if "welding" in skills_learned:
    print("welding is in the list.")
if "beekeeping" not in skills_learned:
    print("Beekeeping not found. Add it to the list.")

# Tip: not in checks for the absence of a value. 
# Both in and not in work inside if statements exactly like any other condition.