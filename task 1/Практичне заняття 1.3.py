num = int(input("Введіть 4-значне число: "))
# Отримуємо цифри числа через рядок
a = [int(d) for d in str(num)]
print(" + ".join(str(d) for d in a), "=", sum(a))
