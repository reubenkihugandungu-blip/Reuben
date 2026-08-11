# You can also use .get("key") to access a value safely. 
# If the key does not exist, it returns None instead of an error: daily_log.get("steps")
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD",
    "sleep_hours": 7.5
}
print("Steps today:", daily_log["steps"])
print("Protocol:", daily_log["fasting_protocol"])
print("Cold shower:", daily_log["cold_shower"])

