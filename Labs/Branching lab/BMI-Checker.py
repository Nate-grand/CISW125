# nathan macbeth
# 11/12/25
# Branching lab - BMI-Checker

weight = float(input("Input weight: "))
height = float(input("Input height: "))

bmi = weight / (height ** 2)

print(f"Your BMI is: {bmi:.2f}")

if bmi < 18.5:
    print("Your underweight.")
elif 18.5 <= bmi and bmi < 25:
    print("You have a healthy weight.")
elif 25 <= bmi and bmi < 30:
    print("Your overweight.")
else:
    print("Your Obese.")