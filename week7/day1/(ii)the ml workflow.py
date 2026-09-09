# Every scikit-learn project follows the same five steps. 
# Prepare data. 
# Split into train/test.
# Create the model object.
# Fit (train) it on training data. 
# Evaluate on test data.

# STEP-BY-STEP ML WORKFLOW

import numpy as np # NumPy creates and manages the numerical arrays used by the model
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split # Imports the function that separates data into training and testing portions

# Step 1: Data (28 days of SMP fitness log)
# Features: sleep hours, water glasses
# Label: The value the model predicts, called the label or target, is daily steps.
X = np.array([
    [7.5, 7], [8.0, 8], [6.5, 6], [7.0, 9], [9.0, 8], [7.5, 7], [8.0, 8],
    [6.0, 6], [8.5, 9], [7.0, 8], [7.5, 8], [9.0, 7], [7.0, 9], [7.5, 8],
    [7.0, 7], [8.0, 8], [6.5, 6], [7.5, 9], [8.0, 8], [7.0, 7], [8.5, 9],
    [7.0, 8], [7.5, 8], [6.5, 6], [8.0, 9], [9.5, 7], [7.0, 8], [8.0, 9]
]) 
# shape: (28, 2) - 28 days, 2 features per day
# 👇Creates the target array named y
y = np.array([
    9200, 10500, 8800, 11000, 7600, 9400, 10200,
    8900, 10800, 9100, 11200, 7900, 10000, 9700,
    9500, 10300, 8600, 11500, 8200, 9800, 10600,
    9000, 10100, 8400, 10900, 7500, 9600, 10400
])  # shape: (28,) - one step count per day

print(f"Features shape: {X.shape}") # prints the input/features data
print(f"Labels shape:   {y.shape}")

# Step 2: Split into training and test sets
# X_train: input features used for training
# X_test: input features used for testing
# y_train: correct answers for training rows
# Y_test: correct answers for the testing rows
# test_size=0.2 keeps 20% of the data for testing and uses 80% for training
# with rows appro 22 rows are used for training, 6 rows are used for testing
# random_state=42 makes the script repeatable. the same rows go into training and testing everytime the script runs
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
print(f"\nTraining rows: {X_train.shape[0]}") # prints how many samples are in the training set
print(f"Test rows:     {X_test.shape[0]}") # prints how many samples are in the test set

# Step 3: Create and train the model
model = LinearRegression() # creates a linear regression model object
model.fit(X_train, y_train) # trains the model using the training data. learns the rship btwn sleep, water & step count

# Step 4: Evaluate
score = model.score(X_test, y_test) # tests how well the model predicts the test data
print(f"\nModel R2 score: {score:.3f}") # prints the model accuracy score with 3 decimal places
print("(1.0 = perfect, 0 = no better than guessing the mean)") # 1.0 perfect prediction