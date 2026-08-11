# Adding a contact means creating a new dictionary and appending it to the list.
#  Use the same structure as the existing contacts.

contacts = [
    {"name": "James Omondi", "phone": "0712345678", "skill": "welding",  "city": "Nairobi"},
    {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling",   "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu"},
    {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},
]

print("Before:", len(contacts), "contacts")
# Add a new contact
new_contact = {
    "name": "Kevin Mwangi",
    "phone": "0767890123",
    "skill": "beekeeping",
    "city": "Nakuru"
}
contacts.append(new_contact)

print("After:", len(contacts), "contacts")
print("Last contact:", contacts[-1])
