# Classification predicts a category or class like goal hit, below goal
# Use a Random Forest classifier to predict whether a day will hit the 10,000 step goal based on sleep and water intake.

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

X = np.array([
    [7.5,7],[8.0,8],[6.5,6],[7.0,9],[9.0,8],[7.5,7],[8.0,8],
    [6.0,6],[8.5,9],[7.0,8],[7.5,8],[9.0,7],[7.0,9],[7.5,8],
    [7.0,7],[8.0,8],[6.5,6],[7.5,9],[8.0,8],[7.0,7],[8.5,9],
    [7.0,8],[7.5,8],[6.5,6],[8.0,9],[9.5,7],[7.0,8],[8.0,9]
    ])
steps = np.array([
    9200,10500,8800,11000,7600,9400,10200,
    8900,10800,9100,11200,7900,10000,9700,
    9500,10300,8600,11500,8200,9800,10600,
    9000,10100,8400,10900,7500,9600,10400
    ])

# Convert step counts to binary labels: 1 = hit goal, 0 = missed
# If step count is 10000 or more it becomes 1 else becomes 0
# .astype(int) converts True/False to integer values. True becomes 1, False becomes 0
y = (steps >= 10000).astype(int)
print("Label distribution (1=hit goal, 0=missed):")
print(f" Hit goal: {y.sum()}/28 days")
print(f" Missed:  {(y==0).sum()}/28 days")

# Split data
# x_train trainining features
# y_train training labels
# n_estimators=10 - use 10 decision trees
# random_state=42 keeps the model result consistent

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=10, random_state=42)

# Train the model
# the model learns from the training data sleep,water or whether the goal was hit or missed
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test) # Tests how accurate the model is on the test data
print(f"\nClassification accuracy: {accuracy:.0%}") # P accuracy as %tage

# Predict new days
new_days = np.array([[8.0, 8], [6.0, 5], [9.0, 9]]) # this creates 3 new examples
preds = clf.predict(new_days) # Uses the trained model to predict the class/category for each new day
labels = {1: "Goal hit", 0: "Below goal"} # creates a dict mapping (1-Goal hit)(0-Below goal)
print("\nPredictions for new days:")
for inputs, pred in zip(new_days, preds): # loops through each new day and its prediction
    print(f" Sleep={inputs[0]}h, Water={int(inputs[1])}g => {labels[pred]} ")

# This code:

# uses sleep and water as features,
# converts step count into binary labels,
# trains a Random Forest classifier,
# checks accuracy,
# then predicts whether a new day will hit or miss the step goal.
# The biggest thing to notice is that this is classification because the answer is not a number like 10,200.
#  It is a category: 1 = goal hit, 0 = below goal.