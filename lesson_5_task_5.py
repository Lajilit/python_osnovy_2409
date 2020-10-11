# 5. Создать (программно) текстовый файл, записать в него программно
# набор чисел, разделенных пробелами. Программа должна подсчитывать
# сумму чисел в файле и выводить ее на экран.
from random import randint

with open('l5t5_text.txt', 'w', encoding='UTF-8') as numbers_write:
    numbers_list = [str(randint(0, 100)) for num in range(20)]
    numbers_write.write(' '.join(numbers_list))

with open('l5t5_text.txt', 'r', encoding='UTF-8') as numbers_read:
    numbers = []
    for line in numbers_read:
        for number in line.strip().split():
            numbers.append(int(number))
    print(sum(numbers))
