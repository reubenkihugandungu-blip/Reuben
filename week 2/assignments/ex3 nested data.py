# Create a list of 3 student dictionaries
# Loop through and print each student's name and grade

students = [
    {"name": "Eric", "grade": "A"},
    {"name": "James", "grade": "B"},
    {"name": "Amina", "grade": "A"}
]
for s in students:
    print(f"{s['name']}: {s['grade']}")
# 9 iterates over each dictionary in the list and prints the name and grade of each student.
# s is a variable that represents each dictionary in the list as the loop iterates through it. 
# The print statement uses f-strings to format the output, accessing the 'name' and 'grade' keys of 
# each student dictionary.