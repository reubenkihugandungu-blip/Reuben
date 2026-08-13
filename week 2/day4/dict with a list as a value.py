# A dictionary value can itself be a list.
#  This is useful when one key needs to hold multiple items,
#  like all the steps from a full week.

weekly_summary = {
    "week": 1,
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "protocols": ["OMAD", "2MAD", "OMAD", "Autophagy Marathon", "OMAD", "2MAD", "OMAD"],
    "cold_showers_completed": 6
}

print("week", weekly_summary["week"])
print("Total days tracked:", len(weekly_summary["steps"]))
print("First day steps:", weekly_summary["steps"][0])
print("Average steps:", sum(weekly_summary["steps"]) / len(weekly_summary["steps"]))
# sum() adds up all numbers in a list. 
# Combine it with len() to calculate averages without writing a loop.