# a dictionary tracking an SMP client's profile for a personal training session:
client = {
    "name": "James",
    "weight_kg": 84.5,
    "goal": "fat loss",
    "fasting_protocol": "2MAD",
    "bench_press_kg": 80,
    "weekly_sessions": 4

}
print("Client profile:")
for key, value in client.items():
    print(f" {key}: {value}")

    print()

if client["bench_press_kg"] >= 80:
    print("Bench press goal reached.")
