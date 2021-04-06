#Лаба по информатике номер 3
import math
def square_tri(x, y, z):
    p = (x + y + z) / 2
    Stri = math.sqrt(p * (p - x) * (p - y) * (p - z))
    return Stri
def square_kvad(a):
    Skv = a ** 2
    return Skv
def square_round(r):
    Srou = math.pi * r ** 2
    return Srou
Stri = square_tri(3, 4, 5)
Skv = square_kvad(2)
Srou = square_round(3)
if Skv > Srou:
    if Stri > Skv:
        print("Площадь треугольника = ", Stri)
    else:
        print("Площадь квадрата = ", Skv)
else:
    if Stri > Srou:
        print("Площадь треугольника = ", Stri)
    else:
        print("Площадь круга = ", Srou)





