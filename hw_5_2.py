with open('test_5_2.txt') as my_file:
    content = my_file. readlines()
print(f'В файле {len(content)} строк(и)')
i = 1
for string in content:
    print(f'В строке под номером {i}: {len(string.split())} слов(а)')
    i += 1
