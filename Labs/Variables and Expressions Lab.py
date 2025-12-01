# CISW 125
# Intro to programming

# Follow the Documentation Policy as it's good practice and will get you used to what you should do for
# your projects and other labs.

# If you're stuck, ask questions. There are no dumb questions.
# ------------------------------------------------------------------------------------------------------
# We're going to play around with variables and expressions today
# The goal is to just test out things and put them to use and possibly
# save the ideas/work for projects down the line.

# Again, the goal is to "play" around and explore. There's no right or wrong to this.
# Just think about input vs output and what we can do with them.
# ------------------------------------------------------------------------------------------------------


# Create some variables, give them a theme. Example: items on a grocery list, games/books/movies you enjoy, etc.
vegtable = "carrot"
fruit = "apple"
meat = "steak"
book = "paper"
movie = "screens"
game = "Clue"
pi = 3.14
# Then print your variables.
print(vegtable)
print(fruit)
print(meat)
print(book)
print(movie)
print(game)
print(pi)

# Now try to reassign a value. This is essentially "overwriting" your variables data with new data. Python works from top to bottom.
vegtable = "cucumbers"
fruit = "bananas"
# After you've done this, try to print your variables in string using f-strings.
print(f"You like {vegtable} a lot")
print(f"You love {fruit} even more")
print(f"I personally like {meat} the most")
print(f"I love to draw on {book} an awfull lot")
print(f"Looking at {movie} is fun")
print(f"Im having lots of {game} right now")
print(f"The first three digits of pi are {pi} which is cool")

# Next, try to create some expressions that involve addition, subtraction, multiplication, and division
# Store the results of your expressions in a variable and then print the outcome
plus = "+"
minus = "-"
times = "*"
divided = "/"

print(f"5 {plus} 5 = 10")
print(f"28 {minus} 22 = 6")
print(f"4 {times} 5 = 20")
print(f"12 {divided} 2 = 6")

a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 10
h = 15
i = 20

print(f" {f} + {d} = {g}")
print(f" {g} + {e} = {h}")
print(f" {a} + {b} = {c}")
print(f" {c} + {a} = {d}")

print(f" {i} - {g} = {g}")
print(f" {h} - {e} = {g}")
print(f" {d} - {a} = {c}")
print(f" {f} - {e} = {a}")


# See if you can find other ways to "do maths" (hint: operators are useful and efficient.)
# https://www.w3schools.com/python/python_operators.asp
print(10 + 5)

sum1 = 100 + 50      # 150 (100 + 50)
sum2 = sum1 + 250    # 400 (150 + 250)
sum3 = sum2 + sum2   # 800 (400 + 400)

# Now, I'd like you to make two variables that contain your first and last name
# After you've made the variables, find a way to join the two strings to print your full name. This is string concatenation.
# Think of it as "adding" your variables together.
firstname = "Nathan"
lastname = "Macbeth"

print(" my name is " + str(firstname) + str(lastname) +  " which i like")

# While we did some math earlier, I'd like you to try doing math with variables this time. (If you already did this, you can skip this. Good job.)


# Lastly, do something of your own choice. Anything that involves variables and expressions is allowed here.
# If you're stumped on ideas, just try and make an expression that converts Celsius to Fahrenheit or vice versa.
sixty = 15.6
print(f"sixty degrees fareinheit is about {sixty} degrees in celcious")

fairytail = "greatest"
print(f"fairytail is the {fairytail} show of all time")
# Upload this to Schoology under the Variable and Expressions Lab assignment.
