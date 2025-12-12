# nathan macbeth
# 11/12/25
# Branching lab - Discount-Calculator

bill_amount = float(input("Enter bill amount: "))
discount_percetage = float(input("Enter discount percentage: "))

discount_amount = (bill_amount * discount_percetage) / 100

final_amount = bill_amount - discount_amount

print(f"Original bill amount: ${bill_amount:.2}")
print(f"Discount applied: {discount_percetage}")
print(f"Discount amount: ${discount_amount:.2f}")
print(f"After discount your bill is: ${final_amount:.2f}")