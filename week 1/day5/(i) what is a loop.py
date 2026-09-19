# A loop is an instruction that tells Python to repeat a block of code more than once.

# That is it. That is the whole idea.

# Instead of writing the same line ten times, you write it once and tell Python: run this ten times. 
# Python does the repetition for you.

# Here is why this matters. Imagine you want to remind yourself of your daily step goal for five days.
#  Without a loop, you would write this:

print("Step goal: 8,000 steps")
print("Step goal: 8,000 steps")
print("Step goal: 8,000 steps")
print("Step goal: 8,000 steps")
print("Step goal: 8,000 steps")

# Five lines. Fine for 5 days. But what about 30 days? Or a full year of 365 days?
#  You would be typing forever. A loop solves this. You write the instruction once and tell Python
#  how many times to run it:

for day in range(5):
    print("Step goal: 8,000 steps")