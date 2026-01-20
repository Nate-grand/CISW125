# nathan macbeth
# 20/1/26
# Functions Lab


def greet_user(name):
    print(f"Hello, {name}! Welcome to the Functions Lab.")

user_name = input("please enter your name: ")

greet_user(user_name)

def function_calc(num1, num2):

    num1 = int(input("Enter the first number: "))

    num2 = int(input("Enter the second number: "))

    operation = input("Enter the operation you want to perform (+, -, *, /): ")

    if operation == '+':
        result = num1 + num2
    elif operation == '-':
            result = num1 - num2
    elif operation == '*':
            result = num1 * num2
    elif operation == '/':
            if num2 != 0:
                result = num1 / num2
            else:
                return "Error: Division by zero is not allowed."
            
    else:
            return "Error: Invalid operation."
    return result

print(f"Result: {function_calc(10,5)}")

while True:
    choice = input("would you like to play again? (yes/no): ").lower()

    if choice == "yes":
        print(f"Result: {function_calc(10, 5)}")
    
    elif choice == "no":
        print("Thank you for using the Functions Lab. Goodbye!")
        break
    
    else:
        print("Invalid entry. Please type 'yes' or 'no'.")


