# not writing to a real disk file. Using io.stringIO() to create an in memory text buffer that behave like a file.
# This is useful when you want to practice file operations or test code without creating an actual file on your computer.

import io

# Simulating file write using in-memory buffer
file_content = io.StringIO()
file_content.write("Steps: 9200\n")
file_content.write("Water: 8 glasses\n")
file_content.write("Protocol: OMAD\n")
file_content.write("Cold shower: Yes\n")

print("File written. Contents:")
print(file_content.getvalue())

# The \n at the end of each string is a newline character. 
# Without it, all your text runs together on one line.