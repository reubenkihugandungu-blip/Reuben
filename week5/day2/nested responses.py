# Parsing means reading a raw data structure and extracting the specific values you need.
#  An API response can have dictionaries inside dictionaries inside lists. 
# You navigate it layer by layer using chained bracket access and .get() for safety.

# Navigate nested structure
response = {
    "status": "success",
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

# Navigate layer by layer👉 by first storing dict items in variables
name = response["user"]["name"]
city = response["user"]["location"]["city"]
steps = response["today"]["steps"]
protocol = response["today"]["fasting"]["protocol"]
bench = response["today"]["workout"]["bench_press_kg"]# response[today] gets the today dict,[workout] gets the workout dict inside today, [bench_press_kg] gets the value 90 from the bench_press_kg key

print(f"Name:  {name}")
print(f"City: {city}")
print(f"Steps: {steps}")
print(f"protocol: {protocol}")
print(f"Bench: {bench} kg")
