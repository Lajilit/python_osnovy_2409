# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите целое положительное число: '))
max_digit = 0

while number > 0:
# оригинальный код
    # if number % 10 > max_digit:
    #     max_digit = number % 10
    # number = number // 10

# первый вариант исправления
    # number, remainder = number // 10, number % 10
    # if remainder > max_digit:
    #     max_digit = remainder

# второй вариант исправления, встроенная функция divmod одновременно делит и убирает остаток от деления
    number, remainder = divmod(number, 10)
    if remainder > max_digit:
        max_digit = remainder

print(max_digit)