# Once you have the lines, you can parse them into a dictionary.
#  Each line is a label and a value separated by a colon.

# parse lines into a dictionary.

import io
file_data = """Steps: 9200
water: 8
protocol: OMAD
Cold shower: Yes
Sleep hours: 7.5
pages read: 30
""" # closes the multiline string assigned to file_data, at this point file data contains full simulated file text.

log = {} # creates an empty dictionary named log, this will store parsed key/value pairs from the file content.
f = io.StringIO(file_data)# creates an in memory file object from the string file_data, f behaves like a file opened for reading
for line in f: # loops over each line in the simulated file, each iteration reads one line from f.
    line = line.strip()# removes whitespace from both ends of the line & newline characters and extra spaces.
    if ":" in line: # checks whether the line contains a colon, only lines with key:value format are processed.
        key, value = line.split(":", 1)# split the line into two parts at the first colon. key gets the text before the colon, value gets the text after it.
        log[key.strip()] = value.strip()# trims extra spaces from both key & value. stores them in the dictionary log as log[key] = value

print("Parsed log:")
for key, value in log.items(): # loops through each key/value pair in the dictionary
    print(f" {key}: {value}") # prints each parsed item in key:value format