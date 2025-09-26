import math

a = float(input("Введіть a: "))
b = float(input("Введіть b: "))
c = float(input("Введіть c: "))

D = b**2 - 4*a*c  # дискримінант

if D < 0:
    print("Коренів немає")
elif D == 0:
    x = -b / (2*a)
    print(f"Один корінь: {x:.2f}")
else:
    x1 = (-b + math.sqrt(D)) / (2*a)
    x2 = (-b - math.sqrt(D)) / (2*a)
    print(f"Корені: {x1:.2f}, {x2:.2f}")
