# Parsing ends when you can produce clean, readable output from raw API data.
#  This means extracting, computing, and formatting in one pass.

# parse and summarize
api_response = {
    "week": "2024-W47",
    "members":[
        {"name": "James Omondi", "daily_steps": [9200, 10100, 8800, 11000, 9400, 10200,8600]},
        {"name": "Sandra Weru", "daily_steps": [10500, 9800, 10200, 11500, 9100, 10800, 10000]},
        {"name": "Patrick Njiru", "daily_steps": [8100, 7900, 8500, 9200, 8800, 7600, 9000]},
        {"name": "Grace Achieng", "daily_steps": [11000, 10800, 9900, 12000, 10500, 11200, 10300]},
    ]
}

print(f"Week: {api_response['week']}")
print("-" * 62)
print(f"{'name':<20} {'Avg Steps':>10} {'Days 10k+':>15} {'Max Steps':>15}")
print("-" * 62)

for member in api_response["members"]:
    steps = member["daily_steps"]
    avg = round(sum(steps) / len(steps))
    days_hit = sum(1 for s in steps if s >= 10000)
    max_steps = max(steps)
    print(f"{member['name']:<20} {avg:>10} {days_hit:>10} {max_steps:>15}")  

# Try this:
# Add a column to the output that shows the single best day for each member. Use max(steps).