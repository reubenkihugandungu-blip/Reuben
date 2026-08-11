# You can loop through a dictionary in three ways: 
# keys only, values only, or both at the same time.
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}
# loop through keys and values together
for key, value in daily_log.items():
    print(key, ":", value)