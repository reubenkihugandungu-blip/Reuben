# describe() gives you count, mean, std, min, max, 
# and quartiles for every numeric column in one call.

# DESCRIBE THE DATA
import pandas as pd
data = {
    "day":      ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":    [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "water":    [7, 8, 6, 9, 8, 7, 8],
    "bench_press_kg": [80, 82, 78, 85, 80, 83, 84]
}
df = pd.DataFrame(data)# converts the dict into a pandas DataFrame

print("Statistics for all numeric columns:")
print(df.describe().to_string())# calculates summary statistics for numeric columns, .to_strings formats the output as plain text so it prints neatly

print("\nManual checks:")
print(f"Mean steps: {df['steps'].mean():.0f}")# df['steps'] selects the steps column as a pandas series : formats the result as a whole numbers without decimals
print(f"Mean weight lifted: {df["bench_press_kg"].mean():.0f}")
print(f"Max steps: {df['steps'].max()}")
print(f"Min steps: {df['steps'].min()}")
print(f"Total steps: {df['steps'].sum()}")

# Every column in a DataFrame is a Series. 
# All the statistical methods (mean(), sum(), max(), min(), std()) work on Series directly.