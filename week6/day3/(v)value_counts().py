# value_counts() counts how many times each unique value appears in a column. 
# It returns a Series sorted by count, highest first.

#COUNT UNIQUE VALUES
import pandas as pd

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian", "Kevin", "James", "Grace", "Sandra", "James"],
    "protocol": ["OMAD", "2MAD", "OMAD", "OMAD", "2MAD", "OMAD", "OMAD", "OMAD", "2MAD", "OMAD"],
    "city":     ["Nairobi", "Mombasa", "Nairobi", "Kisumu", "Nairobi", "Mombasa", "Nairobi", "Kisumu", "Mombasa", "Nairobi"],
})

print("Protocol distribution:")
print(df["protocol"].value_counts())

print("\nCity distribution:")
print(df["city"].value_counts())