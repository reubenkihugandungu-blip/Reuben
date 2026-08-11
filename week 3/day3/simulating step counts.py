import random

print("Simulated step counts for this week:")
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
for day in days: # starts a loop that goes through each item in the days list, setting day to "mon then "Tue
    steps = random.randint(5000, 13000) # generates a random integer between 5000 & 13000 inclusive and stores it in the variable steps 
    status = "OK" if steps >= 8000 else "low"
    print(f" {day}: {steps} steps ({status})")