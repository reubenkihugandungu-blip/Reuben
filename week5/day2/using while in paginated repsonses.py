
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
    "next_page": 3,
    "data": [
        {"name": "Grace Achieng", "steps": 11000},
        {"name": "Brian Kamau", "steps": 7400},
        {"name": "Kevin Mwangi", "steps": 10800},
    ]
}

page_3 = {
    "page": 3,
    "total_pages": 3,
    "per_page": 3,
    "next_page": None,
    "data": [
        {"name": "Lilian Wanjiku", "steps": 8700},
        {"name": "Dennis Otieno", "steps": 9900},
        {"name": "Amina Hassan", "steps": 11200},
    ]
}

pages = {1: page_1, 2: page_2, 3: page_3}# creates a dict that connects each page number to its page data
all_records = [] # creates an empty list for storing records for every page
next_page = 1 # start with page 1

while next_page is not None: # keeps looping as long as there is another page. None means no more pages
    current_page = pages[next_page] # adds the current page's records to all_records
    all_records.extend(current_page["data"])# updates next_page using the current pages "next_page" value
    next_page = current_page["next_page"]# loop runs like this page 1 points to page 2, 2 to 3, 3 to None. The condition becomes false

print(f"Total records collected: {len(all_records)}")
for r in all_records:
    print(f" {r['name']}: {r['steps']} steps")
