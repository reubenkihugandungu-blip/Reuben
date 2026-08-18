# Parsing means reading a raw data structure and extracting the specific values you need.
#  An API response can have dictionaries inside dictionaries inside lists. 
# You navigate it layer by layer using chained bracket access and .get() for safety.

# Navigate nested structure
response = {
    "status": "sucess",
    "user": {
        "id": 42,
        "name": "Kevin Mwangi",
        "location": {
            "city": "Kisumu",
            "country": "Kenya"
        }
},
    "today": {
        "steps": 10800,
        "cold_shower": True,
        "fasting": {
            "protocol": "OMAD",
            "window_hours": 23
        },
        "workout": {
            "completed": True,
            "bench_press_kg": 90,
            "duration_minutes": 55
        }
    }
}

# Navigate layer by layer
name = response["user"]["name"]
city = response["user"]["location"]["city"]
steps = response["today"]["steps"]
protocol = response["today"]["fasting"]["protocol"]
bench = response["today"]["workout"]["bench_press_kg"]

print(f"Name:  {name}")
print(f"City: {city}")
print(f"Steps: {steps}")
print(f"protocol: {protocol}")
print(f"Bench: {bench} kg")
