# putting an if statement inside another if statement.
# it lets you check a second condition only if the first one has passed.

workout_done = True
weight_lifted_kg = 6000
personal_best_kg = 5000

if workout_done:
    print("Workout logged.")
    if weight_lifted_kg > personal_best_kg:
        print("New personal best! Previous:", personal_best_kg, "kg")
    else:
        print("Solid session. No new record today.")
else:
    print("Rest day. No workout logged.")
# 