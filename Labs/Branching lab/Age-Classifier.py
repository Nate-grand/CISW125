# nathan macbeth
# 11/12/25
# Branching lab - Age-Classifier

age = int(input("Input age: "))

if age >= 20 and age <= 64:
    print("Your an adult.")
elif age <= 19 and age >= 13:
    print("Your a teenager.")
elif age >= 65:
    print("Your a senior.")
else:
    print("Your a child.")