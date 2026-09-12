# Code Challenge 1 — Project Delivery Risk

# A construction contractor wants to know if a project will finish on time. 
# Write a function called predict_delivery_risk that takes three parameters: crew_size, days_remaining, and tasks_left. 
# Apply this logic:

# Calculate efficiency = tasks_left / (crew_size * days_remaining)
# If efficiency is above 1.5: return "High risk"
# If efficiency is above 0.8: return "Medium risk"
# Otherwise: return "Low risk"

# Use these calls in this order: predict_delivery_risk(3, 5, 25), predict_delivery_risk(4, 10, 18),
#  predict_delivery_risk(2, 4, 8)

def predict_delivery_risk(crew_size, days_remaining, tasks_left):
	efficiency = tasks_left / (crew_size * days_remaining)
	if efficiency > 1.5:
		return "High risk"
	if efficiency > 0.8:
		return "Medium risk"
	return "Low risk"


print(predict_delivery_risk(3, 5, 25))
print(predict_delivery_risk(4, 10, 18))
print(predict_delivery_risk(2, 4, 8))
