# Many API responses have nested structure where a key's value is itself a dictionary. 
# Chain brackets to go deeper.
# Nested API Data
data = {
    "user": {
        "id": 1,
        "name": "Sandra Weru",
        "city": "Nairobi"
    },
    "metrics": {
        "steps": 10500,
        "sleep_hours": 8.0,
        "bench_press_kg": 80
    },
    "skills": ["welding", "tiling", "copywriting"]
}

print(data["user"]["name"])
print(data["user"]['city'])
print(data["metrics"]["steps"])
print(data["metrics"]["bench_press_kg"], "kg bench press")
print("Skills:", data["skills"])
print("First skill:", data["skills"][0])