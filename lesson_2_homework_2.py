# 2. Для списка реализовать обмен значений соседних элементов, т.е. Значениями обмениваются элементы с индексами 0 и
# 1, 2 и 3 и т.д. При нечетном количестве элементов последний сохранить на своем месте. Оформите обмен, как функцию.
# Исходные списки можете инициализировать прямо в коде, но обязательно проверьте работоспособность, для пустого
# списка, списка из 1 элемента, списка с четным количеством элементов и с нечетным.


def list_element_exchange(my_list):
    length = len(my_list)
    if length == 0:
        print('Список пуст')
    elif length == 1:
        print(my_list)
    else:
        length = length if length % 2 == 0 else length - 1
        for i in range(length):
            if i % 2 == 0:
                my_list[i], my_list[i + 1] = my_list[i + 1], my_list[i]
        print(my_list)


if __name__ == '__main__':
    list_element_exchange([1, 2, 3, 4, 5, 6, 7, 8])
    list_element_exchange([1, 2, 3, 4, 5, 6, 7])
    list_element_exchange([1])
    list_element_exchange([])
