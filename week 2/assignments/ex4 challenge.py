# Build a simple phonebook
# Store 3 contacts as a dictionary of name: number
# Print a formatted contact list

phonebook = {"Eric": "0712345678", "James": "0723456789", "Amina": "0734567890"}
print("--- CONTACT LIST ---")
for name, number in phonebook.items():
    print(f"{name}: {number}")