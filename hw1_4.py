number =input('Введите целое положительное число: ')
i = 1
max = int(number[0])
while i<len(number):
    if int(number[i])>max:
        max=int(number[i])
    i+=1
print("максимальная цифра: ",max)

