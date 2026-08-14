# Crop Harvest Tracker
# A crop farmer tracks harvest yield per field using a CSV.
#  The same DictReader pattern reads each field's output and flags underperforming plots.

import csv, io # imports both modules

harvest_csv = """field,crop,bags_harvested,target_bags
North Plot,Maize,48,50
South Plot,Beans,22,30
East Plot,Wheat,61,55
West Plot,Maize,35,50
Centre Plot,Sorghum,44,40
"""
reader = csv.DictReader(io.StringIO(harvest_csv)) # (io.stringio(harvest_csv) converts the string into a file like object)
# reader csv.dictreader() reads it as CSV with headers, returns each row as a dict, reader stores this for looping
print(f"{'Field':<15} {'Crop':<10} {'Harvested':>10} {'Target':>8} {'Status':>12}")
# prints column headers with formatting :<15 left align in 15 characters, :>10 right align in 10 characters
print("-" * 63) # prints dashes as a separator (63characters)

for row in reader:# iterates through each harvest record
    harvested = int(row["bags_harvested"])# converts harvest count to integer
    target = int(row["target_bags"])
    pct = (harvested / target) * 100 # calculates %ntage not used in output
    status = "On target" if harvested >= target else f"Short by {target - harvested} bags"
    print(f"{row['field']:<15} {row['crop']:<10} {harvested:>10} {target:>8} {status:>12}")
    
