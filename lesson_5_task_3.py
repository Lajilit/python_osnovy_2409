# 3. Создать текстовый файл (не программно), построчно записать фамилии
# сотрудников и величину их окладов. Определить, кто из сотрудников
# имеет оклад менее 20 тыс., вывести фамилии этих сотрудников.
# Выполнить подсчет средней величины дохода сотрудников.

with open('lesson_5_task_3_text.txt', 'r', encoding='UTF-8') as surname_salary:
    number_of_stuff = 0
    sum_salary = 0
    for line in surname_salary:
        surname, salary = line.strip().split()
        salary = int(salary)
        number_of_stuff += 1
        sum_salary += salary
        if salary < 20000:
            print(f'{surname} salary is less than 20000')
    print(f'Average salary is {sum_salary / number_of_stuff}')
