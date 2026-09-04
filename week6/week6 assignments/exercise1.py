# DATAFRAMES
import pandas as pd

# Create a Dataframe from a dict and inspect it
data = {
    "name": ["Eric", "James", "Amina", "Sara"],
    "score": [85, 72, 91, 68],
    "city": ["Nairobi", "Mombasa", "Nairobi", "Kisumu"]
}

df = pd.DataFrame(data)
print(df)
print("\nShape:", df.shape)