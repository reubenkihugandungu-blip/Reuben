# Machine learning is not magic. It is a method: show the model examples, let it find the pattern, 
# then ask it to apply that pattern to new data. scikit-learn is the standard library for doing this in Python. 
# This lesson shows you the workflow from data to trained model to prediction.

# Machine learning is training a program to make predictions by showing it examples, rather than writing explicit rules.
#  You provide labeled data: inputs with known correct outputs. 
# The model finds the mathematical relationship. Then it applies that relationship to inputs it has never seen before.

# Think of a personal trainer learning your body.
# You show up every day with data: how many hours you slept, how much you ate, what your energy is. Over weeks, 
# the trainer notices: when you sleep under 7 hours, your bench press drops 5kg. When you are in an OMAD deficit,
#  your steps are lower on day 3. The trainer did not write these rules. They observed the pattern.
#  That is what a machine learning model does with data.

# Type	         What It Does	      Known Example
# Supervised     (regression)	     Predicts a number	Predict bench press from sleep + steps
# Supervised    (classification)	 Predicts a category	Predict OMAD vs 2MAD from daily metrics
# Unsupervised    (clustering)	     Groups similar records	Group members by training style
