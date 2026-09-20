# To add a new key-value pair, assign a value to a new key. 
# To update an existing one, assign a new value to an existing key. Python handles both the same way.

daily_log = {
    "steps": 9200,
    "water_glasses": 8,
    "cold_shower": True,
    "fasting_protocol": "OMAD"
}

# add a new key

daily_log["pages_read"] = 30
print("After adding pages:", daily_log)

# Update an existing key
daily_log["steps"] = 10400
print("After updating steps:", daily_log) 
