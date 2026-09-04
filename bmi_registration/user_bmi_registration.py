"""
User Registration & BMI Calculator
------------------------------------
A simple command-line program that:
- Collects a user's name, hometown, age, and password (with input validation)
- Calculates BMI from weight and height
- Saves the results to a CSV file

Author: Rebbman
"""

import getpass
import csv
import os

CSV_FILE = "users.csv"

# ...rest of your code stays exactly the same below
import getpass
import csv
import os

CSV_FILE = "users.csv"

def get_name(prompt):
    while True:
        value = input(prompt)
        if value.strip().replace(" ", "").isalpha():
            return value.strip()
        else:
            print("⚠️  Please enter letters only (no numbers), try again.")

def get_age(prompt):
    while True:
        value = input(prompt)
        try:
            age = int(value)
            if age <= 0 or age > 120:
                print("⚠️  Please enter a realistic age.")
                continue
            return age
        except ValueError:
            print("⚠️  That's not a number. Please enter your age using digits (e.g. 25).")

def get_positive_number(prompt):
    while True:
        value = input(prompt)
        try:
            number = float(value)
            if number <= 0:
                print("⚠️  Please enter a number greater than 0.")
                continue
            return number
        except ValueError:
            print("⚠️  That's not a valid number. Try again.")

def get_password(prompt):
    while True:
        pw = getpass.getpass(prompt)
        if len(pw) < 4:
            print("⚠️  Password too short. Use at least 4 characters.")
        else:
            return pw

def calculate_bmi(weight_kg, height_m):
    return weight_kg / (height_m ** 2)

def bmi_category(bmi):
    if bmi < 18.5:
        return "Underweight"
    elif bmi < 25:
        return "Normal weight"
    elif bmi < 30:
        return "Overweight"
    else:
        return "Obese"

def save_to_csv(name, hometown, age, bmi, category):
    file_exists = os.path.exists(CSV_FILE)

    with open(CSV_FILE, mode="a", newline="") as f:
        writer = csv.writer(f)

        # Write the header row only if the file is brand new
        if not file_exists:
            writer.writerow(["Name", "Hometown", "Age", "BMI", "Category"])

        writer.writerow([name, hometown, age, f"{bmi:.2f}", category])

def main():
    print("=== User Registration ===")
    name = get_name("Enter your name: ")
    hometown = get_name("Where are you from? ")
    age = get_age("Enter your age: ")
    password = get_password("Create a password: ")  # kept in memory only, never saved

    print("\n=== BMI Calculator ===")
    weight = get_positive_number("Enter your weight in kg: ")
    height = get_positive_number("Enter your height in meters (e.g. 1.7): ")

    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)

    print("\n=== Summary ===")
    print(f"Name: {name}")
    print(f"From: {hometown}")
    print(f"Age: {age}")
    print(f"Your BMI is {bmi:.2f} ({category})")

    save_to_csv(name, hometown, age, bmi, category)
    print(f"\n✅ Saved to {CSV_FILE}")

if __name__ == "__main__":
    main()