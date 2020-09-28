# 3. Пользователь вводит месяц в виде целого числа от 1 до 12. Сообщить к какому времени года относится месяц (зима,
# весна, лето, осень). Напишите решения через list и через dict.

try:
    input_month = int(input('Введите номер месяца: '))
    if input_month < 1 or input_month > 12:
        raise ValueError
except ValueError:
    print('Нужно ввести целое число от 1 до 12')
else:
    seasons = {'Зима': (12, 1, 2),
               'Весна': (3, 4, 5),
               'Лето': (6, 7, 8),
               'Осень': (9, 10, 11)}
    for season, months in seasons.items():
        if input_month in months:
            print(f'{input_month} месяц относится ко времени года {season}')

# Второй вариант решения - через список. Если честно, я не совсем поняла, как в принципе решать через список,
# поэтому решение получилось достаточно корявое, в реальной жизни я бы так не написала
try:
    input_month = int(input('Введите номер месяца: '))
    if input_month < 1 or input_month > 12:
        raise ValueError
except ValueError:
    print('Нужно ввести целое число от 1 до 12')
else:
    seasons = ['Зима', 'Весна', 'Лето', 'Осень']
    if 3 <= input_month <= 5:
        print(f'{input_month} месяц относится ко времени года {seasons[1]}')
    elif 6 <= input_month <= 8:
        print(f'{input_month} месяц относится ко времени года {seasons[2]}')
    elif 9 <= input_month <= 11:
        print(f'{input_month} месяц относится ко времени года {seasons[2]}')
    else:
        print(f'{input_month} месяц относится ко времени года {seasons[0]}')
