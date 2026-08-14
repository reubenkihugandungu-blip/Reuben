# Each row is a Python list. The first row is the header. To skip it, call next(reader) before the loop.

import csv
import io

csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)
next(reader)  # skip header row

for row in reader:
    name, phone, skill, city = row
    print(f"{name} | {skill} | {city}")