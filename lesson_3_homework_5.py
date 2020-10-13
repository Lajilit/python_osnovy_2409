# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_numbers(numbers):
    """Calculates the sum of all numbers in the argument until the character 'q' is entered

    Takes a string consisting of one or more float numbers separated by spaces.
    Returns a tuple consisting of a number (sum of numbers) and a bool True (if 'q' in  argument) or False (if not))"""
    numbers_list = numbers.split()
    func_result = 0
    for i in numbers_list:
        if i == 'q':
            return func_result, True
        else:
            try:
                i = float(i)
            except ValueError:
                print(f'ValueError: "{i}" is not a number. You should enter numbers separated by spaces')
                continue
            else:
                func_result += i
    return func_result, False


if __name__ == '__main__':
    result = 0
    while True:
        numbers_input = input("Enter numbers separated by spaces: ")
        result_sum, ready_to_exit = sum_numbers(numbers_input)
        result += result_sum
        if not ready_to_exit:
            print(f'The sum of all entered numbers is {result}. You can continue typing. To exit enter "q"')
        else:
            print(f'The sum of all entered numbers is {result}. Counting  is over.')
            break
