

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD"},
    {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
    {"day": "Thursday", "steps": 11000, "protocol": "Autophagy Marthon"},
    {"day": "Friday", "steps": 7600, "protocol": "OMAD"},
]
week_log[0]["cold_shower"] = True
week_log[1]["cold_shower"] = False
week_log[2]["cold_shower"] = False
week_log[3]["cold_shower"] = True
week_log[4]["cold_shower"] = True
print("After adding cold shower", week_log)

for log in week_log:
    status = "Done" if log["cold_shower"] == True else "Cold shower skipped"
    print(log["day"], log["cold_shower"], status)
#  