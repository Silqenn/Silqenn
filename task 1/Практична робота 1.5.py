a = float(input("Введіть s0: "))
b = float(input("Введіть v0: "))
c  = 9.8   # прискорення вільного падіння
d = float(input("Введіть час t: "))

import math

s = a + b*d + 0.5*c*d**2
print("s =", s)

e = float(input("Введіть PV (початкова сума): "))
f = float(input("Введіть INT (річний %): "))
g = int(input("Введіть кількість років: "))

FV = e * (1 + f/100)*g
print("FV =", FV)

m1 = float(input("Введіть a: "))
m2 = float(input("Введіть p: "))
m3 = float(input("Введіть m1: "))
m4 = float(input("Введіть m2: "))

G = (4 * math.pi**2 * a**3) / (m2**2 * (m1 + m2))
print("G =", G)
