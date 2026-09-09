# Once trained, the model can predict step counts for days it has never seen,
# given sleep hours and water intake.

import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

# 👇 x = np.array([...]) creates the dataset of features
# Each row contains 2 values: sleep hours, water glasses
# y = np.array([...]) this is the target (what we want to predict)
X = np.array([
              [7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],
              [6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],
              [7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],
              [7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]
              ])
y = np.array([
              9200,10500,8800,11000,7600,9400,10200,
              8900,10800,9100,11200,7900,10000,9700,
              9500,10300,8600,11500,8200,9800,10600,
              9000,10100,8400,10900,7500,9600,10400
              ])

# 👇 This splits the data into
# x_train training features
# x_test test features
# y_training target
# y_test target
# test_size= 0.2 means 20% of the data is kept for testing
# random_state=42 makes the split the same every time
# model = linearRegression()creates a linear regression model
# This is the machine learning algorithm that will learn the pattern
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
model = LinearRegression()
model.fit(X_train, y_train) # trains the model using the training data, the model learns the relationship btwn sleep/water and predicted steps

# Predict for new days not in the training data
new_days = np.array([
    [8.0, 8],   # 8 hours sleep, 8 glasses water
    [6.0, 5],   # 6 hours sleep, 5 glasses water
    [9.0, 9],   # 9 hours sleep, 9 glasses water
    [7.5, 7],   # typical day
])

# 👇 Uses the trained model to predict step counts for all the new days
# it returns an array of predicted values
predictions = model.predict(new_days)
print("Predictions for new days:")

# starts a loop
# zip(new_days, predictions) pairs each input day with its matching prediction
# enumerate(..) gives each pair a number index, so it will be the first day, the the second day and so on
# sleep, water = inputs Unpacks the two values from one row of new_days ex inputs = [8.0, 8], sleep = 8, water = 8
for i, (inputs, pred) in enumerate(zip(new_days, predictions)):
    sleep, water = inputs 
    print(f"  Sleep={sleep}h, Water={water}g => predicted steps: {pred:,.0f}")

# ☝️ prints each result in a redable format 
# {pred:,.0f} prints the prediction as a whole number with commas