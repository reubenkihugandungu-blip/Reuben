# Use in to check whether a key exists in a dictionary before you try to access it.

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "fasting_protocol": "OMAD"
}
if "steps" in daily_log:
    print("Steps recorded:", daily_log["steps"])
if "sleep_hours" not in daily_log:
    print("Sleep hours not logged yet.")
