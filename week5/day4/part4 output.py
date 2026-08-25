# The output stage prints the report, saves it to a file, or sends it somewhere.
#  Here it does both: prints a formatted report and saves results as JSON.

# OUTPUT FUNCTION
import json

def print_report(summary, city="Nairobi"):
    print("=" * 48)
    print(f" SMP MEMBER REPORT: {city.upper()}")
    print("=" * 48)
    print(f" Total members: {summary['total_members']}")
    print(f" Hit step goal: {summary['goal_met_count']}")
    print(f" Missed goal: {summary['goal_missed_count']}")
    print(f" Average steps: {summary['average_steps']:,}")
    print(f" Top performer: {summary['top_performer']} ({summary['top_steps']:,})")
    print("-" * 48)
    print(" Members who hit goal:")
    for name in summary["goal_met"]:
        print(f" {name}")
        print("=" * 48)

summary = {
    "total_members": 5,
    "goal_met_count": 3,
    "goal_missed_count": 2,
    "average_steps": 9780,
    "top_performer": "Grace Achieng",
    "top_steps": 11000,
    "goal_met": ["Sandra Weru", "Grace Achieng", "Kevin Mwangi"]
}

print_report(summary, city="Nairobi")

# Save to JSON
output = json.dumps(summary, indent=2)
print("\nJSON output saved:")
print(output)
