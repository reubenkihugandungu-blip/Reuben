# Put all four parts together. Each function has one job. The main block calls them in sequence.
import json, os

# --- Configuration ---
BASE_URL =  "https://api.smptracker.com/v1" # stores the API base URl. It is currently unused
API_key = os.environ.get("SMP_API_KEY", "demo_key_123")# reads smp api key from the environment. if missing, uses demo key 123
TARGET_CITY = "Mombasa"
STEP_GOAL = 10000 # sets the step goal to 10,000

# --- Fetch ---
def fetch_members(city, limit=50):# defines fetch_members accepting a city and optional limit of 50
    # Simulated API response
    all_members = [
        {"name": "James Omondi", "city": "Nairobi", "steps": 9200, "protocol": "OMAD", "sleep": 7.5},
        {"name": "Sandra Weru", "city": "Nairobi", "steps": 10500,"protocol": "2MAD", "sleep":8.0},
        {"name": "Patrick Njiru", "city": "Mombasa",  "steps": 8100,  "protocol": "OMAD", "sleep": 6.5},
        {"name": "Grace Achieng", "city": "Nairobi",  "steps": 11000, "protocol": "OMAD", "sleep": 7.0},
        {"name": "Brian Kamau",   "city": "Kisumu",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0},
        {"name": "Kevin Mwangi",  "city": "Nairobi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5},
        {"name": "Andreas Korir", "city": "Mombasa", "steps": 11900, "protocol": "2MAD", "sleep": 7.5},
    ]
    return [m for m in all_members if m["city"] == city][:limit]# filters members whose city matches city, then limits the results to limit

# --- Process ---
def process_members(members, step_goal):# defines process members accepting members and a step goal
    goal_met = [m for m in members if m["steps"] >= step_goal]# creates goal met containing members whose steps are greater than or equal to the goal
    avg_steps = round(sum(m["steps"] for m in members) / len(members), 1) if members else 0
    avg_sleep = round(sum(m["sleep"] for m in members) / len(members), 1) if members else 0
    top = max(members, key=lambda m: m["steps"]) if members else {}# finds the member with the highest number of steps. if there are no members, uses an empty dict
    return{ # begins returning a summary dictionary
        "total": len(members), # stores the total number of members
        "goal_met": len(goal_met),
        "avg_steps": avg_steps,
        "avg_sleep": avg_sleep,
        "top_name": top.get("name", "N/A"),
        "top_steps": top.get("steps", 0),
        "achievers": [m["name"] for m in goal_met]
    }

# --- Output ---
def print_report(city, summary):
    print(f"\n{'='*48}")# prints a blank line and 48 equal signs
    print(f" SMP DAILY REPORT: {city.upper()}")# prints the report title converting the city to uppercase
    print(f"{'='*48}")
    print(f" Members: {summary['total']}")# prints the total number of members
    print(f" Hit {STEP_GOAL:,} steps: {summary['goal_met']}")
    print(f" Avg steps: {summary['avg_steps']:,}")
    print(f" Avg sleep: {summary['avg_sleep']} hrs")
    print(f" Top: {summary['top_name']} ({summary['top_steps']:,})")
    print(f"\n Achievers: {','.join(summary['achievers'])}")
    print(f"{'='*48}\n")

# --- Main ---
members = fetch_members(TARGET_CITY)# calls fetch_members("Mombasa") and stores the result in members
summary = process_members(members, STEP_GOAL)# processes those members and stores the summary in summary
print_report(TARGET_CITY, summary)# prints the report using the target city and summary.avg_steps = round(sum(m["steps"] for m in members) / len(members), 1) if members else 0


