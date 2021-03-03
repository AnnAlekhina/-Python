from functools import reduce


def mult_func(prev_el, el):
    return prev_el * el


rez = reduce(mult_func, [x for x in range(100, 1001) if x % 2 == 0])
print(rez)
