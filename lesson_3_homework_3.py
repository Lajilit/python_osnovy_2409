# 3. Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму наибольших двух
# аргументов.

def my_func(num_1, num_2, num_3):
    """Takes three (non-complex) numbers as arguments and returns the sum of the two largest ones"""
    try:
        result = sum((num_1, num_2, num_3)) - min(num_1, num_2, num_3)
    except TypeError:
        return 'TypeError: arguments must be numbers'
    else:
        return result


if __name__ == '__main__':
    print(my_func('5643', 566, 1858))

