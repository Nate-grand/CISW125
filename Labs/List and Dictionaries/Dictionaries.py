# nathan macbeth
# 1/30/26
# Dictionaries lab

inventory = {"Apples": 10, "Bananas": 15, "Oranges": 8, "Pears": 5, "Peaches": 12}
print(f"Current Banana Stock: {inventory['Bananas']}")
inventory["Plums"] = 17
inventory["Peaches"] += 56
inventory["Apples"] -= 8
all_items = inventory.keys()
print(list(all_items))