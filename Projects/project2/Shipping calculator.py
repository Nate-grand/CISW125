# nathan macbeth
# 15/12/25
# Project 2-Shipping Calculator

print("Shipping Calculator program")

def shipping_cost(weight, distance):

    cost_per_pound = 1.00

    cost_per_segment = 0.25

    segment_length = 500

    weight_cost = weight * cost_per_pound

    num_segments = distance // segment_length

    distance_cost = num_segments * cost_per_segment

    total_cost = weight_cost + distance_cost

    return total_cost

shippment_weight = float(input("Enter weight of shipment: "))
miles_to_ship = float(input("Enter miles to ship: "))

if shippment_weight <= 0 or miles_to_ship <= 0:
        print("Weight and distance must be positive numbers.")
else:
        charge = shipping_cost(shippment_weight, miles_to_ship)
        print(f"To ship a {shippment_weight} pound package {miles_to_ship} miles, your charge is ${charge:,.2f}.")

    
    
