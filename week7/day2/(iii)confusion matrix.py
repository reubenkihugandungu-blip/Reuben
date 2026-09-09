# A confusion matrix shows the count of correct and incorrect predictions, broken down by class.
#  Rows are actual labels; columns are predicted labels.
#  The diagonal is correct predictions. Off-diagonal entries are errors.

# BUILD AND READ A CONFUSION MATRIX

import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix # imports the function used to compare actual predictions with model predictions

X = np.array([
              [7.5,7,80],[8.0,8,82],[6.5,6,78],[7.0,9,85],[9.0,8,80],[7.5,7,83],[8.0,8,84],
              [6.0,6,81],[8.5,9,85],[7.0,8,80],[7.5,8,86],[9.0,7,79],[7.0,9,84],[7.5,8,83],
              [7.0,7,82],[8.0,8,86],[6.5,6,79],[7.5,9,88],[8.0,8,81],[7.0,7,85],[8.5,9,87],
              [7.0,8,82],[7.5,8,86],[6.5,6,80],[8.0,9,87],[9.5,7,79],[7.0,8,84],[8.0,9,86]
              ])
steps = np.array([
                  9200,10500,8800,11000,7600,9400,10200,
                  8900,10800,9100,11200,7900,10000,9700,
                  9500,10300,8600,11500,8200,9800,10600,
                  9000,10100,8400,10900,7500,9600,10400
                  ])
y = (steps >= 10000).astype(int)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=42)
clf = RandomForestClassifier(n_estimators=20, random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

# creates the confusion matrix by comparing y_test(the actual answers), y_pred the model's answers
cm = confusion_matrix(y_test, y_pred)
print("Confusion matrix:")

print(f"                Predicted Below Predicted Hit")
print(f"Actual Below    {cm[0][0]:>14} {cm[0][1]:>14}")
print(f"Actual Hit      {cm[1][0]:>14} {cm[1][1]:>14}")
print()
print(f"True Negatives (correct 'Below'):   {cm[0][0]}")
print(f"False Positives (Wrong 'Hit'):      {cm[0][1]}")
print(f"False Negatives (missed 'Hit'):     {cm[1][0]}")
print(f"True Positives  (correct 'Hit'):    {cm[1][1]}")
