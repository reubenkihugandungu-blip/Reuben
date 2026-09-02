# A goat farmer tracks herd weights monthly.
#  Filter underweight animals, add a status column, and sort by weight to identify which goats need priority feeding.

# GOAT FARM: FILTER AND TRANSFORM
import pandas as pd
data = {
    "goat": ["Simba", "Kijana", "Mzee", "Damu", "Furaha", "Pendo", "Jasiri"],
    "breed": ["Boer", "Galla", "Boer", "Galla", "Boer", "Galla", "Boer"],
    "weight_kg": [28, 19, 35, 14, 32, 22, 17],
    "age_months": [18, 12, 36, 8, 24, 15, 10]
}

df = pd.DataFrame(data)

# Flag underweight: Boer target 25kg, Galla target 18kg
def weight_status(row): # creates a function called weight_status, it accepts one  parameter row
    target = 25 if row['breed'] == "Boer" else 18 #if the breed is "Boer target is 25" otherwise target is 18
    return "OK" if row["weight_kg"] >= target else "Needs feeding"

#👇df.apply(..) applies the function to each row in the data frame
# axis=1 tells pandas to apply the function across columns for each row
#The result is stored in a new column called status
df["status"] = df.apply(weight_status, axis=1)

# The lambda function
#👇 r["breed"] == "Boer" checks the breed
# if Boer, target = 25, else target = 18
# then it calculates: target - weight
# max(0, ...) ensures the gap is never negative if the goat is already above target, the gap becomes 0
# axis=1 applies this to every row
df["weight_gap_kg"] = df.apply(
    lambda r: max(0, (25 if r["breed"] == "Boer" else 18) - r["weight_kg"]), axis=1
)

# Show underweight animals sorted by gap
# 👇 df['status'] == "Needs feeding" filters the DataFrame selects only the goats whose status is "Needs Feeding"
# .sort_values("weight_gap_kg", ascending=False) sorts the filtered DataFrame by the weight gap in descending order, so the goats with the largest gap come first
# priority is a new DataFrame that contains only the goats that need feeding, sorted by how much weight they need to gain
priority = df[df["status"] == "Needs feeding"].sort_values("weight_gap_kg", ascending=False) 
print("Priority feeding list:")
print(priority[["goat", 'breed', "weight_kg", "weight_gap_kg"]].to_string(index=False))# priority selects only the columns to display from the priority DataFrame

#☝️.to-string(index=false) converts the table to text
# hides the DataFrame index
# makes the output cleaner