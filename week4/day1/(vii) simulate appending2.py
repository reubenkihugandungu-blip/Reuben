import io

# Start with existing content
file_data = "Steps: 9200\nWater: 8 glasses\nProtocol: OMAD\n" # creates a string named file_data. With three lines of text.
# \n adds a newline  so each item appears on its own line

# Simulate append
file_data += "Pages read: 30\n" # appends another line to the existing string, += adds new text to the end.
file_data += "Workout: benchpress 5*5 at 80kg\n"

print("File after appending:")
print(file_data)