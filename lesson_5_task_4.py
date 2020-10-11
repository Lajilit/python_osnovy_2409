# 4. Создать (не программно) текстовый файл со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу, открывающую файл на чтение и
# считывающую построчно данные. При этом английские числительные
# должны заменяться на русские. Новый блок строк должен записываться в
# новый текстовый файл.

translates = {'One': 'Один',
              'Two': 'Два',
              'Three': 'Три',
              'Four': 'Четыре'}

with open('l5t4_text_1.txt', 'r', encoding='UTF-8') as eng_numbers, \
        open('l5t4_text_2.txt', 'w', encoding='UTF-8') as rus_numbers:
    for line in eng_numbers:
        word, sep, num = line.strip().split()
        num = int(num)
        if word in translates:
            word = translates[word]
        rus_numbers.write(f'{word} - {num}\n')
