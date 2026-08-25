# The dashboard calls three endpoints. In a script each would be a requests.get() call. 
# Here each returns a hardcoded dict that mirrors an API response exactly.

# endpoint 1 
# GET /v1/members?city=Nairobi: returns a list of members with their today stats.

# endpoint 2
# GET /v1/weekly-summary: returns aggregated step data for the past 7 days across all members.

# endpoint 3
# GET /v1/skills/active: returns the list of active SMP skills being taught this week.

# STEP 1: PREVIEW ALL THREE ENDPOINTS

def fetch_members():
    return [
        {"name": "James Omondi", "steps": 9200, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
        {"name": "Patrick Njiru", "steps": 8100,  "protocol": "OMAD", "sleep": 6.5, "cold_shower": False},
        {"name": "Grace Achieng", "steps": 11000, "protocol": "OMAD", "sleep": 7.0, "cold_shower": True},
        {"name": "Brian Kamau",   "steps": 7400,  "protocol": "2MAD", "sleep": 9.0, "cold_shower": True},
        {"name": "Kevin Mwangi",  "steps": 10800, "protocol": "OMAD", "sleep": 7.5, "cold_shower": True},
    ]

def fetch_weekly_summary():
    return {
        "week": "2024-W47",
        "daily_totals": [54200, 62000, 58400, 71000, 49600, 68000, 65200],
        "days": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
        "member_count": 6
    }

def fetch_active_skills():
    return {
        "week": "2024-W47",
        "skills": [
            {"name": "welding",   "instructor": "Patrick Njiru", "enrolled": 8},
            {"name": "tiling",        "instructor": "James Omondi",  "enrolled": 12},
            {"name": "copywriting",   "instructor": "Sandra Weru",   "enrolled": 15},
            {"name": "phone repair",  "instructor": "Kevin Mwangi",  "enrolled": 10},
            {"name": "beekeeping",    "instructor": "Grace Achieng", "enrolled": 6},
        ]
    }

# preview 
members = fetch_members()
weekly = fetch_weekly_summary()
skills = fetch_active_skills()

print(f"Members endpoint: {len(members)} records")
print(f"Weekly endpoint: {len(weekly['daily_totals'])} days of data")
print(f"Skills enpoint: {len(skills['skills'])} active skills")