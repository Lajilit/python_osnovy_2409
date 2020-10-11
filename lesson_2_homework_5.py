# 5. Реализовать структуру «Рейтинг», представляющую собой не возрастающий набор натуральных чисел. У пользователя
# необходимо запрашивать новый элемент рейтинга. Если в рейтинге существуют элементы с одинаковыми значениями,
# то новый элемент с тем же значением должен разместиться после них.
# Подсказка. Например, набор натуральных чисел: 7, 5, 3, 3, 2.
# Пользователь ввел число 3. Результат: 7, 5, 3, 3, 3, 2.
# Пользователь ввел число 8. Результат: 8, 7, 5, 3, 3, 2.
# Пользователь ввел число 1. Результат: 7, 5, 3, 3, 2, 1.
# Исходный набор натуральных чисел можно задать  непосредственно в коде, например, my_list = [7, 5, 3, 3, 2].

my_list = []


def rating_include(list_rating):
    try:
        input_number = int(input('Введите число: '))
        if input_number <= 0:
            raise ValueError
    except ValueError:
        print('Нужно ввести целое положительное число')
    else:
        if not list_rating:
            list_rating.append(input_number)
            print(list_rating)
        else:
            for i, n in enumerate(list_rating):
                if n < input_number:
                    list_rating.insert(i, input_number)
                    break
            if input_number <= list_rating[-1]:
                list_rating.append(input_number)


if __name__ == '__main__':
    for i in range(15):
        rating_include(my_list)
        print(my_list)
