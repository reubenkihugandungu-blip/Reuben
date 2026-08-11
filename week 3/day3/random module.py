# random generates random numbers and makes random choices. 
# Useful for simulations, shuffling, and selecting random items.

import random

# Random integer between 1 and 10 (inclusive)
print("Random number:", random.randint(1, 10))

# Random float between 0 and 1
print("Random float:", random.random())

# Random choice from a list
skills = ["welding", "tiling", "upholstery", "phone repair", "copywritting"]
print("Today'skill focus:", random.choice(skills))

# shuffle a list
random.shuffle(skills)
print("Shuffled:", skills)
    