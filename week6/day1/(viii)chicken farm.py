# A chicken farmer tracking daily egg production and feed cost uses a DataFrame exactly as you have just learned. 
# The commands are identical. Only the column names change.

# CHICKEN FARM DATFRAME
import pandas as pd
data = {
    "day":         ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "eggs":        [312, 298, 320, 305, 290, 315, 308],
    "feed_kg":     [18.5, 18.0, 19.2, 18.8, 17.5, 18.6, 19.0],
    "deaths":      [0, 1, 0, 0, 2, 0, 0],
    "pen":         ["A", "A", "A", "B", "B", "B", "A"],    
    "revenue_kes": 18
}
df = pd.DataFrame(data)

# Add revenue column: each egg earns KES 18
df["revenue_kes"] = df["eggs"] * 18

print("Weekly egg production log:")
print(df.to_string())

print("\nShape:", df.shape)#df.shape returns the dataframe size as (rows, columns) 7 days and 6 columns
print("\nSummary statistics:")
print(df[["eggs", "feed_kg", "deaths", "revenue_kes"]].describe().round(1).to_string())# statistical summary for the selected numeric column

print(f"\nTotal eggs this week: {df['eggs'].sum()}")
print(f"Average daily eggs: {df['eggs'].mean():.1f}")
print(f"Weekly total revenue: KES {df['revenue_kes'].sum():.0f}")
print(f"Worst day (eggs): {df.loc[df['eggs'].idxmin(), 'day']} ({df['eggs'].min()} eggs)")

#☝️df['eggs'].idxmin() finds the index of the day with the minimum number of eggs
# df.loc[..] looks up that row
# 'day' gets the day name
# df['eggs'].min() gets the lowest egg count