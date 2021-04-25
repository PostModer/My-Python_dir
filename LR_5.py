from math import sin
print("ВВедите x0 - начальный x, hx - шаг, xn - конечное значение x")
x0 = float(input("Ввод x0 = "))
xh = float(input("Ввод hx = "))
xn = float(input("Ввод xn = "))
x = x0
plus = 0
minus = 0
while x <= xn:
    y = 1 / 2 + sin(x / 2)
    if y > 0:
        plus += 1
    elif y < 0:
        minus += 1
    else:
        None
    x = x + xh
print("положительных значений y: {}\nОтрицательных значений y: {}".format(plus, minus))
