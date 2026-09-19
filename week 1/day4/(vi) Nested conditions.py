# putting an if statement inside another if statement. This is called nesting
# it lets you check a second condition only if the first one has passed.

# NESTED CONDITIONS: Training session check

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

# The inner if only runs when workout_done is True. If it is False, Python goes straight to the outer
#  else and never even looks at the inner block.