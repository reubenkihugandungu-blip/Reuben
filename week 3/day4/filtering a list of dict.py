# Comprehensions also work on lists of dictionaries. 
# This is where they become very useful in data work.

clients = [
    {"name": "James", "goal": "fat loss", "sessions": 4},
    {"name": "Mwangi", "goal": "muscle gain", "sessions": 5},
    {"name": "Sandra", "goal": "endurance", "sessions": 3 },
    {"name": "Patrick", "goal": "fat loss-", "sessions": 4},
    {"name": "Grace", "goal": "fat loss", "sessions": 3},
]

# Get names of all fat loss clients
fat_loss_names = [c["name"] for c in clients if c["goal"] == "fat loss"]
print("Fat loss clients:", fat_loss_names)
# Get all clients with 4 or more sessions per week
active_clients = [c for c in clients if c["sessions"] >= 4]
print("Active clients:", [c["name"] for c in active_clients])