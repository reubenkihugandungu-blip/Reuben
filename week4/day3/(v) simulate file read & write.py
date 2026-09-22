import json

# simulate writing
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.5
}
json_string = json.dumps(daily_log, indent=2)
print("Saved JSON:")
print(json_string)

# simulate reading it back
loaded_data = json.loads(json_string)
print("\nRead back as python dict:")
for key, value in loaded_data.items():
    print(f" {key}: {value}")