# Retraining every time is wasteful. Save the trained model to a file with joblib.dump(). 
# Load it back later with joblib.load(). The loaded model works identically to the trained one.

# In VS Code: save the model
import joblib
from sklearn.ensemble import RandomForestClassifier

# (after training clf)
joblib.dump(clf, "step_goal_model.joblib")
print("Model saved.")


# In VS Code: load and use
import joblib
import numpy as np

clf = joblib.load("step_goal_model.joblib")

# Predict without retraining
new_day = np.array([[8.0, 8, 84]])
pred = clf.predict(new_day)[0]
print("Prediction:", "Goal hit" if pred == 1 else "Below goal")