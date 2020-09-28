# Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn. Например, пользователь ввёл число 2.
# Считаем 2 + 22 + 222 = 246.

number = input("Введите число:  ")
try:
    num = int(number)
    if num < 0:
        raise ValueError
except ValueError:
    print('Нужно ввести положительное число')
else:
    print(f'{number} + {number*2} + {number*3} = {int(number) + int(number*2) + int(number*3)}')