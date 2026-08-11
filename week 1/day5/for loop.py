# loop an instruction that tells python to repeat a block of code more then once
# for tells python we are starting a loop and repeats something a set of number of times.
# day variable to track which round of the loop we are on, you can name it anything you want
# in range(5) generates sequence of 5 numbers
# : marks the end of the loop
# 'for variable in range (number):'
# print(...) indented block. the code that runs on every loop.

for day in range(5):
    print("Step goal: 8,000 steps")

for day in range(1, 5):
    print(f"Day {day}: Steps 8000")

for day in range(5):
    print("Day:", day,"- Step goal: 8,000 steps")
    