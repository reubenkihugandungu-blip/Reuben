# csv.writer writes rows to a CSV. Each call to writerow() writes one row as a list.
# simulate writing csv
import csv
import io

output = io.StringIO()
writer = csv.writer(output)

# Write header
writer.writerow(["name", "steps", "protocol", "goal_hit"])

# Write data rows
data = [
    ["James", 9200, "OMAD", True],
    ["Sandra", 10500, "2MAD", True],
    ["Patrick", 7600, "OMAD", False],
    ["Grace", 11000, "Autophagy Marathon", True],
]

for row in data:
    writer.writerow(row)
    
print("Generated CSV:")
print(output.getvalue())