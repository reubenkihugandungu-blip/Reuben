# Instead of importing the whole module, you can import just the functions you need using from module import function.
#  Then you call the function directly without the module prefix.
# Use import math when you need many things from a module.
#  Use from math import sqrt when you only need one or two specific functions. 
# Both approaches are common in Python code.

from math import sqrt, floor, ceil
from random import randint, choice

# No need to write math.sqrt() or random.randint()
print("Square root of 225:", sqrt(225))
print("Floor of 9.7:", floor(9.7))

protocols = ["OMAD", "2MAD", "Autophagy Marathon"]
print("Today's protocol:", choice(protocols))
print("Random step bonus:", randint(100, 500), "steps")