# APIs sometimes return null in JSON, which becomes None in Python. 
# If you try to access a key on None, you get a TypeError. Check for None before going deeper.
# Handle None values

users = [
    {"name": "James Omondi", "workout": {"bench_press_kg": 80, "duration_minutes": 45}},
    {"name": "Sandra Weru", "workout": None}, # did not train today
    {"name": "Grace Achieng", "workout": {"bench_press_kg": 60, "duration_minutes": 40}},
]

for user in users:
    name = user["name"]
    workout = user["workout"]
    if workout is None:
        print(f"{name}: rest day")
    else:# if workout is NOT none(meaning its a dict with data, execute the following block)
        bench = workout.get("bench_press_kg", "not recorded")
        # ☝️safely get the "bench_press_kg" key from the workout dict. 
        # if the key doesnt exist use the default value "not recorded" instead of crashing
        mins = workout.get("duration_minutes", "?")# safely get the "duration_minutes" key from the workout dict. if missing default to "?"
        print(f"{name}: bench={bench}kg, duration={mins}min ")

#👉 key concept: The code safely handles cases where workout is None (using is None check) 
# and cases where specific keys might be missing (using .get() with defaults).
#  This prevents crashes when data is incomplete or missing.