# nathan macbeth
# 8/12/25
# Choose-my-adventure

inventory = []
def begin():
    print("""You are a young man conscripted into the Ronaran military to fight in a war with neighboring central nation of Vihar.
           You have been training for battle for less than a week and are being shipped out to the front lines deep in enemy territory to most likely die.
           After engaging in battle for the fist time almost immediatly you are gravely wounded and are left on ground and trampled by both enemys and allies. Miraculasly you survived till the end but was unable to move and was left behind deep into enemy lines.
           What should you do now? A: You decide to prioritize fixing your wounds nd looks for things to help bind your wounds. B: You decide that its too risky to move around and start yelling for help gambling that whatever person heres you wont kill you.
           C: You decide its too risky to do anything at all and choose to stay there and be quiet.
          """)

    choice = input("Whats do you do now: ")

    match choice.lower():
        case "a":
            print("You choose to try and fix your self up")
        case "b":
            print("You choose to call for help")
        case "c":
            print("You choose to remain where you are and be quiet")

def Fix_your_self():
    print("""cythvtydrgh""")

begin()








# myinput = input("Whats your favorite letter: ")

# match myinput.lower():
    # case "a":
        # print("Choose your own adventure")
    # case "b":
        # print("Lame letter")
    # case _:
        # print("Thats lame")