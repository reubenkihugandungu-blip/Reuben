# Create a dictionary for a student with name, age, and grade
# Print each value using the key

student = {"name": "Eric", "age": 25, "grade": "A"}
for key, value in student.items(): 
    print(f"{key}: {value}")
# students.items() returns pairs of keys and values.
# 5 each loop iteration assigns the current key to key, 
# & the current value to value