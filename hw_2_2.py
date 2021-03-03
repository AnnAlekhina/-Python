ls = list(input('input list: '))
if len(ls) % 2 == 0:
    ls[::2], ls[1::2] = ls[1::2], ls[::2]
else:
    ls[:-2:2], ls[1::2] = ls[1::2], ls[:-2:2]
print(ls)
