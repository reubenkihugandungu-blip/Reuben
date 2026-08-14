# csv.DictReader automatically uses the first row as keys and gives you each row as a dictionary. 
# This is the most practical way to read CSV data because you access values by column name, not by position.
# 
import csv
import io

csv_data = """name,steps,water,protocol,cold_shower
James Omondi,9200,8,OMAD,True
Sandra Weru,10500,9,2MAD,True
Patrick Njiru,7600,6,OMAD,False
Grace Achieng,11000,8,Autophagy Marathon,True"""

f = io.StringIO(csv_data)# reads the file like object and converts it to CSV format
reader = csv.DictReader(f) # reads the file like object and converts it to CSV format, it automatically treats the first row(name,steps ..) as column names/keys
# reader - contains the data ready to loop through
# each row will be a dictionary where you access values by column name (e.g row["name"],row["steps"])
for row in reader:
    steps = int(row["steps"])
    status = "Goal hit" if steps >= 8000 else "Below goal"
    print(f"{row['name']}: {steps} steps | {row['protocol']} | {status}")

# Line 13 prepares the data as a readable file,
#  and line 14 converts it to a dictionary-based format for easy access by column name.
# Tip: All values from a CSV come in as strings.
#  Convert them to the right type before using them in calculations. Use int() for whole numbers and float() for decimals.