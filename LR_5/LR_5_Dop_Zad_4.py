import math
n = 20
a = 1 / 2
S = ""
for i in range(0, n):
    an = 1 / 2 + math.sqrt(a - a ** 2)
    S = str(an) + ';'+ S 
    a = an  
print(S)
