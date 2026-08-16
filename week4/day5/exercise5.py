# A carpenter tracks daily production: chairs made and timber used.
#  Read the log, calculate totals, and print a summary.
# Modify the values and run it again to see how the totals change.

import io

#  Carpentry workshop daily log: day, chairs made, timber used (metres)
workshop_log = """Monday,8,24
Tuesday,6,18
Wednesday,10,30
Thursday,7,21
Friday,9,27
"""
total_chairs = 0
total_timber = 0
days = 0

f = io.StringIO(workshop_log)
for line in f:
    line = line.strip()
    if line:
        day, chairs, timber = line.split(",")
        chairs = int(chairs)
        timber = int(timber)
        print(f"{day}: {chairs} chairs | {timber}m timber")
        total_chairs += chairs
        total_timber += timber
        days += 1

print(f"\nTotal chairs made: {total_chairs}")
print(f"Total timber used: {total_timber}m")
print(f"Average chairs per day: {total_chairs // days}")
