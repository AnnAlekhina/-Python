key = 0
message = {
    0: 'Вы ввели некорректное число, попробуйте снова',
    1: 'Программа завершена'
}
while True:
    while True:
        try:
            number_month = int(input('Введите номер месяца: '))
            break
        except ValueError:
            print('Не правильный формат данных.')

    while (number_month <= 12) and (number_month > 0):
        dict_month = {
            1: 'winter',
            2: 'winter',
            3: 'spring',
            4: 'spring',
            5: 'spring',
            6: 'summer',
            7: 'summer',
            8: 'summer',
            9: 'autumn',
            10: 'autumn',
            11: 'autumn',
            12: 'winter',
        }
        list_month = ['winter', 'winter', 'spring', 'spring', 'spring', 'summer', 'summer', 'summer', 'autumn',
                      'autumn', 'autumn', 'winter']
        print(f'(словарь) Месяц под номером {number_month} - {dict_month[number_month]} (список) {list_month[number_month-1]}')
        key = 1
        break
    print(message[key])
    if key == 1:
        break
