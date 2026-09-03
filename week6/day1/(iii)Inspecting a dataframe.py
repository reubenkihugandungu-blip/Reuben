# Before analyzing any dataset, inspect it. These four commands tell you what you are working with.

import pandas as pd

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", '2MAD', "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data) # Converts the dictionary into a dataframe

print("Shape (rows, cols):", df.shape)
print("\nColumns:", list(df.columns)) # df.columns is an index of column names, so we convert it to a list for better readability
print("\nData types:")
print(df.dtypes)
print("\nFirst 3 rows:") # Print a header before showing the first 3 rows of the dataframe
print(df.head(3).to_string()) # head(3) selects the first 3 rows of the dataframe, and to_string() prints them in a readable format
