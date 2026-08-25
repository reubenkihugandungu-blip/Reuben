# Every business script follows the same four-part pattern.
#  Here is a dairy farm cooperative running the exact same structure: configuration, fetch, process, output.

# FARM SCRIPT: FOUR PARTS APPLIED

import json

# --- Configuration ---
COOPERATIVE = "Githunguri Dairy Cooperative"
MIN_LITRES = 15.0 # falgs farms below this daily target

# --- Fetch ---
def fetch_farm_readings():
    # Simulated readings from morning collection
    return [
        {"farm": "Kamau wa Njoroge", "location": "Githunguri", "litres": 22.5, "cows": 3},
        {"farm": "Wanjiku Farm", "location": "Limuru", "litres": 18.0, "cows": 2},
        {"farm": "Mwangi Dairy",      "location": "Githunguri", "litres": 31.5, "cows": 4},
        {"farm": "Achieng Holdings",  "location": "Thika",      "litres": 11.0, "cows": 2},
        {"farm": "Kariuki Homestead", "location": "Limuru",     "litres": 26.0, "cows": 3},
    ] 

# --- process ---
