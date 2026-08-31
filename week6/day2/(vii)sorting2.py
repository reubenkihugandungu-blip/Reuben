# Try this:
# Sort by sleep_hr in descending order and print who gets the most sleep.
# Then add a "wake_up_score" column using sleep_hr * steps / 1000 and sort by that.

import pandas as pd

df = pd.DataFrame({
    "name": ["James Omondi", "Sandra Weru", "Patrick Njiru", "Grace Achieng", "Brian Kamau", "Kevin Mwangi"],
    "steps": [9200, 10500, 8100, 11000, 7400, 10800],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5],
})

# Add a new score column using sleep_hr * steps / 1000
df['wake_up_score'] = (df['sleep_hr'] * df['steps']) / 1000

# Sort by the new score, highest first
ranked = df.sort_values('wake_up_score', ascending=False).reset_index(drop=True)
ranked.index = ranked.index + 1

print("Wake-up score leaderboard:")
for i, row in ranked.iterrows():
    print(f" #{i} {row['name']:<20} {row['wake_up_score']:.2f} score")
