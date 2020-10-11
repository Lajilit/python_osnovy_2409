# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.

with open('l5t5_text.txt', 'w', encoding='UTF-8') as numbers_write:
    numbers_write.write('1 2 3 4 5 6 7 8 9 0')

with open('l5t5_text.txt', 'r', encoding='UTF-8') as numbers_read:
    numbers = []
    for line in numbers_read:
        for number in line.strip().split():
            numbers.append(int(number))
    print(sum(numbers))
