# 2. Создайте собственный класс-исключение, обрабатывающий ситуацию
# деления на нуль. Проверьте его работу на данных, вводимых
# пользователем. При вводе пользователем нуля в качестве делителя
# программа должна корректно обработать эту ситуацию и не завершиться с
# ошибкой.

class Zero_division_error(Exception):
    def __init__(self, text):
        self.text = text

try:
    dividend = int(input('Enter number: '))
    divisor = int(input('Enter number: '))
    if divisor == 0:
        raise Zero_division_error('Dividing by zero')
except Zero_division_error as err:
    print(err)
else:
    result = dividend / divisor
    print(result)



