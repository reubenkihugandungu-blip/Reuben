# JSON is not only for fitness apps. Any business that tracks records uses it.
#  Here is how a Jua Kali welding workshop might store a job record and read it back in Python:
# Workshop job record
import json

# A welding workshop stores job records as JSON
job_json = '''
{
"workshop": "Kamau Metalworks",
"location": "Gikomba, Nairobi",
"jobs": [
{"client": "Wanjiru", "item": "gate", "material": "mild steel", "quote_kes": 28000, "paid": true},
{"client": "Otieno", "item": "window grills", "material": "angle iron", "quote_kes": 14500, "paid": false},
{"client": "Mwangi", "item": "door frame", "material": "hollow tube", "quote_kes": 9800, "paid": true},
{"client": "Edna", "item": "Curtain rods", "material": "hollow tube", "quote_kes": 12000, "paid": false},
{"client": "Victor", "item": "flowers", "material": "aluminium", "quote_kes": 8000, "paid": true}
]
}
'''
data = json.loads(job_json)
print("Workshop:", data["workshop"])
print("Location:", data["location"])
print()

total = 0
paid = 0
for job in data["jobs"]:
    status = "PAID" if job ["paid"] else "PENDING"
    print(f" {job['client']}: {job['item']} - KES {job['quote_kes']:,} [{status}]")
    total += job["quote_kes"]
    if job["paid"]:
        paid += job["quote_kes"]

print(f"\nTotal quoted: KES {total:,}")
print(f"Collected: KES {paid:,}")
print(f"Ouststanding: KES {total - paid:,}")
    