import random

def dice_roller():
    while True:

        roll_input = input("Roll the dice? (yes/no): ").strip().lower()

        if roll_input == 'yes':
                result = random.randint(1, 6)
                print(f"You rolled a {result}")
        elif roll_input == 'no':
                break
        else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

if __name__ == "__main__":
    dice_roller()