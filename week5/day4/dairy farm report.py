# Every business script follows the same four-part pattern.
#  Here is a dairy farm cooperative running the exact same structure: configuration, fetch, process, output.

# FARM SCRIPT: FOUR PARTS APPLIED

import json

# --- Configuration ---
COOPERATIVE = "Githunguri Dairy Cooperative"
MIN_LITRES = 10.0 # flags farms below this daily target, try change it to 15

# --- Fetch ---
def fetch_farm_readings():
    # Simulated readings from morning collection
    return [
        {"farm": "Kamau wa Njoroge",  "location": "Githunguri", "litres": 22.5, "cows": 3},
        {"farm": "Wanjiku Farm",      "location": "Limuru",      "litres": 18.0, "cows": 2},
        {"farm": "Mwangi Dairy",      "location": "Githunguri", "litres": 31.5, "cows": 4},
        {"farm": "Achieng Holdings",  "location": "Thika",      "litres": 11.0, "cows": 2},
        {"farm": "Kariuki Homestead", "location": "Limuru",     "litres": 26.0, "cows": 3},
        {"farm": "Winfred Dairyland", "location": "Nyeri",      "litres": 34.0, "cows": 5},
    ] 

#👇 defines a function named (process readings), readings is the list, min litres is the minimum acceptable daily milk target currently 15.0
# r represents one reading r[litres] gets that farms milk production sum() calculates the total
# --- process ---
def process_readings(readings, min_litres): 
    total = sum(r["litres"] for r in readings)
    avg = round(total / len(readings), 1) if readings else 0 #round(...,1) keeps one decimal place, if readings else 0 prevents division by zero when the list is empty
    below_target = [r for r in readings if r ["litres"] < min_litres]# creates a new list containing farms producing less than the minimum target
    top = max(readings, key=lambda r: r["litres"])#max() finds the largest item, key=tells python what value to compare, lambda r: r[litres] means compare farms using their litres
    return { # returns the processed results as a dict
        "farms_collected": len(readings),
        "total_litres": total, # stores the total milk production
        "average_litres": avg, # stores the average production per farm
        "below_target": [r["farm"] for r in below_target],# extracts only the names of farms below target
        "top_farm": top["farm"],
        "top_litres": top["litres"]
    }

# ---- Output ----
def print_farm_report(cooperative, summary):
    print(f"\n{'='*50}")
    print(f" DAILY REPORT: {cooperative.upper()}")
    print(f"{'='*50}")
    print(f" Farms collected: {summary['farms_collected']}")
    print(f" Total litres: {summary['total_litres']:.1f} L")
    print(f" Average per farm: {summary['average_litres']} L")
    print(f" Top farm: {summary['top_farm']} ({summary['top_litres']} L)")
    if summary['below_target']:
        print(f" Below target: {','.join(summary['below_target'])}")
    else:
        print("All farms met target today.")
        print(f"{'='*50}\n")

# --- Main ---
readings = fetch_farm_readings()
summary = process_readings(readings, MIN_LITRES)
print_farm_report(COOPERATIVE, summary)