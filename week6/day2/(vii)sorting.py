# sort_values() sorts by one or more columns. ascending=False sorts high to low.
import pandas as pd
df = pd.DataFrame({
    "name":     ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "steps":    [9200, 10500, 8100, 11000, 7400, 10800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5],
})

# 👇Sort by steps, highest first
# sort_values('steps', ascending false) sorts the rows by the steps column
# .reset_index(drop=True) resets the row numbers after sorting
# drop=true prevents keeping the old index values
ranked = df.sort_values('steps', ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1 # changes the index so it starts from 1 instead of 0, ranked.index is the row index. ranked.index +1 adds 1 to each index old index 0 becomes 1

print("Step leaderboard:")
for i, row in ranked.iterrows():# i gives you the row index, row the values in that row
    print(f" #{i} {row['name']:<20} {row['steps']:,} steps")
# ☝️#{i} prints the ranking number, since index starts at 1, the first row prints #1
# {row['steps']:,} prints the  number with commas as thousands separators

