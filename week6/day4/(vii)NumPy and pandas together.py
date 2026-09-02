# NumPy and pandas work together. A pandas Series is built on a NumPy array. 
# You can pull a column out of a DataFrame as a NumPy array using .values or .to_numpy().
#  Many pandas methods internally use NumPy for speed.

# NUMPY AND PANDAS TOGETHER
import numpy as np
import pandas as pd

df = pd.DataFrame({
    "day":            ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps":          [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr":       [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "bench_press_kg": [80, 82, 78, 85, 80, 83, 84]
})

# Pull a column as a NumPy array
steps_arr = df["steps"].to_numpy()
print("NumPy array from pandas column:", steps_arr)
print("Type:", type(steps_arr))

steps = df["steps"].to_numpy()
bench = df["bench_press_kg"].to_numpy()
print("\nCorrelation between steps and bench press:")
print(np.corrcoef(steps, bench))

# Use NumPy on it
print(f"\nMean: {np.mean(steps_arr):,.0f}")
print(f"Std dev: {np.std(steps_arr):,.0f}")

# Add a normalized column back to the DataFrame
# Normalize to 0-1 range (min-max scaling)
df["steps_norm"] = (df["steps"] - df["steps"].min()) / (df["steps"].max() - df["steps"].min())
df["steps_norm"] = df["steps_norm"].round(3)
print("\nWith normalized steps:")
print(df[["day", "steps", "steps_norm"]].to_string())

# Try this:
# Add a bench_press_kg array with values like [80, 82, 78, 85, 80, 83, 84].
# Compute the correlation between steps and bench press using np.corrcoef(steps, bench). 
# A value close to 1.0 means they move together; close to 0 means no relationship.