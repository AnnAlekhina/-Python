n = int(input('Введите число n от 0 до 9: '))
if n<10:
    nn = n * 10 + n
    nnn = n * 100 + nn
    res = n + nn + nnn
    print('Результат: ', res)
else:
    print('вы ввели слишком большое число')
