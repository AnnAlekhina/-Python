rate = []
first_try = True
while True:
    while True:
        try:
            element = int(input('Введите число: '))
            break
        except ValueError:
            print('Не правильный формат данных.')
    if first_try == True or element < rate[-1]:
        rate.append(element)
        first_try = False
        print(rate)
    elif element > rate[0]:
        rate.insert(0, element)
        print(rate)
    elif element in rate:
        rate.insert(rate.index(element) + rate.count(element), element)
        print(rate)
    else:
        first_meet = True
        for el in rate:
            while first_meet:
                if el < element:
                    rate.insert(rate.index(el), element)
                    print(rate)
                    first_meet = False

