# A file is a named container of data stored on your computer. Text files store plain text, 
# one line after another. Python can read from them and write to them using built-in functions.

# open() is Python's built-in function for working with files. You give it a file name and a mode. 
# The mode tells Python what you want to do:
#  "r" for read, "w" for write (overwrites), "a" for append (adds to end).
#  Always close the file when you are done, or use a with statement that does it automatically.

# Mode	    What it does	                              If file does not exist
# "r"	    Read only.Cannot change the file.	           Error
# "w"	    Write. Creates or overwrites the file.	       Creates it
# "a"	    Append. Adds to the end of the file.	       Creates it