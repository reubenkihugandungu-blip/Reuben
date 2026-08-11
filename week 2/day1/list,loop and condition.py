# Combine the loop with a condition to make decisions about each item.

weekly_steps = [9200, 10500, 8800, 11000, 7600, 9400, 10200]
for steps in weekly_steps:
    if steps >= 10000:
        print(steps, "steps - Goal exceeded")
    elif steps >= 8000:
        print(steps, " steps - Goal hit")
    else:
        print(steps, "steps - Below goal")