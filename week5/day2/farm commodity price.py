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

market = commodity_response["market"] # Gets the value stored under "market" and saves it in the variable market
date = commodity_response["date"] # Gets the market date from the dict and saves it in date
print(f"Market: {market} | Date: {date}")
print("-" * 55)
print(f"{'Commodity':<15} {'unit':<12} {'price (KES)':>12} {'change':>8} Status")
print("-"*55)

available_prices = []#👉 creates an empty list. Available commodity records will be stored here
# 👇loops through every dict inside the "prices" list. Each dict is temporarily called item.
for item in commodity_response["prices"]:
# 👇checks whether the commodity is unavailable
# item["available"] is either True or false
# not reverses the value (False becomes True) therefore, this condition is true when availability is False.
    if not item["available"]:
        continue # skips the current commodity and moves to the next item in the loop.

    available_prices.append(item)# Adds the available commodity dict to available_prices
    if item["change_pct"] > 0:# checks whether the commodity's % change is positive
        status = "rising"# Assigns "rising" if the price increased
    elif item["change_pct"] < 0:
        status = "falling"
    else:
        status = "stable"# Runs when the % change is neither positive nor negative

    change = f"{item['change_pct']:+.1f}%"# + displays a plus sign for positive no,.1f displays one decimal place
    print(f"{item['commodity']:<15} {item['unit']:<12} {item['price_kes']:>12} {change:>8} {status}")

highest_increase = max(available_prices, key=lambda item: item["change_pct"])
print(f"Highest percentage increase: {highest_increase['commodity']} ({highest_increase['change_pct']:+.1f}%)")

#☝️ max() finds the largest value
# available_list is the list being searched, key= tells python what value to compare
# lambda item: item["change_pct"] means: compare items using their "change_pct" value
# Try this:
# Add a filter so only available commodities print. Then add a line at the bottom that prints the commodity with the highest percentage increase.