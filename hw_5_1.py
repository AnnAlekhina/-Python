import os

modes = {0:'w', 1:'a'}
str_list =[]
user_mode = int(input('Создать новый файл?\n да - 0\n нет - 1\n:'))
user_path = input('Введите название файла : ')
if os.path.exists(f'{user_path}.txt') and user_mode == 0:
    choice = int(input(('Файл с таким именем уже существует. Продолжить?\n'
          'да - 0 (В этом случае данные будут потеряны)\n'
          'нет -1\n:')))
    while  os.path.exists(f'{user_path}.txt') and choice == 1:
        user_path = input('Введите новое название файла : ')
        if  not os.path.exists(f'{user_path}.txt'):
            choice = 0
        else:
            print('Файл с таким именем уже существует' )
    user_mode = choice
while True:
    message = input('Введите строку (для окончания записи нажмите ENTER): ')
    if not message:
        break
    else:
        str_list.append(message)
with open(f'{user_path}.txt', modes[user_mode]) as new_file:
    new_file.writelines('%s\n' % line for line in str_list)




