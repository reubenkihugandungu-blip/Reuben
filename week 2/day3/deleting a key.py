# Use del to remove a key and its value from a dictionary.
daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "fasting_protocol": "OMAD",
    "junk_entry": "delete me"
}
del daily_log["junk_entry"]
print(daily_log)
