# Add a "bench_press_kg" column to the groupby examples and group by protocol to find the average bench press per protocol.
# Which protocol correlates with higher bench press in the data?

import pandas as pd
import numpy as np

df = pd.DataFrame({
    "name":     ["James", "Sandra", "Patrick", "Grace", "Brian"],
    "steps":    [9200, None, 8100, 11000, None],
    "sleep_hr": [7.5, 8.0, None, 7.0, 9.0],
    "bench_press_kg": [80, 90, None, 100, 85],
    "protocol": ["A", "B", "A", "B", "A"]
})

print("Original with NaN:")
print(df.to_string())

print("\nRows with any missing value:")
print(df[df.isna().any(axis=1)].to_string())

# Fill missing steps with the column mean
df["steps"] = df["steps"].fillna(df["steps"].mean())
df["sleep_hr"] = df["sleep_hr"].fillna(df["sleep_hr"].median())
df["bench_press_kg"] = df["bench_press_kg"].fillna(df["bench_press_kg"].mean())

print("\nAfter filling NaN:")
print(df.to_string())

# Group by protocol and find average bench press per protocol
print("\nAverage bench press by protocol:")
avg_by_protocol = df.groupby("protocol")["bench_press_kg"].mean()
print(avg_by_protocol)

# Which protocol has higher average bench press?
print("\nAnalysis:")
print(f"Protocol A average: {avg_by_protocol['A']:.2f} kg")
print(f"Protocol B average: {avg_by_protocol['B']:.2f} kg")
if avg_by_protocol['A'] > avg_by_protocol['B']:
    print("✓ Protocol A correlates with higher bench press")
else:
    print("✓ Protocol B correlates with higher bench press")
