# 6. Необходимо создать (не программно) текстовый файл, где каждая
# строка описывает учебный предмет и наличие лекционных, практических и
# лабораторных занятий по этому предмету и их количество. Важно, чтобы
# для каждого предмета не обязательно были все типы занятий.
# Сформировать словарь, содержащий название предмета и общее количество
# занятий по нему. Вывести словарь на экран.
# Примеры строк файла:
# Информатика: 100(л) 50(пр) 20(лаб).
# Физика: 30(л) — 10(лаб)
# Физкультура: — 30(пр) —
#
# Пример словаря:
# {“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
subjects_dict = {}

with open('lesson_5_task_6.txt', 'r', encoding='UTF-8') as subjects:
    for line in subjects:
        subject, hours = line.strip().split(': ')
        hours_list = []
        num = ''
        for char in hours:
            if char.isdigit():
                num += char
            elif num != '':
                hours_list.append(int(num))
                num = ''
        if num != '':
            hours_list.append(int(num))
        subjects_dict[subject] = sum(hours_list)

print(subjects_dict)