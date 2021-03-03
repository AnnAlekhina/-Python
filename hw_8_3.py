class MyError(Exception):
    def __init__(self,text):
        self.text = text

user_list = []
print('Вводите эдементы: ')
while True:
    try:
        el = input().lower()
        if el == 'stop':
            break
        elif el.isdigit():
            user_list.append(el)
        else:
            raise MyError('Введено не число!')
    except MyError as err:
        print(f'Ошибка {err}')
print(user_list)





