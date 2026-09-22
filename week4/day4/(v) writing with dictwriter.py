# csv.DictWriter writes dictionaries as CSV rows.
# You define the column names (fieldnames) upfront, then write each dictionary as a row.

import csv
import io

clients = [
    {"name": "James", "skill": "welding", "city": "Nairobi", "sessions": 4},
    {"name": "Sandra", "skill": "tiling", "city": "Mombasa", "sessions": 3},
    {"name": "Patrick", "skill": "phone repair", "city": "Nairobi", "sessions": 4},
    {"name": "Grace", "skill": "copywriting", "city": "kisumu", "sessions": 2},
]
output = io.StringIO()
fieldnames = ["name", "skill", "city", "sessions"]
writer = csv.DictWriter(output, fieldnames=fieldnames)

writer.writeheader()
writer.writerows(clients)

print(output.getvalue())