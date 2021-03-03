fin_dict = {}
summ = 0
with open('test_5_6.txt', encoding='UTF-8') as my_file:
    for line in my_file:
        summ = 0


        subline = line.split()
        for el in subline:
            el = el.split('(')
            print(el)
            for subel in el:
                try:
                    summ += int(subel)
                except:
                    pass
        fin_dict[subline[0][:-1]] = summ
print(fin_dict)
