# nathan macbeth
# 4/12/25
# Types project

Anime = input("Whats your favorite anime?: ")
Anime_character = input("Whats your favorite anime character?: ")

character_count = len(Anime)
print(f"Your favorite anime is {character_count} characters long.")

character_count = len(Anime_character)
print(f"Your favorite anime_character is {character_count} characters long.")

mysubstring1 = Anime[0:100]
mysubstring1 = mysubstring1[0]

mysubstring2 = Anime_character[0:100]
mysubstring2 = mysubstring2[0]

print(f"The intials of your favorite anime and anime character are {mysubstring1} and {mysubstring2}.")