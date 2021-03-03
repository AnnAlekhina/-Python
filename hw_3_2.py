def cheak_email(email):
    if '@' and ('.ru' or '.com') not in email:
        return 'Введен некорректный email'
    else:
        return email


def cheak_number(number):
    if len(number) < 10 or len(number) > 11:
        return 'Введен некорректный номер'
    return number


def user_inf_func(name, sur, city, year, email, num):
    return f'Имя: {name}, Фамилия: {sur}, город: {city}, год рождения: {year},email: {email}, номер: {num}'


print('Введите через пробел следующую информацию: '
      'Имя, Фамилия, год рождения, город проживания, email, моб.телефон: ')
name, surname, years, *city, email, number = input().split(' ')
print(user_inf_func(name=name, sur=surname, year=years,
                    city=' '.join(city), email=cheak_email(email), num=cheak_number(number)))

