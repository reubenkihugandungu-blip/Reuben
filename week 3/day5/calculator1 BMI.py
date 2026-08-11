# Takes weight in kg and height in metres. Returns BMI rounded to one decimal place.

import math

def calculate_bmi(weight_kg, height_m):
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"
#Test
weight = 64
height = 1.59
bmi = calculate_bmi(weight, height)
print(f"Weight : {weight} kg")
print(f"Height : {height} m")
print(f" BMI  : {bmi}")
print(f"Status : {bmi_category(bmi)}")