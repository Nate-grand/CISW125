# nathan macbeth
# 8/12/25
# Choose-my-adventure

inventory = []
def begin():
    print("""You are a young man conscripted into the Ronaran military to fight in a war with neighboring central nation of Vihar.
           You have been training for battle for less than a week and are being shipped out to the front lines deep in enemy territory to most likely die.
           After engaging in battle for the fist time almost immediatly you are gravely wounded and are left on ground and trampled by both enemys and allies.
           Miraculasly you survived till the end but was unable to move and was left behind deep into enemy lines.
           What should you do now?
           A: You decide to prioritize fixing your wounds nd looks for things to help bind your wounds. 
           B: You decide that its too risky to move around and start yelling for help gambling that whatever person heres you wont kill you.
           C: You decide its too risky to do anything at all and choose to stay there and be quiet.
          """)

    choice = input("Whats do you do now: ")

    match choice.lower():
        case "a":
            print("You choose to try and fix your self up.")
            fix_your_self()
        case "b":
            print("You choose to call for help.")
            call_for_help()
        case "c":
            print("You choose to remain where you are and be quiet.")
            remain_where_you_are()
        case _:
            print("Error")

def fix_your_self():
    print("""You tear off a peice of cloth from a fallen solgier on the ground nearby and use it to close off your wound as much as possible.
          You also find a long spear dropped in the fighting which you use to lean on while you slowly make your way to a nearby forest where you hope to rest a bit.
          After your safely in the forest you find a safe place to get some rest and go to sleep for a while.
          You awake to the sound of crunching leaves and the thump of what sounds like a stick on the ground.
          You sit up from where you are and see an old looking man standing near and looking at you.
          What do you do now?
          a: Ask the old man for help.
          b: Try to run away.
          c: stay silent and wait for him to make the first move.""")
    
    choice = input("Whats do you do now: ")

    match choice.lower():
        case "a":
            print("You choose ask the old man for help.")
            ask_the_old_man_for_help()
        case "b":
            print("You try to run away.")
            try_to_run_away()
        case "c":
            print("You choose to stay silent.")
            stay_silent()
        case _:
            print("Error")

def ask_the_old_man_for_help():
    print("""You ask the old man for help and he decides to take you to his house and tend to your wounds.
         Before you leave he ask you if you want a special potion he made.
         Do you take it or not?""")
    
    choice = input("Do you take it or not?: ")

    match choice.lower():
        case "a":
            print("You take the potion.")
            yes()
        case "b":
            print("You dont take the potion.")
            no()
        case _:
            print("Error")

def yes():
    print("You leave the house with the potion.")
    inventory.append("potion")
    leave()

def no():
    print("You leave the house without the potion.")
    leave()

def leave():
    if "potion" in inventory:
        print("You get curious about the potion and decide to drink it.")

    else:
        print("You wander around the forest and get lost.")

def drink_potion():
    print("""You down the potion in one go hopeing it dosent kill you when you feel something happeneing to your eyes.
          You start seeing a trail of light going through the forest and decide to follow it.
          The trail of light evetually leads you to a cave deep in the woods which you enter.
          After you enter come accross a glowing sword stuck in an alter and have to choose what to do from here.
          What do you do know?
          a: Leave the sword.
          b: Wait and see what it does.
          c: try and take the sword.""")
    
    choice = input("Whats do you do now: ")

    match choice.lower():
        case "a":
            print("You choose to leave the sword glowing things arent good news.")
            leave_the_sword()
        case "b":
            print("You choose to wait and see what it does no harm in being casious.")
            wait_and_see()
        case "c":
            print("You choose to try and take the sword it looks cool.")
            take_the_sword()
        case _:
            print("Error")

def leave_the_sword():
    print("""You leave the cave without the sword and continue through the forest.""")

def wait_and_see():
    print("""You sit down and start watching the sword waiting to see what it will do.""")

def take_the_sword():
    print("""You put both hands on the hilt of the sword and with a bright shine a sliding sound the sword comes free and you feel a powerfull feeling inside you.
          """)
    inventory.append("Glowing sword")

def try_to_run_away():
    print("dgbyuwegdjwniadiw")

def stay_silent():
    print("budiweghioweeyfgnwd")

def call_for_help():
    print("""You start shouting and waiving for help hoping that anyone who sees you wont kill you.
          After a while a group of riders on horseback that looked like scouts survaying with a Viharian symbol the battle ground showed up and approach you.
          After some deliberation the men decide to tie him to one of the horses who they send back to there camp with him on it.
          Your wound is bound but you are also put in cuffs and placed in an area with other prisoners of war, you know good things wont come from staying here.
          What do you do?
          a: Stay where you are.
          b: Try sneaking away.
          C: Attempt a mass break out with your fellow war prisoners.""")
    
    choice = input("Whats do you do now: ")

    match choice.lower():
        case "a":
            print("You decide to do nothing and stay where you are.")
            stay_wher_you_are()
        case "b":
            print("You choose to try sneaking away by yourself.")
            try_sneaking_away()
        case "c":
            print("You choose to try and orchastrate a mass breakout.")
            attempt_a_mass_breakut()
        case _:
            print("Error")

def stay_wher_you_are():
    print("gobblesmock")

def try_sneaking_away():
    print("caravanderfan")

def attempt_a_mass_breakut():
    print("ulusiusesesss")

def remain_where_you_are():
    print("""You decide to remain and not do anything devoid of any will to keep going you lie there in agony for hours even days.
          After what he thought was almost two days you can feel the end coming when your near lifeless body is approach by a group men.
          These men turned out to be Draebanoren slavers who during the central wars had made a habbit of looking for injured left on the battle feild fixing them up then selling them off.
          The slavers take you to a temporary camp and after making sure your condition was no longer fatal began traveling.
          While stopped for the night after two weeks travel you spy a knife that was left out and you succesfully use the knife cut your binds without waking any of the slavers.
          You know have a knife and a choice.
          What should you do?
          a: You take the knife and a few other things and leave as quickly as possible.
          b: You still leave but you also make sure to sabatage the slavers provisions and supplies.
          c: You decide to stab all the slavers to make sure you arent followed and then leave.""")
    
    choice = input("Whats do you do now: ")
    
    match choice.lower():
         case "a":
            print("You choose to leave quickly.")
            leave_quickly()
         case "b":
            print("You choose to sabatoge the slavers before you leave.")
            sabatoge_the_slavers()
         case "c":
            print("You choose to kill the slavers before they can get up and follow you.")
            kill_the_slavers()
         case _:
            print("Error")

def leave_quickly():
    print("fatsfastfsats")

def sabatoge_the_slavers():
    print("sabatagaga")

def kill_the_slavers():
    print("murdkiljeijs")



begin()








# myinput = input("Whats your favorite letter: ")

# match myinput.lower():
    # case "a":
        # print("Choose your own adventure")
    # case "b":
        # print("Lame letter")
    # case _:
        # print("Thats lame")