# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
try:
    time_sec = int(input("Введите время в секундах: "))
    if time_sec < 0:
        raise ValueError
except ValueError:
    print('Нужно ввести положительное число')
else:
    hour = time_sec // 3600
    if hour < 10:
        hour = '0' + str(hour)
    else:
        hour = str(hour)
    minute = time_sec % 3600 // 60
    if minute < 10:
        minute = '0' + str(minute)
    else:
        minute = str(minute)
    second = time_sec % 60
    if second < 10:
        second = '0' + str(second)
    else:
        second = str(second)
    print(f'{time_sec} сек. = {hour}:{minute}:{second}')

