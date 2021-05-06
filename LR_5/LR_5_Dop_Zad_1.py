import math
print("ВВедите x0 - начальный x, hx - шаг, xn - конечное значение x")
x0 = float(input("Ввод x0 = "))
xh = float(input("Ввод hx = "))
xn = float(input("Ввод xn = "))
x = x0
while x <= xn:
    if x >= 1 and x <= 3:
        y = (x / 2) * (abs(1 + x) ** (1 / 3))
        print("При x = {}, y = {}".format(x, y))
    elif x > 3:
        y = math.sin(2 * x) / (2 + math.cos(3 * x))
        print("При x = {}, y = {}".format(x, y))
    else:
        print("При x = {} функция неопределена".format(x))
    x = x + xh

