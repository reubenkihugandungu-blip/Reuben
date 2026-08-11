def calculate_bmi(weight_kg, height_m): # defines a function called calculate_bmi that takes two parameters: weight_kg and height_m.
    bmi = weight_kg / (height_m ** 2)
    return round(bmi, 1)# rounds the BMI value to one decimal place and returns it.

def bmi_category(bmi): # defines a second function called bmi_category that takes one parameter: bmi.
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

weight = 84
height = 1.78
bmi = calculate_bmi(weight, height)# calls the calculate_bmi function with the weight and height values, and stores the returned BMI value in the variable bmi.
category = bmi_category(bmi)# calls the bmi_category function with the calculated BMI value, and stores the returned category in the variable category.

print(f"Weight: {weight}kg | Height: {height}m")
print(f"BMI: {bmi} | Category: {category}") # prints the calculated bmi and its corresponding category to the console.
# 