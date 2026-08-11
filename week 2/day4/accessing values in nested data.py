# To get a value from inside a nested structure, chain your square brackets.
#  First bracket picks the list item. Second bracket picks the dictionary key.
# week_log[0]["steps"] steps from the first day (Monday)
# week_log[2]["day"] Day name of the third record (Wednesday)

week_log = [
    {"day": "Monday", "steps": 9200, "protocol": "OMAD"},
    {"day": "Tuesday", "steps": 10500, "protocol": "2MAD"},
    {"day": "Wednesday", "steps": 8800, "protocol": "OMAD"},
]
# Third day's protocol
print("Wednesday protocol:", week_log[2]["protocol"]) # week_log[2] is the list item
# ["protocol"] is the dictionary key
# second day, all details
print("Tuesday:", week_log[1])


