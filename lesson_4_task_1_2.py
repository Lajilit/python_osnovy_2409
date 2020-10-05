# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт
# с параметрами.

import argparse

parser = argparse.ArgumentParser()

parser.add_argument('month_hours', type=int, help='Months number of hours')
parser.add_argument('hourly_rate', type=int, help='Salary for an hour')
parser.add_argument('month_bonus', type=int, help='Bonus for an month')

arg = parser.parse_args()

salary = arg.month_hours * arg.hourly_rate +\
         arg.month_bonus

print(salary)