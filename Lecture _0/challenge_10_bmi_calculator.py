# Challenge 10 - BMI Calculator
# Goal: Calculate BMI using a dedicated function

def calculate_bmi(weight, height):
    return weight / height ** 2

weight = float(input("Enter your weight (kg): "))
height = float(input("Enter your height (m): "))
bmi_index = calculate_bmi(weight, height)
print(f"Your BMI is: {bmi_index:.1f}")
