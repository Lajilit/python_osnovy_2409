# 5. Программа запрашивает у пользователя строку чисел, разделенных пробелом. При нажатии Enter должна выводиться
# сумма чисел. Пользователь может продолжить ввод чисел, разделенных пробелом и снова нажать Enter. Сумма вновь
# введенных чисел будет добавляться к уже подсчитанной сумме. Но если вместо числа вводится специальный символ,
# выполнение программы завершается. Если специальный символ введен после нескольких чисел, то вначале нужно добавить
# сумму этих чисел к полученной ранее сумме и после этого завершить программу.


def sum_numbers(numbers):
    numbers_list = numbers.split()
    func_result = 0
    try:
        for i in range(len(numbers_list)):
            if numbers_list[i] == 'q':
                return [func_result, 'q']
            else:
                numbers_list[i] = float(numbers_list[i])
                func_result += numbers_list[i]
    except ValueError:
        return 'ValueError: you should enter numbers separated by spaces'
    else:
        return func_result


if __name__ == '__main__':
    result = 0
    while True:
        numbers_input = input("Enter numbers separated by spaces: ")
        a = sum_numbers(numbers_input)
        if type(a) is list:
            result += a[0]
            print(f'The sum of all entered numbers is {result}. Counting  is over.')
            break
        elif type(a) is str:
            print(a)
        else:
            result += a
            print(f'The sum of all entered numbers is {result}. You can continue typing. To exit enter "q"')
