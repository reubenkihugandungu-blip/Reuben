# A ride-hailing app returns a driver's completed trips for the day.
# Loop through the trips, count them, add up the fares, and find the highest-paying trip

# Create a dictionary containing the driver's name, the date, and a list of trip records
data = {
    "driver": "Kamau Njoroge",   # Driver's name
    "date": "2026-08-13",       # Date of the trips
    "trips": [                   # List of trip dictionaries
        {"route": "Westlands to CBD",     "fare_kes": 560},  # Trip 1: fare = 560
        {"route": "CBD to South B",       "fare_kes": 420},  # Trip 2: fare = 420
        {"route": "South B to Karen",     "fare_kes": 980},  # Trip 3: fare = 980
        {"route": "Karen to Westlands",   "fare_kes": 720},  # Trip 4: fare = 720
        {"route": "Westlands to Airport", "fare_kes": 740},  # Trip 5: fare = 740
    ]
}

# Start counting trips and earnings at zero
total_trips = 0       # Number of trips completed
total_earned = 0      # Total money earned so far
highest_trip = ""    # Route with the highest fare, no trip made yet thats why there is ""
highest_fare = 0      # Highest fare seen so far

# Loop through each trip in the trips list
for trip in data["trips"]:  # loops through every item in the trips list; each item is one trip dict
    total_trips += 1                  # Add 1 for each trip visited
    fare = trip["fare_kes"]          # Get the fare for this trip
    total_earned += fare             # Add this trip's fare to total earnings

    # If this trip's fare is bigger than the current highest fare, update the record
    if fare > highest_fare:  # checks whether this trip's fare is bigger than the best fare seen so far
        highest_fare = fare          # Save the new highest fare
        highest_trip = trip["route"] # Save the route linked to that fare

# Print all the results after the loop finishes
print(f"Total trips: {total_trips}")
print(f"Total earned: KES {total_earned}")
print(f"Highest trip: {highest_trip} | KES {highest_fare}")

