# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в
# цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
# На вебинаре реализовали похожий пример для чисел Фиббоначи.

def fact(num: int):
    """Generator of the factorial of a number for numbers from 0 to num

    :param num: positive integer
    :return: generator
    """
    start = 0
    end = num + 1
    factorial = 1
    for i in range(start, end):
        if i == 0:
            yield 1
        else:
            factorial *= i
            yield factorial


if __name__ == '__main__':
    print([el for el in fact(10)])