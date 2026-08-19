# Many APIs return data in pages. Instead of sending 10,000 records at once, they send 100 at a time 
# and include a next_page key. In a script you would loop, checking for None to stop. 
# Here you see the response structure.
# what page 1 of a paginated API looks like

page_1 = {
    "page": 1,
    "total_pages": 3,
    "per_page": 3,
    "next_page": 2,
    "data": [
        {"name": "James Omondi", "steps": 9200},
        {"name": "Sandra Weru", "steps": 10500},
        {"name": "Patrick Njiru", "steps": 8100},
    ]
}

page_2 = {
    "page": 2,
    "total_pages": 3,
    "per_page": 3,
    "data": [
        {"name": "Grace Achieng", "steps": 11000},
        {"name": "Brian Kamau", "steps": 7400},
        {"name": "Kevin Mwangi", "steps": 10800},
    ]
}

# Combine pages manually
all_records = page_1["data"] + page_2["data"]
print(f"Total records collected: {len(all_records)}")
for r in all_records:
    print(f" {r['name']}: {r['steps']} steps")

# In a script you would use a while loop: keep fetching the next page until next_page is None.
#  The data processing code stays the same regardless of how many pages there are.