# 1. Создать программно файл в текстовом формате, записать в него
# построчно данные, вводимые пользователем. Об окончании ввода данных
# свидетельствует пустая строка.

with open('lesson_5_task_1_text.txt', 'w', encoding='UTF-8') as text_txt:
    a = True
    while a:
        a = input('Введите данные для записи в файл:\n')
        text_txt.write(f'{a} \n')
