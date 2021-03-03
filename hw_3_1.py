def div_func(div1, div2):
    try:
        return div1/div2
    except ZeroDivisionError as err:
        return f'Ошибка {err}'


while True:
    try:
        a = int(input('Введите делимое: '))
        b = int(input('Введите делитель: '))
        break
    except ValueError as err:
        print(f'Ошибка {err}, попробуйте еще раз')

print(div_func(a, b))

