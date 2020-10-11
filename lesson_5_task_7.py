# 7. Создать (не программно) текстовый файл, в котором каждая строка
# должна содержать данные о фирме: название, форма собственности,
# выручка, издержки.
# Пример строки файла: firm_1 ООО 10000 5000.
# Необходимо построчно прочитать файл, вычислить прибыль каждой компании,
# а также среднюю прибыль. Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список. Он должен содержать словарь с фирмами и их
# прибылями, а также словарь со средней прибылью. Если фирма получила
# убытки, также добавить ее в словарь (со значением убытков).
# Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000},
# {“average_profit”: 2000}].
# Итоговый список сохранить в виде json-объекта в соответствующий файл.
# Пример json-объекта:
# [{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
#
# Подсказка: использовать менеджеры контекста.
import json

with open('lesson_5_task_7.txt', 'r', encoding='UTF-8') as firms, \
        open('lesson_5_task_7.json', 'w', encoding='UTF-8') as firms_json:
    total_profit = 0
    firm_dict = {}
    count_profit_firms = 0
    for line in firms:
        units = line.strip().split()
        name = ' '.join(units[:-3])
        proceeds = int(units[-2])
        cost = int(units[-1])
        profit = proceeds - cost
        firm_dict[name] = profit
        if profit >= 0:
            total_profit += profit
            count_profit_firms += 1
    average_profit_dict = {
        'average_profit': total_profit / count_profit_firms
    }
    result_list = [firm_dict, average_profit_dict]
    print(result_list)
    json.dump(result_list, firms_json)
