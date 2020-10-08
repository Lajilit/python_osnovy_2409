# 7. Реализовать генератор с помощью функции с ключевым словом yield,
# создающим очередное значение. При вызове функции должен создаваться
# объект-генератор. Функция должна вызываться следующим образом:
# for el in fact(n). Функция отвечает за получение факториала числа, а в
# цикле необходимо выводить только первые n чисел, начиная с 1! и до n!.
# Подсказка: факториал числа n — произведение чисел от 1 до n. Например,
# факториал четырёх 4! = 1 * 2 * 3 * 4 = 24.
# На вебинаре реализовали похожий пример для чисел Фиббоначи.

def fact(num: int):
    """Generator of the factorial of a number for numbers from 1 to num

    :param num: positive integer
    :return: generator
    """
    start = 1
    end = num + 1
    for i in range(start, end):
        factorial = 1
        while i > 1:
            factorial *= i
            i -= 1
        yield factorial


if __name__ == '__main__':
    print([el for el in fact(10)])