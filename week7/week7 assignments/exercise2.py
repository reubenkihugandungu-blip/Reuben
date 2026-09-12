# Make predictions

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
import numpy as np

X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)
model = DecisionTreeClassifier().fit(X_train, y_train)
new_sample = np.array([[5.1, 3.5, 1.4, 0.2]])
pred = model.predict(new_sample)
names = load_iris().target_names
print(f"Predicted class: {names[pred[0]]}")