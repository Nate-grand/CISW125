import os

file_path = "output.txt"

if os.path.exists(file_path):
    with open(file_path, "r") as file:
        anime_list = [line.strip() for line in file.readlines()]
else:
    anime_list = ["MHA", "Fairytail", "Darling in the Franxx", "Attack on Titan", "Demon Slayer"]

print("Current List:", sorted(anime_list))

new_show = input("Enter a show you would like to add: ")
if new_show:
    anime_list.append(new_show)
    print("Updated List:", sorted(anime_list))


remove_show = input("Enter a show you would like to remove: ")
if remove_show in anime_list:
    anime_list.remove(remove_show)
    print("Final List:", sorted(anime_list))
else:
    print(f"'{remove_show}' not found in list.")

with open(file_path, "w") as file:
    for item in anime_list:
        file.write(f"{item}\n")

print(f"List successfully saved to {file_path}!")