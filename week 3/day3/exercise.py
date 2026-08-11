# Write a function called generate_week() that uses random to simulate a week of step counts 
# (7 days, each between 6000 and 12000 steps).
#  The function should print each day's count, calculate 

import random
import math

def generate_week():
    days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
    total = 0
    goal_days = 0

    for day in days:
        steps = random.randint(6000, 12000)
        total += steps
        if steps >= 8000:
            goal_days += 1
        print(f" {day}: {steps} steps")

    avg = math.floor(total / 7)
    print(f"\nAverage steps: {avg}")
    print(f"Days on goal : {goal_days}/7")

generate_week()