# You have a simulated CSV of a week's step data.
#  Read it with DictReader, convert steps to integers, filter out any days with steps below 7000 as invalid,
#  and print the average steps for the valid days only.

import csv # brings in CSV handling functionality
import io # provides tools for working with text streams

csv_data = """day,steps,protocol # creates a multiline string containing CSV data(day,steps, protocol for a week)
Monday,9200,OMAD
Tuesday,7500,2MAD
Wednesday,10500,OMAD
Thursday,4200,OMAD
Friday,8800,Autophagy Marathon
Saturday,11000,2MAD
Sunday,9600,OMAD"""

f = io.StringIO(csv_data) # wraps the text string so it can be read like a file.
reader = csv.DictReader(f) # reads it as CSV treating the fisrst row as headers and returning each row as a dictionary

valid_steps = []
for row in reader: # loops through each day's data
    steps = int(row["steps"]) # converts steps from text to integer with int(row["steps"])
    if steps >= 7000:
        valid_steps.append(steps) # filters only keeps days with 7000+ steps(marks others as invalid)
        print(f"{row['day']}: {steps} steps ({row['protocol']})")
    else:
        print(f"{row['day']}: {steps} steps - flagged as invalid")

avg = sum(valid_steps) / len(valid_steps)
print(f"\nAverage (valid days): {round(avg)} steps")
