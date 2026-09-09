# A model that scores 90% accuracy sounds impressive until you learn that 90% of the data was in one class anyway.
#  Evaluation is about understanding what a score actually means. 
# This lesson covers the metrics that tell you whether your model is genuinely working or just guessing the majority class.

# Evaluation measures how well a model generalizes to data it has never seen. 
# You train on one portion of the data and test on the rest. 
# A model that only memorizes training examples (overfits) will score high on training data and poorly on test data. 
# Evaluation catches this.

# Think of a driving test.
# You practice on known roads (training data). The examiner takes you to roads you have never driven (test data).
#  If you only memorized one route, you fail on the new roads.
# The test is designed to measure whether you can actually drive, not whether you remembered a specific route. 
# Train/test split works the same way.