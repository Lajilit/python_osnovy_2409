# 4. Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел, соответствующих
# требованию. Элементы вывести в порядке их следования в исходном
# списке. Для выполнения задания обязательно использовать генератор
# списка. (Можно использовать list.count()).
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]

list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
set_1 = set(list_1)
list_2 = list_1[:]
for i in set_1:
    if i in list_1:
        list_2.remove(i) # list_1 - set_1
print(list_2) # the non-unique elements
result_list = [i for i in list_1 if i not in list_2]
print(result_list)