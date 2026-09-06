# A tiling contractor tracks jobs completed across different clients.
#  Calculate total boxes laid, total revenue, and the average price per box across all jobs.
#  Add your own job and re-run.

# Tiling contractor job records
jobs = [
    {"client": "Kamau", "location": "Kiambu", "boxes_used": 30, "price_per_box": 1800},
    {"client": "Mutua", "location": "Machakos", "boxes_used": 48, "price_per_box": 2100},
    {"client": "Odhiambo", "location": "Kisumu", "boxes_used": 20, "price_per_box": 1600},
    {"client": "Wanjiru", "location": "Nakuru", "boxes_used": 60, "price_per_box": 2200},
]

print("Job Summary:")
print("-" * 50)
total_boxes = 0
total_revenue = 0

for j in jobs:
    revenue = j["boxes_used"] * j["price_per_box"]
    print(f"{j['client']} ({j['location']}): {j['boxes_used']} boxes | KES {revenue:,}")
    total_boxes += j["boxes_used"]
    total_revenue += revenue

avg_price = total_revenue / total_boxes

print(f"\nTotal boxes laid: {total_boxes}")
print(f"Total revenue: KES {total_revenue:,}")
print(f"Average price per box: KES {avg_price:.0f}")