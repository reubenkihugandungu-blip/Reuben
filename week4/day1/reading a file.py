# Use open("filename", "r") to read
#  .read() reads the entire file as one string,.readlines() reads each line into a list.

# In Vs code, this reads a file from your computer:
with open("daily_log.txt", "r") as f:
    content = f.read()
    print(content)