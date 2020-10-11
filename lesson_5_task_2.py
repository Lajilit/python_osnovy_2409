# 2. Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой
# строке.

with open('lesson_5_task_2.txt', 'r', encoding='UTF-8') as esenin:
    count_lines = 0
    count_words = 0

    for line in esenin:
        count_lines += 1
        line_words = len([word for word in line.strip().split()])
        print(f'В {count_lines} строке - {line_words} слов')
        count_words += line_words

    print(f'Всего строк в документе {count_lines}.')
    print(f'Всего в документе {count_words} слов')
