def fact(n):
    for el in list(range(1, n+1)):
        if el == 1:
            rez = el
            yield rez
        else:
            rez = rez * el
        yield rez


n = int(input('Введите чило: '))
for el in fact(n):
    print(el)
