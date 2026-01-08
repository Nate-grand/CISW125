# nathan macbeth
# 5/1/26
# Project 3 - Rock paper scissors

ask_user = input("Do you want to play rock, paper, scissors? (yes/no): ").lower()
while ask_user == "yes":
    import random

    user_choice = input("Enter rock, paper, or scissors: ").lower()
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    print(f"computer chose: {computer_choice}")
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == "rock" and computer_choice == "scissors") or \
                (user_choice == "paper" and computer_choice == "rock") or \
                (user_choice == "scissors" and computer_choice == "paper"):
        print("You win!")
    else:
        print("Computer wins!")
        ask_user = input("Do you want to play again? (yes/no): ").lower()
        if ask_user == "Yes":
            continue
        elif ask_user == "no":
            break
