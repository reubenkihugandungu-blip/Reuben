week_summary = {
    "week": 1,
    "steps": [9000, 7500, 9700, 10500, 11000], 
    "protocol": ["OMAD", "2MAD", "AUTOPHAGY MARATHON", "OMAD", "2MAD"],
    "cold_shower_completed": 6
}

print("Week:", week_summary['week'])
print("Average steps:", sum(week_summary["steps"]) / len(week_summary["steps"]))