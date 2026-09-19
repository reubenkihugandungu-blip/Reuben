# The first type of loop is called a for loop. You use it when you know exactly how many times you 
# want to repeat something.

# The structure looks like this:

# for variable in range(number):
    # code to repeat goes here, indented

for day in range(5):
    print("Step goal: 8,000 steps")

for day in range(1, 5):
    print(f"Day {day}: Steps 8000")

for day in range(5):
    print("Day:", day,"- Step goal: 8,000 steps")

# for
# This keyword tells Python: we are starting a loop.

# day
# This is a variable that Python will use to track which round of the loop we are on.
#  You can name it anything. We called it day because we are thinking of each round as one day.

## in range(5)
# range(5) generates a sequence of 5 numbers. Python will go through each one.
#  The loop runs once for each number in that sequence, giving us 5 total runs: 5 days.

## :
# The colon marks the end of the loop header. Everything indented below it is what gets repeated.

## print(...)
# This is the indented block. It is the code that runs on every loop. The indentation is not optional.
#  Python uses it to know what belongs inside the loop and what does not.