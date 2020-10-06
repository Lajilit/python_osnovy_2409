# 4. Представлен список чисел. Определить элементы списка, не имеющие
# повторений. Сформировать итоговый массив чисел, соответствующих
# требованию. Элементы вывести в порядке их следования в исходном
# списке. Для выполнения задания обязательно использовать генератор
# списка. (Можно использовать list.count()).
# Пример исходного списка: [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11].
# Результат: [23, 1, 3, 10, 4, 11]
from collections import OrderedDict

list_1 = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
dict_1 = OrderedDict()

for i in list_1:
    if i not in dict_1:
        dict_1[i] = 1
    else:
        dict_1[i] +=1
list_2 = [i for i in dict_1 if dict_1[i] == 1]
print(list_2)
