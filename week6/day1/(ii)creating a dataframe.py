# What is a DataFrame
# A DataFrame is a two-dimensional data structure with labeled rows and columns. 
# Think of it as a Python spreadsheet. Each column is a Series (a labeled list).
#  Each row is one record. You can filter, sort, group, compute, and reshape the whole table in a single line.

import pandas as pd

data = {
    "day": ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"],
    "steps": [9200, 10500, 8800, 11000, 7600, 9400, 10200],
    "sleep_hr": [7.5, 8.0, 6.5, 7.0, 9.0, 7.5, 8.0],
    "protocol": ["OMAD", '2MAD', "OMAD", "OMAD", "2MAD", "OMAD", "OMAD"],
    "cold_shower": [True, True, False, True, True, True, True]
}

df = pd.DataFrame(data)
print(df.to_string())