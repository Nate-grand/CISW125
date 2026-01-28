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
    with open("CISW125\In class work\hangmangame\Hangman Bugfix\wordlist.txt", "r") as file:
        word_list = file.read().split()#8#is it splitlines or split?...
    return random.choice(word_list)#3

def displayword(word, guessed_letters):
    
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter#4
        else:
            display_word += "_"
    return display_word

def hangman():
    word = choose_word()
    guessed_letters = []
    tries = 6

    while tries > 0:
        display_word = displayword(word, guessed_letters)#5
        print(display_word)
        print(f"Guessed letters: {', '.join(guessed_letters)}")
        print(f"Tries left: {tries}")
        #print("You already guessed that letter.")#6
        print(word)
        if display_word == word:
                print(f"Congratulations! You guessed the word: {word}")
                break
        guess = input("Guess a letter: ").lower()

        if guess in guessed_letters:
            print("You already guessed that letter.")
        elif guess == word:#9
            print(f"Congratulations! You guessed the word: {word} correctly!")#7
            break

        elif guess in word:
            guessed_letters.append(guess)
            
        else:
            guessed_letters.append(guess)
            tries -= 1#11
            if tries <= 0:#12
                print("You're out of tries. The word was: " + word)
                break
    #print("You lost. The word was: " + "randomword.")#10

print("Welcome to my Hangman Game!")
print("You have 6 tries to win the game!")
print("Good luck.")
time.sleep(3)
hangman()
