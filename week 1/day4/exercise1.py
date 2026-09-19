# Write a program that takes a score and prints a grade
# 90+ = A, 75+ = B, 60+ = C, below 60 = F
score = 78

if score >= 90:
    print("A")
elif score >= 75:
    print("B")
elif score >= 60:
    print("C")
else:
    print("Below 60. Fail.")