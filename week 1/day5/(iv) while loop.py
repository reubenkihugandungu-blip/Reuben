# while loop says: keep repeating this block of code.
# for as long as this condition is true.
# check the condition before each round, when it is false stop.

# steps += 500  same as: steps = steps + 500

glasses = 0 # sets the starting point. Zero glasses consumed.

# is the condition. P checks this b4 every round. is glasses less than 8? 
# if yes, run the block, if no, stop.
# it adds one to glasses, also tells the loop when to stop.same as glasses += 1

while glasses < 8: 
    glasses = glasses + 1  
    print("Glass", glasses, "done")

# Always make sure the loop can stop. In this example, glasses = glasses + 1 is what eventually makes 
# the condition false. If you removed that line, glasses would stay at 0 forever,
#  the condition would always be true, and the loop would run forever.
