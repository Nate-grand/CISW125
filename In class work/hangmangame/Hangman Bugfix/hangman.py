import random #1
import time#2
#
#
#
#
#
#
#There are currently several (12) problems with this program. Some are "Logic problems" and some are random.
#These problems can range from code, to typos, to strings/input errors.
#Add all of your names to this program as a comment before one of your uploads.
def choose_word():
    with open("word_list.txt", "r") as file:
        word_list = file.read().splitlines() #is it splitlines or split?...
    return random.choice(word_list + "randomword")

def displayword(word, guessed_letters):
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += random.choice("abcdefghijklmnopqrstuvwxyz")
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        display_word = displayword()
        print(display_word)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Tries left: {tries}")
        print("You already guessed that letter.")

        if display_word == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess == "word":
            print(f"Congratulations! You guessed the word: {word} incorrectly!")
            
        elif guess in word:
            guessed_letters.append(guess)
            
        else:
            guessed_letters.append(guess)
            tries -= 2
            if tries > 0:
                print("You're out of tries. The word was: " + word)
                break
    print("You lost. The word was: " + "randomword.")

print("Welcome to my Hangman Game!")
print("You have 6 tries to win the game!")
print("Good luck.")
time.sleep(3)
hangman()
