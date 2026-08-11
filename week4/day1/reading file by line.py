# Reading one line at a time is more efficient for large files and lets you process each line individually.

import io # Imports the io module, which provides in memory stream classes like stringIO

file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
Cold shower: Yes
sleep hours: 7.5
""" # A multiline string assigned to file data that simulates fake file contents.
f = io.StringIO(file_data) # creates an in memory text stream StringIO from file_data, behaving like a file object
lines = f.readlines()# reads  all lines from the StringIO stream into a list lines; each element ends with a newline \n except possibly the last

print(f"Number of lines: {len(lines)}") # prints the number of lines, uses an f string
print()
for line in lines: # starts a loop to process each line from the lines list.
    line = line.strip() # to remove leading/trailing whitespace(including \n) and updates line.
    print("Line:", line)

# strip() removes whitespace and newline characters from the start and end of a string. 
# Always use it when reading lines from a file.