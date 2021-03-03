string = input('Введите строку: ')
ls = string.split(' ')
print(ls)
for el in ls:
    if len(el) <= 10:
        print(el)
    else:
        print(el[:10])
print('Программа завершена')