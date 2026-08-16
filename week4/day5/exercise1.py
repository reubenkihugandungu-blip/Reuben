# File writing
# Write a program that saves your name and city to a text file
# then reads it back and prints it

import tempfile, os # imports modules - tempfile for creating temporary files and OS for operating system operations
path = tempfile.mktemp(suffix='.txt')# suffix= .txt parameter adds a txt extension to the temporary filename, stores this variable  in the variable path
with open(path, 'w') as f: # open the file at the stored path in write mode("w") with statement ensures the file is closed when done
      f.write("Name: Reuben\nCity: Nyahururu\n")
with open(path) as f:# opens the file again this time in read mode(default when no mode is specified)
    print(f.read())# Reads all the file content using(read)