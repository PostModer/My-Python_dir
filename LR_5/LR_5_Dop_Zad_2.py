import math
print("ВВедите x0 - начальный x, hx - шаг, xn - конечное значение x")
x0 = float(input("Ввод x0 = "))
xh = float(input("Ввод hx = "))
xn = float(input("Ввод xn = "))
x = x0
xmax = x
dmax = (1 + math.cos(xmax / 3) ** 2) - (3 + math.sin(xmax / 2) ** 2)
while x <= xn:
    y1 = 1 + math.cos(x / 3) ** 2
    y2 = 3 + math.sin(x / 2) ** 2
    d = y2 - y1
    if d > dmax:
        dmax = d
        xmax = x
    else:
        None
    x = x + xh
print("Значение х при котором расстояние максимальное: xmax = {}\nМаксимальное расстояние dmax = {}".format(xmax, dmax))
