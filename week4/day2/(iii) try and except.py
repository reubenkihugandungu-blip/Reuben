# Wrap code that might fail in a try block. Put your response in the except block. 
# If the try block fails, Python jumps to except instead of crashing.

steps_data = ["9200", "7500", "ten thousand", "8800", "6900"]

for item in steps_data: # starts a loop that goes through each value in the list steps_data. each element is assigned to the variable item on each iteration.
    try:# begins a try block to run code that might raise an error. If an exception occurs inside this block, python will skip to the matching except
        steps = int(item) # tries to convert the current item from a string to an integer, if item is not a valid numeric string this raises ValueError
        if steps >= 8000:# checks whether the converted integer steps is atleast 8000
            print(steps, "- Goal hit")
        else:
            print(steps, "- Below goal")
    except ValueError:# this block runs only if converting item to int failed with a value error
        print(f"'{item}' is not a valid number. Skipping.")# prints a message saying the current item is invalid and wil be skipped.


# 