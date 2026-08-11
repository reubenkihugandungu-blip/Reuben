import io # imports python's io module, which provides file like objects for in memory text and binary data.

# Simulate file content
# Defines a multiline string with several lines of fake file text.
# Each newline inside the triple quotes represents a line break in the simulated file.
file_data = """Steps: 9200
Water: 8 glasses
Protocol: OMAD
cold shower: Yes
Sleep hours: 7.5
"""
# Simulate reading the whole file
f = io.StringIO(file_data) # creates an in line memory text file object containing file_data.
content = f.read()# reads all text from the in memory file into the variable content.
print("Full file content:")
print(content)
