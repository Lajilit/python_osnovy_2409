# Поработайте с переменными, создайте несколько, выведите на экран, запросите у пользователя несколько чисел и строк и
# сохраните в переменные, выведите на экран.

a = 5
print(a)

b = 'string'
print(b)

print(f'{a} - {type(a)}; {b} - {type(b)}')

c = input('Введите значение переменной c: ')

print(f'Класс переменной "c" - {type(c)}, так как класс информации, получаемой через input всегда "строка".'
      f' Значение переменной "c" - {c} ')
