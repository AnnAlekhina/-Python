list_product = []
dict_product = {}
count = 0
while True:
    name = input('Введите имя товара: ')
    while True:
        try:
            cost = int(input('Введите цену товара: '))
            quantity = int(input('Введите количество товаров: '))
            break
        except ValueError:
            print(' Цена и количество товаров задаются числом. Повторите попытку')
    count += 1
    dict_product['Название'] = name
    dict_product['Цена'] = cost
    dict_product['Количество'] = quantity
    tupl_product = (count, dict_product.copy())
    list_product.append(tupl_product)
    print(list_product)
    key = input('Если хотите покинуть режим ввода товаров, нажмите q, если желаете продолжить, нажмите ENTER: ')
    if key.lower() == 'q':
        break
new_dict = {}
new_list=[]
for key in tupl_product[1].keys():
    new_list.clear()
    for i in range(len(list_product)):
        new_list.append(list_product[i][1][key])
    new_dict[key] = new_list.copy()
print(new_dict)






