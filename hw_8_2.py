class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

a = int(input('Введите делимое: '))
b = int(input('Введите делитель: '))
try:
    if b == 0:
        raise MyError('Деление на ноль')
except MyError as err:
    print(err)
else:
    rez = a/b
    print(rez)
