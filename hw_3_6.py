def int_func(new_word_list):
    new_word_list = ' '.join(list(map(str.capitalize, new_word_list)))
    return new_word_list


word = input('Введите слово с маленькой буквы: ').split(' ')
print(int_func(word))
