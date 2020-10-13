def degree_func_easy(num, deg):
    return num ** deg


def degree_func_hard(num, deg):
    rez = 1
    i = 0
    while i != abs(deg):
        rez = rez/num
        i += 1
    return rez


number = int(input('Введите положительное число: '))
degree = int(input('Введите степень (отрицательное число): '))
print((degree_func_easy(number, degree)))
print((degree_func_hard(number, degree)))
