# A dairy farmer logs morning and evening milk yield per cow. 
# Read the log, calculate each cow's daily total, flag any cow producing below 10 litres, 
# and print the herd summary.

import io

# Daily log: cow_name, morning_litres, evening_litres
milk_log = """Daisy,6.5,7.2
Bella,4.1,4.8
Nala,8.3,9.1
Rosa,3.2,3.5
Lola,7.8,8.4
"""
total_herd = 0
low_producers = []

f = io.StringIO(milk_log)
for line in f:
    line = line.strip()
    if line:
        name, morning, evening = line.split(",")
        daily = float(morning) + float(evening)
        status = "OK" if daily >= 10 else "LOW"
        print(f"{name}: {daily:.1f} litres [{status}]")
        total_herd += daily
        if daily < 10:
            low_producers.append(name)
print(f"\nHerd total: {total_herd:.1f} litres")
print(f"Low producers: {','.join(low_producers) if low_producers else 'None'}")