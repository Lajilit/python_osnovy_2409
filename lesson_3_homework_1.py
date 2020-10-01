# 1. Реализовать функцию, принимающую два числа (позиционные аргументы) и выполняющую их деление. Числа запрашивать у
# пользователя, предусмотреть обработку ситуации деления на ноль.

def input_div(num_1, num_2):
    """Takes two (non-complex) numbers as arguments and returns the quotient from division of first argument by the
    second """
    try:
        result = num_1 / num_2
    except ZeroDivisionError:
<<<<<<< HEAD
        return 'Division by zero'
=======
        print('Division by zero')
>>>>>>> lesson_3
    else:
        return result


if __name__ == '__main__':
    a = float(input('Enter the first number: '))
    b = float(input('Enter the second number: '))
    c = input_div(a, b)
    print(c)
