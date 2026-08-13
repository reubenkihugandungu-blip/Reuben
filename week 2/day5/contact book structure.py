# Each contact is a dictionary.
# The full contact book is a list of those dictionaries. 
# Start by creating five contacts and printing them.

contacts = [
    {"name": "James Omondi", "phone": "0712345678", "skills": "welding",  "city": "Nairobi"},
    {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling",   "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu"},
    {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},
]
print("Contacts stored:", len(contacts))
print(contacts[0]["phone"])

#
