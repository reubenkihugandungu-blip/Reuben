# Try this:
# Add a "region" column (Nairobi, Kiambu, Machakos).
# Group by both region and material to find which region earns most per job type.
import pandas as pd

df = pd.DataFrame({
    "client":   ["Wanjiru", "Otieno", "Kamau", "Mwangi", "Njeri", 'Odhiambo', "Achieng", "Bett"],
    "item":     ["gate", "grills", "frame", "gate", "grills",  "tank stand", "frame", "gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes":[28000, 14500, 9800, 32000, 12000, 18500, 11000, 29500],
    "status":   ["paid","paid","pending","paid","paid","pending","paid","paid"],
    "region":   ["Nairobi", "Kiambu", "Machakos", "Nairobi", "Kiambu", "Machakos", "Nairobi", "Kiambu"],
})

print("Revenue by material type:")
by_material = df.groupby("material")["price_kes"].agg(["sum", "mean", "count"]).round(0)
by_material.columns = ["total_kes", "avg_kes", "jobs"]
print(by_material.sort_values("total_kes", ascending=False).to_string())

print("\nRevenue by region and material:")
region_material = (
    df.groupby(["region", "material"], as_index=False)["price_kes"]
      .sum()
      .rename(columns={"price_kes": "total_kes"})
      .sort_values(["region", "total_kes"], ascending=[True, False])
)
print(region_material.to_string(index=False))

print("\nHighest earning region per job type:")
region_winner_per_material = (
    region_material.sort_values(["material", "total_kes"], ascending=[True, False])
    .drop_duplicates(subset="material")
    .rename(columns={"total_kes": "region_total_kes"})
)
print(region_winner_per_material[["material", "region", "region_total_kes"]].to_string(index=False))

print("\nPaid vs pending jobs:")
print(df["status"].value_counts())

print("\nAverage job value by status:")
print(df.groupby("status")["price_kes"].mean().round(0))