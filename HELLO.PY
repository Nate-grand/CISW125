firstname = "Nathan"
lastname = "Macbeth"

address= """north 3000 west
Rexburg ID, 83440"""



a = 1
b = 2
c = 3
d = 4
e = 5
f = 6
g = 10
h = 20

f = e + a
e = d + a
d = a + c
c = a + b

print(f" {a} + {c} = {d}")
print(f" {a} + {d} = {e}")
print(f" {a} + {e} = {f}")
print(f" {a} + {b} = {c}")

print(f" {f} / {b} = {c}")
print(f" {g} / {b} = {e}")
print(f" {h} / {b} = {g}")
print(f" {d} / {b} = {b}")

celcius = int(input("enter a celcious temp"))
fareignheight = (9/5)*celcius + 32
print(f" {celcius} c = {fareignheight} f ")

