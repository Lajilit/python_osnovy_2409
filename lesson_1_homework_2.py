# Пользователь вводит время в секундах. Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.
try:
    time_sec = int(input("Введите время в секундах: "))
except ValueError:
    print('Нужно ввести число')
else:
    hour = time_sec // 3600
    minute = time_sec % 3600 // 60
    second = time_sec % 60
    print(f'{time_sec} сек. = {hour} ч. {minute} мин. {second} сек.')

