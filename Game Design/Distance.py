# nathan macbeth
# 4/3/2026
# Distance program

import math as m
from unittest import result

def dist(x1, y1, x2, y2):
    distance = m.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return distance

x1 = int(input(f"Enter the coordinates of the first point (x1): "))
y1 = int(input(f"Enter the coordinates of the first point (y1): "))
x2 = int(input(f"Enter the coordinates of the second point (x2): "))
y2 = int(input(f"Enter the coordinates of the second point (y2): "))

print(f"The distance between the points "
      f"({x1}, {y1}) and ({x2}, {y2}) is: "
      f"{dist(x1, y1, x2, y2)}")