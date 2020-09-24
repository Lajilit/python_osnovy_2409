# Пользователь вводит целое положительное число. Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


number = int(input('Введите целое положительное число: '))
max_digit = 0

while number > 0:
    if number % 10 > max_digit:
        max_digit = number % 10
    number = number // 10

print(max_digit)