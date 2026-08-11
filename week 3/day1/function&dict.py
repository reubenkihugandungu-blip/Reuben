#  Functions work with any data type, including dictionaries and lists.
#  Pass the full structure in and work with it inside the function.

def print_client(client):
    print(f"Name  : {client['name']}")# f string that reads the name key from the client dictionary
    print(f"Goal  : {client['goal']}")
    print(f"Bench : {client['bench_press_kg']} kg")
    print(f"Sessions : {client['weekly_sessions']} per week")
    print()

clients = [
    {"name": "James", "goal": "fat loss", "bench_press_kg": 80, "weekly_sessions": 4},
    {"name": "Sandra", "goal": "endurance", "bench_press_kg": 50, "weekly_sessions": 3},
    {"name": "Mwangi", "goal": "muscle gain", "bench_press_kg": 100, "weekly_sessions": 5},
]
# Call the function for each client
# starts a loop that goes through each client in the clients list and calls the print_client function for each one
for client in clients:
    print_client(client)