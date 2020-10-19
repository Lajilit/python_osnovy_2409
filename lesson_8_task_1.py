# Реализовать класс «Дата», функция-конструктор которого должна
# принимать дату в виде строки формата «день-месяц-год». В рамках класса
# реализовать два метода. Первый, с декоратором @classmethod, должен
# извлекать число, месяц, год и преобразовывать их тип к типу «Число».
# Второй, с декоратором @staticmethod, должен проводить валидацию числа,
# месяца и года (например, месяц — от 1 до 12). Проверить работу
# полученной структуры на реальных данных.


class Date:
    def __init__(self, input_date):
        self.date = input_date

    @classmethod
    def date_to_int(cls, input_date):
        day, month, year = input_date.split('-')
        return int(day), int(month), int(year)

    @staticmethod
    def valid_date(day, month, year):
        if not 2000 <= year <= 2020:
            raise ValueError( 'Invalid year')
        elif not 1 <= month <= 12:
            raise ValueError('Invalid year')
        elif (month in (1, 3, 5, 7, 8, 10, 12) and not 1 <= day <= 31) or \
                (month in (4, 6, 9, 11) and not 1 <= day <= 30) or \
                (month == 2 and year % 4 == 0 and not 1 <= day <= 29) or \
                (month == 2 and year % 4 != 0 and not 1 <= day <= 28):
            raise ValueError('Invalid day')
        else:
            return day, month, year

    def check_date(self):
        date, month, year = Date.date_to_int(self.date)
        date = self.valid_date(date, month, year)
        return date

    def __str__(self):
        return f'The current date - {Date.date_to_int(self.date)}'


a = Date('22-10-2000')
print(a)
print(a.check_date())
print(Date.valid_date(10, 12, 2020))
print(a.valid_date(10, 12, 2020))
# print(a.valid_date(10, 22, 2020))
b = Date.date_to_int('10-10-2010')
print(b)
