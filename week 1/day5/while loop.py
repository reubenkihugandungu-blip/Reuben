# while loop says: keep repeating this block of code.
# for as long as this condition is true.
# check the condition before each round, when it is false stop.
# steps += 500  same as: steps = steps + 500

glasses = 0 # sets the starting point. Zero glasses consumed.
# is the condition. P checks this b4 every round. is glasses less than 8? if yes, run the block, if no, stop.
while glasses < 8: 
    glasses = glasses + 1 # it adds one to glasses, also tells the loop when to stop. same as glasses += 1.
    print("Glass", glasses, "done")
