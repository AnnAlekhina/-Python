ls = ['some str', 32, 32.0, True, (1, 4, False),{1,2,3}]
for obj in ls:
    print(f'{obj} has type {type(obj)}')
print('end')