# 1. Реализовать скрипт, в котором должна быть предусмотрена функция
# расчета заработной платы сотрудника. В расчете необходимо использовать
# формулу: (выработка в часах * ставка в час) + премия. Для выполнения
# расчета для конкретных значений необходимо запускать скрипт
# с параметрами.

from sys import argv

month_number_of_hours_worked = argv[1]
hourly_rate = argv[2]
month_bonus = argv[3]

salary = int(month_number_of_hours_worked) * int(hourly_rate) +\
         int(month_bonus)
print(salary)