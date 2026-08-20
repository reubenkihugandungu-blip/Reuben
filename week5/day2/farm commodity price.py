# A commodity prices API returns exactly the same kind of nested structure.
#  A farmer or trader who builds a price alert script will parse it using everything you just learned. 
# The technique does not change.

# Parse a commodity price API response
# Simulated response from a commodity prices API
commodity_response = {
    "status": "ok",
    "market": "Wakulima Market, Nairobi",
    "date": "2026-08-13",
    "prices":[
        {"commodity": "Maize", "unit": "90kg bag", "price_kes": 3200, "change_pct": -2.1, "available": True},
        {"commodity": "Beans (Dry)", "unit": "90kg bag", "price_kes": 9800, "change_pct": 4.5, "available": True},
        {"commodity": "Milk (Raw)", "unit": "litre", "price_kes": 62, "change_pct": 1.2, "available": True},
        {"commodity": "Tea leaf", "unit": "kg", "price_kes": 28, "change_pct": -0.8, "available": False},
        {"commodity": "Wheat Flour", "unit": "50kg bag", "price_kes": 2900, "change_pct": 0.0, "available": True},
    ]
}

market = commodity_response["market"]
date = commodity_response["date"]
print(f"Market: {market} | Date: {date}")
print("-" * 55)
print(f"{'Commodity':<15} {'unit':<12} {'price (KES)':>12} {'change':>8} Status")
print("-"*55)

available_prices = []

for item in commodity_response["prices"]:
    if not item["available"]:
        continue

    available_prices.append(item)
    if item["change_pct"] > 0:
        status = "rising"
    elif item["change_pct"] < 0:
        status = "falling"
    else:
        status = "stable"

    change = f"{item['change_pct']:+.1f}%"
    print(f"{item['commodity']:<15} {item['unit']:<12} {item['price_kes']:>12} {change:>8} {status}")

highest_increase = max(available_prices, key=lambda item: item["change_pct"])
print(f"Highest percentage increase: {highest_increase['commodity']} ({highest_increase['change_pct']:+.1f}%)")

# Try this:
# Add a filter so only available commodities print. Then add a line at the bottom that prints the commodity with the highest percentage increase.