# csv.reader reads a CSV file and gives you each row as a list. 
# The first row (the header) is just another list.

import csv
import io

# Simulated CSV content
csv_data = """name,phone,skill,city
James Omondi,0712345678,welding,Nairobi
Sandra Weru,0723456789,tiling,Mombasa
Patrick Njiru,0734567890,phone repair,Nairobi
Grace Achieng,0745678901,copywriting,Kisumu
Brian Kamau,0756789012,upholstery,Nairobi"""

f = io.StringIO(csv_data)
reader = csv.reader(f)

for row in reader:
    print(row)

# Each row is a Python list. The first row is the header. To skip it, call next(reader) before the loop.