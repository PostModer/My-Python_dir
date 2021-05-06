number = str(input("Введите длинное число x = "))
answer = ''
for i in number:
    i = int(i)
    if i % 3 != 0:
        answer = answer + str(i)
    else:
        None
print("Цифры из числа, не делящиеся на 3 без остатка: {}".format(answer))
