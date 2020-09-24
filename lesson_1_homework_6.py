# Спортсмен занимается ежедневными пробежками. В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего. Требуется определить номер дня, на
# который результат спортсмена составит не менее b километров. Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
try:
    a = int(input('Введите начальный результат: '))
    b = int(input('Введите желаемый результат: '))
    day_number = 1
    if a <= 0 or b <= 0:
        raise ValueError

except ValueError:
    print('Нужно ввести целое положительное число')
else:
    while a < b:
        print(f'{day_number} день: {a}')
        day_number += 1
        a = round(a * 1.1, 2)
    print(f'{day_number} день: {a}')
    print(f'На {day_number}-й день спортсмен достиг результата - не менее {b} км.')
