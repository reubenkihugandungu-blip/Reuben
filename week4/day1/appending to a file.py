# Use mode "a" to add content to the end of an existing file without deleting what is already there.

with open("daily_log.txt", "a") as f:
    f.write("Pages read: 30\n")
    f.write("Workout: bench press\n")