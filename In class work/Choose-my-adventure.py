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

    choice = input("What do you do now: ")

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
          b: Try to run away.""")
    
    choice = input("What do you do now: ")

    match choice.lower():
        case "a":
            print("You choose ask the old man for help.")
            ask_the_old_man_for_help()
        case "b":
            print("You try to run away.")
            try_to_run_away()
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
        drink_potion()

    else:
        print("You wander around the forest and get lost.")

def drink_potion():
    print("""You down the potion in one go hopeing it dosent kill you when you feel something happeneing to your eyes.
          You start seeing a trail of light going through the forest and decide to follow it.
          The trail of light evetually leads you to a cave deep in the woods which you enter.
          After you enter come accross a glowing sword stuck in an alter and have to choose what to do from here.
          What do you do know?
          a: Leave the sword.
          b: try and take the sword.""")
    
    choice = input("What do you do now: ")

    match choice.lower():
        case "a":
            print("You choose to leave the sword glowing things arent good news.")
            leave_the_sword()
        case "b":
            print("You choose to try and take the sword it looks cool.")
            take_the_sword()
        case _:
            print("Error")

def leave_the_sword():
    print("""You leave the cave without the sword and continue through the forest.""")
    pulll_the_sword()

def take_the_sword():
    print("""You put both hands on the hilt of the sword and with a bright shine a sliding sound the sword comes free and you feel a powerfull feeling inside you.""")
    inventory.append("Glowing sword")
    pulll_the_sword()

def pulll_the_sword():
    if "Glowing sword" in inventory:
        print("""You suddenly feel dragon wings sprout from your back and realize the sword did this.
              You exit the cave and fly into the sky determmined to get back to your home town now.""")

    else:
        print("You leave the cave and wander through the woods till you are completly lost.")

def try_to_run_away():
    print("""You quickly stagger up and start hobbling away as fast as you can worried he might be dangerous.
          Before you get too far away the old man tosses a rolled up map at you and then walks away.
          what do you do now?
          a: Dont pick it up.
          b: Pick it up.""")
    
    choice = input("What do you do now: ")

    match choice.lower():
        case "a":
            print("You choose to leave it.")
            keep_running()
        case "b":
            print("You choose to pick it up.")
            inventory.append("Map")
            keep_running()
        case _:
            print("Error")
    
def keep_running():
    print("""You keep running till you stumble accross a cave and upon entering you find a normal sword in an alter.
          You think about pulling it.
          What do you do now?
          a: Dont pull the sword.
          b: Pull the sword.""")
        
    choice = input("What do you do now: ")
    
    match choice.lower():
        case "a":
            print("You choose not take the sword.")
            second_leave_sword()
        case "b":
            print("You choose to try and take the sword.")
            second_take_sword()
        case _:
            print("Error")

def second_leave_sword():
    print("""You leave the cave without the sword and continue through the forest.""")

def second_take_sword():
    print("""You put both hands on the hilt of the sword and slowly pull the sword free and something starts to happen.""")
    pulll_the_sword()

def pulll_the_sword():
    if "Map" in inventory:
        print("""The sword all of a sudden stops being pulled and you get a strong feeling that you should look at the map that the old man gave you.
              You open it and see it as a map to his house and decide to go to it to get answers.""")
        follow_map()

    else:
        print("You try to pull the sword but when tyr to pull it all the way out a strong shock comes out of it and knocks you out cold.")

def follow_map():
    print("""You slowly follow the map and make your way to the old mans house asking what the sword was.
          The old man tells you to take a potion if and go back if you want to know what it is.
         Do you take it or not?""")
    
    choice = input("Do you take it or not?: ")

    match choice.lower():
        case "a":
            print("You take the potion.")
            yes2()
        case "b":
            print("You dont take the potion.")
            no2()
        case _:
            print("Error")

def yes2():
    print("You leave the house with the potion.")
    inventory.append("potion")
    leave2()

def no2():
    print("You leave the house without the potion.")
    leave2()

def leave2():
    if "potion" in inventory:
        print("Once your a ways from the house you decide to drink the potion.")
        drink_potion2()

    else:
        print("You try to find the cave again but end up getting lost inn the forest.")

def drink_potion2():
    print("""You drink the potion and somethhing satarts happening to your eyes.
          A light trail of light appears going off in the directsion you think the cave is.
          You make it to the cave and you see the sword is now glowing.
          What do you do know?
          a: Leave the sword.
          b: try and take the sword.""")
    
    choice = input("What do you do now: ")

    match choice.lower():
        case "a":
            print("You choose to leave the sword glowing things arent good news.")
            leave_the_sword2()
        case "b":
            print("You choose to try and take the sword it looks cool.")
            take_the_sword2()
        case _:
            print("Error")

def leave_the_sword2():
    print("""You leave the cave without the sword and continue through the forest.""")
    pulll_the_sword()

def take_the_sword2():
    print("""You put both hands on the hilt of the sword and with a bright shine a sliding sound the sword comes free and you feel a powerfull feeling inside you.""")
    inventory.append("Glowing sword")
    pulll_the_sword2()

def pulll_the_sword2():
    if "Glowing sword" in inventory:
        print("""You suddenly feel dragon wings sprout from your back and realize the sword did this.
              You exit the cave and fly into the sky determmined to get back to your home town now.""")

    else:
        print("You leave the cave and wander through the woods till you are completly lost.")

def call_for_help():
    print("""You start shouting and waiving for help hoping that anyone who sees you wont kill you.
          After a while a group of riders on horseback that looked like scouts survaying with a Viharian symbol the battle ground showed up and approach you.
          After some deliberation the men decide to tie him to one of the horses who they send back to there camp with him on it.
          Your wound is bound but you are also put in cuffs and placed in an area with other prisoners of war, you know good things wont come from staying here.
          What do you do?
          a: Stay where you are.
          b: Try sneaking away.
          C: Attempt a mass break out with your fellow war prisoners.""")
    
    choice = input("What do you do now: ")

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
    print("You stay in the camp till they begin moving and weeks later upon reaching a city you are put in jail indefinitly until further notice.")

def try_sneaking_away():
    print("You are trying to sneak put when a gaurd spots you and captures you again and for trying to escape your givin the chopping block.")

def attempt_a_mass_breakut():
    print("""You succesfully convince most of the prisoners to stage a mass breakout and find a way to loosen there binds.
          They launch there suprise attck on the gaurds at night and succesfully get past most of them and while running you see a short sword on the ground.
          Do you pick it up or leave it.
          a: pick it up.
          b: leave it.""")
    
    choice = input("What do you do now: ")

    match choice.lower():
        case "a":
            print("You decide to pick up the short sword.")
            inventory.append("short sword")
            short_sword()
        case "b":
            print("You decide to leave the sword and get out of there.")
            short_sword()
        case _:
            print("Error")

def short_sword():
    if "short sword" in inventory:
        print("""You pick up the sword and make your way away from the camp where you encounter an enemy scout.
              You engage him in combat and though you have limited fighting experience it seems this guy is in the same boat.
              The fight ends with you slaying the scout and making a break for freedom.""")
    else:
        print("""You continue running without the sword and when your about to escape your cornered by a scout.
              Without anything thing to defend yourself with your slayed on the spot.""")

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
    
    choice = input("What do you do now: ")
    
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
    print("""You leave quickly with as much as you can carry without waking anyone and set out.
          You make it a ways and stumble upon a village where you start a making a living through odd jobs and such.
          You also meet a girl and get married and live the rest of your days happily ever after.""")

def sabatoge_the_slavers():
    print("""You sneakily pile all there provisions in a pile and start burning all of it but unfortuantly right as your about to leave a slaver wakes up and tackeles him."
          The fires put out and your bound with much tighter bonds and are soon taken to a draebanorean city where you are sold.""")

def kill_the_slavers():
    print("""You decide to go one by one stabing the slavers."
          You slowly stubble out into the wildernest guilty about what you had done.
          You happen upon a colorfull cloak the road and wonder if you should take it.
          What should you do?
          a: pick it up and wear it.
          b: dont pick it up.""")
    
    choice = input("What do you do now: ")
    
    match choice.lower():
         case "a":
            print("You choose to take the colorfull cloak.")
            inventory.append("colorfull cloak")
            cloak()
         case "b":
            print("You choose to leave it.")
            cloak()
         case _:
            print("Error")

def cloak():
    if "colorfull cloak" in inventory:
        print("""A loud caravan comes by and after seeing his colorfull cloak mistake him for a performer and invite him to join them.
              You decide to take them up on there offer and discover you have a hiddeen talent for this performing thing.
              You end up staying with this group for multiple years and become quite the famous performer in the process.""")
    else:
        print("""A loud caravan comes by and passes him no more than a head nod.
              He continues traveling till he reaches a large city where he spends the majority of his life as a begger on the streets.""")




begin()








# myinput = input("Whats your favorite letter: ")

# match myinput.lower():
    # case "a":
        # print("Choose your own adventure")
    # case "b":
        # print("Lame letter")
    # case _:
        # print("Thats lame")