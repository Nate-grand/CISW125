

list = ["MHA", "Fairytail", "Darling in the Franxx", "Kakurio: Bed and Breakfast for spirits", "Attack on Titan", "Demon Slayer", "Spy X Family", "Black Clover", "JJK", "Frieren", "The Apothecary Diaries"]
print(sorted(list))

new_show = input("Enter a show you would like to add: ")
list.append(new_show)
print(sorted(list))

remove_show = input("Enter a show you would like to remove: ")
list.remove(remove_show)
print(sorted(list))

