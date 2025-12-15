# nathan macbeth
# 12/12/25
# Project2 - Caculator

print("Calculator Program")

first_number = int(input("First number?: "))

operation = input("Operation? (+ - * / 2 R)?: ")

if operation in ("+", "-", "*", "/"):
    second_number = int(input("second number?: "))
    if operation == "+":
        result = first_number + second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    elif operation == "-":
        result = first_number - second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    elif operation == "*":
        result = first_number * second_number
        print(f"{first_number} {operation} {second_number} = {result}")
    elif operation == "/":
        result = first_number / second_number
        print(f"{first_number} {operation} {second_number} = {result}")

if operation in ("2", "R"):
    if operation == "2":
        result = first_number ** 2
        print(f"{operation} {first_number} = {result}")
    elif operation == "R":
        result = first_number ** 0.5
        print(f"{operation} {first_number} = {result}")
