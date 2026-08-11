# Loop through the list and compare each contact's name to the name you are searching for. 
# If it matches, print that contact's details..
# search by name and print the result.


contacts = [
    {"name": "James Omondi", "phone": "0712345678", "skill": "welding",  "city": "Nairobi"},
    {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling",   "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu"},
    {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},
]

search_name = "Emma"
found = False # creates a flag variable to track whether a matching contact is found.

for contact in contacts:
    if contact["name"] == search_name:# checks if the current contact's name value matches search_name
        print("Contact found:")
        print(f" Name : {contact['name']}")
        print(f" Phone : {contact['phone']}")
        print(f"Skill : {contact["skill"]}")
        print(f" City : {contact['city']}")
        found = True# sets the flag to True so the program knows a match was found.
        break # stops the loop early the desired contact has already been found

# checks whether the loop finished without finding a match.
# no match it prints a message saying contact was not found.
if not found:
    print("No contact found with name:", search_name)
