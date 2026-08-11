# Use open("filename", "w") to write. 
# "w" means creae the file if it doesn't exist, or overwrite it if it does.
# The with statement automatically closes the file when the block ends, even if an error occurs.

# In vs code, this creates a file on your computer:
with open("daily_log.txt", "w") as f: 
    f.write("Steps: 9200\n") # writes the text steps: 9200 to the file.
    f.write("Water: 8 glasses\n")# \n newline character so the next write starts on a newline.
    f.write("Protocol: OMAD\n")
    f.write("Cold shower: Yes\n")