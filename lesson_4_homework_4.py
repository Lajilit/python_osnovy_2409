# 4. Программа принимает действительное положительное число x и целое отрицательное число y. Необходимо выполнить
# возведение числа x в степень y. Задание необходимо реализовать в виде функции my_func(x, y). При решении задания
# необходимо обойтись без встроенной функции возведения числа в степень. Подсказка: попробуйте решить задачу двумя
# способами. Первый — возведение в степень с помощью оператора **. Второй — более сложная реализация без оператора
# **, предусматривающая использование цикла.

# Первый вариант решения:

# def my_func(x, y):
#     """Takes the non-complex number as 'x' and a negative integer as 'y' and returns the result of 'x' raised to 'y'
#     power """
#     try:
#         x = float(x)
#         y = int(y)
#         if y >= 0:
#             raise ValueError
#     except ValueError:
#         return '"x" must be non-complex number and "y" must be negative integer'
#     else:
#         return x ** y

# Второй вариант решения:

def my_func(x: float, y: 'int, < 0') -> [str, float]:
    """Takes the non-complex number as 'x' and a negative integer as 'y'
     and returns the result of 'x' raised to 'y' power """
    try:
        x = float(x)
        y = int(y)
        if y >= 0:
            raise ValueError
    except ValueError:
        return 'ValueError: "x" must be non-complex number and "y" must be ' \
               'negative integer'
    else:
        result = 1
        while y < 0:
            result = result * x
            y += 1
        return 1 / result


if __name__ == '__main__':
    print(my_func('слон', -3))
