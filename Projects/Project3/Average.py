# nathan macbeth
# 12/1/26
# Project 3 - Average of numbers

def calculate_average():
    numbers = []
    while True:
        user_input = input("Enter a number (or 'done' to finish): ")
        if user_input.lower() == 'done':
            break
        try:
            numbers.append(float(user_input))
        except ValueError:
            print("Invalid input. Please enter a number or 'done'.")
    if numbers:
        average = sum(numbers) / len(numbers)
        print(f"The average is: {average}")
    else:
        print("No numbers were entered.")

calculate_average()