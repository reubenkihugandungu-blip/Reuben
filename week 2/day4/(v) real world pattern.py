# This pattern of a list of dictionaries is exactly what you get
#  when you call an API or read from a database.
#  Here is what an SMP client roster looks like: 

clients = [
    {"name": "James", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 80},
    {"name": "Mwangi", "goal": "muscle gain", "weekly_sessions": 5, "bench_press_kg": 100},
    {"name": "Sandra", "goal": "endurance", "weekly_sessions": 3, "bench_press_kg": 50},
    {"name": "Patrick", "goal": "fat loss", "weekly_sessions": 4, "bench_press_kg": 70},
]
print("Fat loss clients:")
for client in clients:
    if client["goal"] == "fat loss":
        print("-", client["name"], "| Bench:", client["bench_press_kg"], "kg | Sessions:", client["weekly_sessions"])
        
