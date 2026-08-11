# Workout session report

number_of_exercises = 6
sets_per_exercise = 4
reps_per_set = 10
average_weight_per_rep = 60
session_duration_minutes = 45

total_sets = number_of_exercises * sets_per_exercise
total_reps = total_sets * reps_per_set
total_volume_kg = total_reps * average_weight_per_rep
reps_per_minute = total_reps // session_duration_minutes
exceeded_10000_kg = total_volume_kg > 10000

print(" == Workout Session Report ==")
print(f"Total sets: {total_sets}")
print(f"Total reps: {total_reps}")
print(f"Total volume (kg lifted): {total_volume_kg} kg")
print(f"Reps per minute: {reps_per_minute:}") # .2f gives the answer in 2 decimal places.
print(f"Exceeded 10,000 kg: {exceeded_10000_kg}")

# store your values
number_of_exercises = 6
# Add the rest below

# Calculate and print your report