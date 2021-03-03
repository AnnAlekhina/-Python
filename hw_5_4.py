list_num = ['Один','Два','Три', 'Четыре']
with open('test_5_4.txt') as my_file:
    content = my_file.read()
content = list(map(str.split, content.splitlines()))
with open('test_5_4_result.txt','a') as result:
    for i in range(len(content)):
        content[i][0] = list_num[i]
        new_content = ' '.join(content[i])
        print(new_content)
        result.write(new_content + '\n')




