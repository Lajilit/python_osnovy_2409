# 2. Создать текстовый файл (не программно), сохранить в нем несколько
# строк, выполнить подсчет количества строк, количества слов в каждой
# строке.

with open('l5t2_text.txt', 'r', encoding='UTF-8') as esenin:
    count_lines = 0
    count_line_words = {}
    count_words = 0

    for line in esenin:
        count_lines += 1
        line_words = len([word for word in line.strip().split()])
        count_line_words[count_lines] = line_words

    print(f'Всего строк в документе {count_lines}.')

    for line, words_num in count_line_words.items():
        print(f'В {line} строке - {words_num} слов')
        count_words += words_num

    print(f'Всего в документе {count_words} слов')
