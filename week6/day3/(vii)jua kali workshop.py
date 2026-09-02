# A metalwork workshop tracking jobs by material type uses groupby to answer 
# "which material generates the most revenue?" in a single line. 
# The pattern is identical to everything above.

# WORKSHOP GROUPBY: REVENUE BY MATERIAL
import pandas as pd

df = pd.DataFrame({
    "client":   ["Wanjiru", "Otieno", "Kamau", "Mwangi", "Njeri", 'Odhiambo', "Achieng", "Bett"],
    "item":     ["gate", "grills", "frame", "gate", "grills",  "tank stand", "frame", "gate"],
    "material": ["mild steel","angle iron","hollow tube","mild steel","angle iron","mild steel","hollow tube","mild steel"],
    "price_kes":[28000, 14500, 9800, 32000, 12000, 18500, 11000, 29500],
    "status":   ["paid","paid","pending","paid","paid","pending","paid","paid"],
})

print("Revenue by material type:")
by_material = df.groupby("material")["price_kes"].agg(["sum", "mean", "count"]).round(0)
by_material.columns = ["total_kes", "avg_kes", "jobs"]
print(by_material.sort_values("total_kes", ascending=False).to_string())

print("\nPaid vs pending jobs:")
print(df["status"].value_counts())

print("\nAverage job value by status:")
print(df.groupby("status")["price_kes"].mean().round(0))