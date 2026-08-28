# TRADE APPLICATION - WELDING JOB QUOTE
# A welder receives steel prices from a supplier API. Parse the response, list the prices,
# and calculate the cost of one steel door frame. Change the quantities and see how the quote updates.

import json

# Simulated API response from a steel supplier
response_text = '''
{
    "supplier": "Nairobi Steel Ltd",
    "date": "2026-07-27",
    "prices": {
        "mild_steel_sheet": 4500,
        "angle_iron": 2800,
        "square_tube": 3200
    },
    "currency": "KES",
    "unit": "per metre"
}
'''

data = json.loads(response_text)# converts the json text into a python dict, allows you to access values using keys 

print(f"Supplier: {data['supplier']}")
print(f"Date: {data['date']}")# prints the date from the data dict.
print(f"\nSteel prices ({data['currency']} {data['unit']}):")
for item, price in data["prices"].items():# loops through every item in the prices dict
    print(f"  {item.replace('_', ' ').title()}: KES {price:,}")# replace - changes underscores into spaces .title - capitilizes each word, price:, adds commas to large numbers

# One steel door frame: 3 pieces of angle iron (2m each) + 1 mild steel sheet
angle_cost = data["prices"]["angle_iron"] * 2 * 3 # Calculates the total cost of angle iron, each price 2 metres & there are 3 pieces
sheet_cost = data["prices"]["mild_steel_sheet"]# gets the price of one mild steel sheet and stores it in sheet_cost
frame_cost = angle_cost + sheet_cost

print(f"\nDoor frame quote:") # Prints a heading for the quotation with a blank line before it
print(f"  Angle iron (3 x 2m): KES {angle_cost:,}")
print(f"  Mild steel sheet: KES {sheet_cost:,}")
print(f"  Total: KES {frame_cost:,}")