# .isin() checks if a column's value is in a list.
#  It is cleaner than chaining multiple | conditions when you have several allowed values.

# FILTER WITH .ISIN()
import pandas as pd

df = pd.DataFrame({
    "name":    ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", " Brian Kamau", " Kevin Mwangi"],
     "city":   ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa"],
    "steps":   [9200, 10500, 8100, 11000, 7400, 10800],
    "protocol":["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD"],
})

# Members from Nairobi or Mombasa
nbi_msa = df[df["city"].isin(["Nairobi", "Mombasa"])]
print("Nairobi and Mombasa members:")
print(nbi_msa[["name", "city", "steps"]].to_string())
