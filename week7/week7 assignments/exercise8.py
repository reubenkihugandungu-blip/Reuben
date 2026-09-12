# Code Challenge 2 — The Simp Detector
# A man has been trying to impress a woman for weeks. 
# He tracked his spending, how many texts he sent, how many she replied to, how many times he asked her out, 
# and how many times she said yes.

# Write a function called simp_alert that takes five parameters:
#  money_spent, texts_sent, texts_replied, dates_asked, dates_accepted.
#  Apply this logic:
# Calculate reply_rate = texts_replied / texts_sent
# Calculate date_rate = dates_accepted / dates_asked
# Calculate score = (reply_rate + date_rate) / 2
# If score is 0.5 or above: return "She likes you"
# If score is 0.2 or above: return "Lukewarm"
# Otherwise: return "You are simping"

# Use these calls in this order:

# simp_alert(45000, 80, 2, 10, 0)
# simp_alert(8000, 20, 15, 4, 2)
# simp_alert(18000, 20, 6, 5, 1)

def simp_alert(money_spent, texts_sent, texts_replied, dates_asked, dates_accepted):
	reply_rate = texts_replied / texts_sent
	date_rate = dates_accepted / dates_asked
	score = (reply_rate + date_rate) / 2
	if score >= 0.5:
		return "She likes you"
	if score >= 0.2:
		return "Lukewarm"
	return "You are simping & dust is inevitable"

print(simp_alert(45000, 80, 2, 10, 0))
print(simp_alert(8000, 20, 15, 4, 2))
print(simp_alert(18000, 20, 6, 5, 1))