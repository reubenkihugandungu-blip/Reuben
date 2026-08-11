# A more useful search shows all contacts from a specific city, not just a single name match.
#  This requires printing every matching contact, not stopping at the first one.


contacts = [
    {"name": "James Omondi", "phone": "0712345678", "skill": "welding",  "city": "Nairobi"},
    {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling",   "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu"},
    {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},
]

search_city = "Nairobi"
print(f"Contacts in {search_city}:")

for contact in contacts:
    if contact["city"] == search_city:
        print(f" {contact['name']} | {contact}['skill'] | {contact['phone']}")
        