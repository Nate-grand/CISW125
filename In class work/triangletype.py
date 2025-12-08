# nathan macbeth
# 02/12/25
# triangle types

def triangletype(): # The "def" defines the function
    try: # The try function will try to complete a task and if there is an error it will throw the exeption and move on
        a = float(input("\ninput the length of side one: "))
        b = float(input("input the length of side two: "))
        c = float (input("input the length of side three: "))

        side = [a, b, c] # This adds the sides lengths to a list/array
        side = sorted(side) # Sorts the list from smallest to largest

        if side[0] + side[1] > side[2]:
            if side[0] ** 2 + side[1] ** 2 == side[2] ** 2:
                 print(f"The triangle with side lengths {a}, {b}, {c} is a right triangle")
            elif side[0] ** 2 + side[1] ** 2 == side[2] ** 2:
                 print(f"The triangle with side lengths {a}, {b}, {c} is an acute triangle")
            else:
                 print(f"The triangle with side lengths {a}, {b}, {c} is an obtuse triangle")     
        
        else:
            print("Invalid input!!\n The side lengths you entered will not form a triangle\n Try again: ")
            triangletype() 

    except:
        print("Invalid input\n Input must be a number\n Try again: ")
        triangletype()

triangletype()