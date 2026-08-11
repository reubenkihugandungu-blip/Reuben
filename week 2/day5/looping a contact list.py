# Printing the raw list is hard to read. Write a loop that prints each contact in a clean format.
# Loop through the list and print each contact with a readable layout.

contacts = [
    {"name": "James Omondi", "phone": "0712345678", "skill": "welding",  "city": "Nairobi"},
    {"name": "Sandra Weru", "phone": "0723456789", "skill": "tiling",   "city": "Mombasa"},
    {"name": "Patrick Njiru", "phone": "0734567890", "skill": "phone repair", "city": "Nairobi"},
    {"name": "Grace Achieng", "phone": "0745678901", "skill": "copywriting", "city": "Kisumu"},
    {"name": "Brian Kamau", "phone": "0756789012", "skill": "upholstery", "city": "Nairobi"},
]

print("==== CONTACT BOOK ====")
for i, contact in enumerate(contacts):# returns pairs,the index and the contact item.
    print(f"\n{i+1}. {contact['name']}")# \n p a blank line followed by the contact name and no
    print(f"  Phone : {contact['phone']}")# p the phone number of the current contact
    print(f"  Skill : {contact['skill']}")

# enumerate() gives you both the index and the item as you loop. 
# i is the index number, contact is the dictionary{with name, phone, skill}
#  It starts at 0, so i+1 gives you numbering that starts at 1.
# ln 14{i+1} converts the zero based index into human friendly numbering starting at 1
# ln 14{contact['name']} gets the name value from the current contact dictionary