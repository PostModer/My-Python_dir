print('Дека = 10^1\nГекто = 10^2\nКило = 10^3\nМега = 10^6\nГига = 10^9')
Prest = string(input("Введите название приставки ----> ")
if Prest == "Дека":
    print("{} = 10^1".format(Prest))
elif Prest == "Гекто":
    print("{} = 10^2".format(Prest))
elif Prest == "Кило":
    print("{} = 10^3".format(Prest))
elif Prest == "Мега":
    print("{} = 10^6".format(Prest))
elif Prest == "Гига":
    print("{} = 10^9".format(Prest))
else:
    print('Неверное значение, повторите попытку!')
