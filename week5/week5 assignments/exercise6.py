# Farming Application — Crop Market Price Checker

# A crop farmer fetches today's commodity prices from a market API. Parse the response,
# list prices per bag, and calculate the value of the farmer's current stock for each crop.

import json

# Simulated crop market API response
response_text = '''
{
    "market": "Wakulima Market, Nairobi",
    "date": "2026-07-27",
    "prices_per_bag_kes": {
        "maize": 3800,
        "beans": 9200,
        "wheat": 5500,
        "sorghum": 3200
    },
    "bag_weight_kg": 90
}
'''

data = json.loads(response_text)

# Farmer's current stock in bags
stock = {"maize": 12, "beans": 5, "wheat": 8, "sorghum": 20}

print(f"Market: {data['market']}")
print(f"Date: {data['date']}\n")
print("Crop Valuation:")
print("-" * 40)

total_value = 0 # starts the total at zero 
for crop, bags in stock.items(): # loops through each crop and its number of bags
    price = data["prices_per_bag_kes"][crop]
    value = bags * price
    print(f"{crop.title()}: {bags} bags x KES {price:,} = KES {value:,}")
    total_value += value # adds the crop's value to the running total

print(f"\nTotal stock value: KES {total_value:,}")