# FEATURE IMPORTANCE

from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split

# X contains the four flower measurements
# y contains the correct species labels (Sepal length, petal length etc)
# return_X_y=True means the function returns the data and labels directly instead of a dataset object
X, y = load_iris(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y)
model = DecisionTreeClassifier().fit(X_train, y_train)
features = load_iris().feature_names # loads the readable names of the 4 measurements

# 👇loops through two lists at the same time
# features: measurement names
# model.feature_importances_: importance value for each measurement
# zip() pairs them together,
# name: feature name
# imp: its importance value
# {imp:.3f} displays the importance rounded to 3 decimal places
for name, imp in zip(features, model.feature_importances_):
    print(f"{name}: {imp:.3f}")

# What feature importance means
# Feature importance shows how much each measurement helped the decision tree classify the flowers.

# For example, if petal length has an importance of 0.600,
#  it contributed more to the tree's decisions than a feature with an importance of 0.020.

# For the Iris dataset, petal length and petal width are often the most important features.