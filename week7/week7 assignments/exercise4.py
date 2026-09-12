# CHALLENGE

# trains a logistic regression model to classify breast tumors as either benign or malignant

from sklearn.datasets import load_breast_cancer 
# load_breast-cancer function from scikit-learn
# this function provides a dataset containing measurements of breast tumors
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# X contains measurements about each tumor
# y contains the correct classification for each tumor
# return_X_y returns the measurements and labels separately
# labels represent two classes 0: malignant 1:benign 

X, y = load_breast_cancer(return_X_y=True)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=0)

# logisticRegression() creates the model
# max_iter=10000 allows the model upto 10,000 training iterations
# Larger iteration limit helps the model finish training successfully

model = LogisticRegression(max_iter=10000).fit(X_train, y_train)
acc = accuracy_score(y_test, model.predict(X_test))
print(f"Breast cancer classifier accuracy: {acc:.2%}")