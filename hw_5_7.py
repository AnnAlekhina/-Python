import json

profit_dict = {}
average_profit = 0
i = 0
average_profit_dict = {}
with open('test_5_7.txt',encoding='utf-8') as my_file:
    for string in my_file:
        content = string.split()
        profit = int(content[2]) - int(content[3])
        profit_dict[content[0]] = profit
        if profit > 0:
            average_profit += profit
            i += 1
try:
    average_profit = average_profit/i
except ZeroDivisionError as err:
    print('Все фирмы отработали с убытками, невозможо рассчитать среднюю прибыль: ', err)
average_profit_dict['average_profit'] = average_profit
result_list = [profit_dict, average_profit_dict]
print(type(result_list))
with open('test_5_7.json','w') as json_file:
    json.dump(result_list, json_file)








