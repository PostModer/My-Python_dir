import math
def Math_Sol(x):
    if x == 0 or x < 0:
        print("Недопустимое значение x, введите другое!")
    else:
        a = math.tan(x)
        b = math.exp(math.cos(x))
        y = (a + math.sin(b) ** 2 - math.log(x + 1)) / x
        return y
print(Math_Sol(1))