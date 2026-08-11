# Daily discipline grader

steps = 7500
sleep_hours = 6
water_glasses = 5
cold_shower = False
pages_read = 15

if steps > 10000:
    steps_grade = "excellent"
elif steps > 7500:
    steps_grade = "good"
else:
    steps_grade = "needs work"

if sleep_hours >= 7:
    sleep_grade = "good"
else:
    sleep_grade = "low"

if water_glasses >= 8:
    water_grade = "good"
else:
    water_grade = "low"

if cold_shower:
    cold_shower_grade = "completed"
else:
    cold_shower_grade = "skipped"

if pages_read >= 10:
    pages_grade = "good"
else:
    pages_grade = "low"

print(" == Daily Discipline Report == ")
print(f"Steps: {steps_grade}")
print(f"Sleep: {sleep_grade}")
print(f"Water: {water_grade}")
print(f"Cold shower: {cold_shower_grade}")
print(f"Pages read: {pages_grade}")

if steps_grade == "excellent" and sleep_grade == "good" and water_grade == "good" and cold_shower_grade == "completed" and pages_grade == "good":
    final_verdict = "Excellent discipline day!"
elif steps_grade == "good" and sleep_grade == "good" and water_grade == "good" and pages_grade == "good":
    final_verdict = "Solid discipline day!"
else:
    final_verdict = "Needs more consistency."

print(f"Final verdict: {final_verdict}")
