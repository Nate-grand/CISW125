# nathan macbeth
# 3/3/2026
# First program distance stuff and strings

my_String = """All strings must have double quotes or single quotes surrounding them."""

my_String2 = """I like icecream
do you like nuts?
What is your name?
Anime is peak living."""

# print(my_String2)
# print(my_String)

st3 = "My name is L."

# print(f"Just so you know, \n{my_String2} \n Whats your opinion on your mom typa deal? \n {st3}")

name = input(f"{st3} What is your name?:   ")
age = input(f"What is your age?:   ")
anime = input(f"What is your favorite anime?:   ")

if anime == "Frieren":
    anime = "Frieren thats my favorite too! You have the bestest of taste."
else:
    feelgoods = input(f"oh you like {anime}? Thats pretty good, but do you like Frieren? (yes or no or kinda):   ")
    if feelgoods.lower() == "yes":
        anime = "Frieren thats my favorite too! You have the bestest of taste."
    elif feelgoods.lower() == "no":
        anime = ("""Oh you dont like Frieren? I cant respect that but i can hope you recover from this crippling mental illness
                  that caused this dislike.""")
        print(anime)
    elif feelgoods.lower() == "kinda":
        anime = ("""Oh you kinda like Frieren? Thats pretty good, but you should really just go all in and love it.""")
        print(anime)
    else:
        print("that makes no sense but if you have seen i guess you must like it at least a bit so join the cult.")

myfinalstring = (f" ok your name is: {name} \n your age is: "
      f" {age} \n and your favorite anime "
      f" is: {anime}")

print(myfinalstring)