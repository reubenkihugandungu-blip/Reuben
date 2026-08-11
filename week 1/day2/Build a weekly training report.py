# storing calculations in variables
bench_press_sets = 4
reps_per_set = 15
weight_per_rep_kg = 40

total_reps = bench_press_sets * reps_per_set
total_volume_kg = total_reps * weight_per_rep_kg
reps_per_minute = total_reps // 6 # assume 6 minutes of work time


print("=== BENCH PRESS SESSION ===")
print(f"sets: {bench_press_sets}")
print(f"Reps per set: {reps_per_set}")
print(f"Total reps: {total_reps}")
print("Weight per rep:",weight_per_rep_kg) # using comma to print
print(f"Total volume lifted: {total_volume_kg} kg")
print(f"Reps per minute: {reps_per_minute}")