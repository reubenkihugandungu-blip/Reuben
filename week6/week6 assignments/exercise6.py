# A dairy farmer records weekly milk yield per cow over four weeks.
#  Calculate each cow's total and average, identify the top producer,
#  and flag any cow whose weekly average drops below 60 litres.

# FARMING APPLICATION - WEEKLY MILK YIELD ANALYSIS
# Weekly milk yield per cow (litres)
herd_data = [
    {"cow": "Daisy", "yields": [72, 68, 74, 70]},
    {"cow": "Bella", "yields": [45, 42, 38, 40]},
    {"cow": "Nala",  "yields": [88, 91, 85, 93]},
    {"cow": "Rosa",  "yields": [55, 58, 52, 50]},
    {"cow": "Lola",  "yields": [78, 80, 76, 82]},
]

MINIMUM_WEEKLY = 60
top_cow = None
top_total = 0

print(f"{'Cow':<8} {'Total':>8} {'Avg/wk':>8} {'Status':>10}")
print("-" * 38)

for cow in herd_data:
    total = sum(cow["yields"])
    avg = total / len(cow["yields"])
    status = "OK" if avg >= MINIMUM_WEEKLY else "NEEDS ATTENTION"
    print(f"{cow['cow']:<8} {total:>8} {avg:>8.1f} {status:>10}")
    if total > top_total:
        top_cow = cow["cow"]

print(f"\nTop producer: {top_cow} ({top_total} litres over 4 weeks)")

