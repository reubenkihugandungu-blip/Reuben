# A ride-hailing app returns a driver's completed trips for the day.
#  Loop through the trips, count them, add up the fares, and find the highest-paying trip

data = {
    "driver": "Kamau Njoroge",
    "date": "2026-08-13",
    "trips": [
        {"route": "Westlands to CBD",     "fare_kes": 560},
        {"route": "CBD to South B",       "fare_kes": 420},
        {"route": "South B to Karen",     "fare_kes": 980},
        {"route": "Karen to Westlands",   "fare_kes": 720},
        {"route": "Westlands to Airport", "fare_kes": 740},
    ]
}

total_trips = 0
total_earned = 0
highest_trip = ""
highest_fare = 0

for trip in data["trips"]:
    total_trips += 1
    fare = trip["fare_kes"]
    total_earned += fare

    if fare > highest_fare:
        highest_fare = fare
        highest_trip = trip["route"]

print(f"Total trips: {total_trips}")
print(f"Total earned: KES {total_earned}")
print(f"Highest trip: {highest_trip} | KES {highest_fare}")



