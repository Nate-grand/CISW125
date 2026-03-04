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

print(f" ok your name is: {name} \n your age is: {age} \n and your favorite anime is: {anime}")