# my_log

my_log = {        # start creating a dictionary and assign it to the variable.
    "steps": 9400, # dict entry; key "steps" value 9400
    "water_glasses": 7,
    "fasting_protocol": "OMAD",
    "cold_shower": True,
    "sleep_hours": 7.0
}

for key, value in my_log.items(): # loop over the dictionary's items, each iteration unpacks a key and its corresponding value.
    print(key, ":", value) # inside the loop print the key, a colon, then the value.
print() # prints a blank line for readability. TO separate output sections.
if my_log["steps"] >= 8000: # from my_log access the step value and test whether it is >= 8000
    print("Step goal hit.") # if condition is true, p the success message.
else: # if condition is false run the following block
    print("Step goal missed.")
