g = int(input("Введіть a (1-1000): "))
b = int(input("Введіть b (1-1000): "))

g = (g + b + abs(g - b)) // 2
print("Максимальне:", g)
