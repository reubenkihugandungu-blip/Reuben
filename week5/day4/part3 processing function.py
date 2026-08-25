# The processing function takes raw data and returns something useful: computed stats, filtered records, 
# or a restructured format. It does not fetch or print.

# Processing Function
def process_members(members, step_goal=10000):
    """
    Takes a list of raw member records.
    Returns a summary dict with stats and categorized members.
    """
    if not members:
        return {"error": "No members to process"}

    total = len(members)
    goal_met = [m for m in members if m["steps"] >= step_goal]
    goal_missed = [m for m in members if m["steps"] < step_goal]
    avg_steps = round(sum(m["steps"] for m in members) / total)
    top_performer = max(members, key=lambda m:["steps"])

    return {
        "total_members": total,
        "goal_met_count": len(goal_met),
        "goal_missed_count": len(goal_missed),
        "average_steps": avg_steps,
        "top_performer": top_performer["name"],
        "top_steps": top_performer["steps"],
        "goal_met": [m["name"] for m in goal_met],
    }

# Test with sample data
raw_members = [
    {"name": "James Omondi", "steps": 9200, "protocol": "OMAD"},
    {"name": "Sandra Weru", "steps": 10500, "protocol": "2MAD"},
    {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD"},
    {"name": "Brian Kamau", "steps": 7400, "protocol": "2MAD"},
    {"name": "Kevin Mwangi", "steps": 10800, "protocol": "OMAD"}, 
]

summary = process_members(raw_members, step_goal=10000)
print("Processed summary:")
for key, value in summary.items():
    print(f" {key}: {value}")