# 3. Создайте собственный класс-исключение, который должен проверять
# содержимое списка на наличие только чисел. Проверить работу исключения
# на реальном примере. Необходимо запрашивать у пользователя данные и
# заполнять список. Класс-исключение должен контролировать типы данных
# элементов списка.
# Примечание: длина списка не фиксирована. Элементы запрашиваются
# бесконечно, пока пользователь сам не остановит работу скрипта, введя,
# например, команду “stop”. При этом скрипт завершается, сформированный
# список выводится на экран.
# Подсказка: для данного задания примем, что пользователь может вводить
# только числа и строки. При вводе пользователем очередного элемента
# необходимо реализовать проверку типа элемента и вносить его в список,
# только если введено число. Класс-исключение должен не позволить
# пользователю ввести текст (не число) и отобразить соответствующее
# сообщение. При этом работа скрипта не должна завершаться.

class NotInt(Exception):
    def __init__(self, text):
        self.text = text


class CreateList:
    def __init__(self):
        self._created_list = []
        number = 0
        while number != 'stop':
            number = input('Enter a number: ')
            if number == 'stop':
                continue
            try:
                self._add_a_number(self._created_list, number)
            except NotInt as err:
                print(err)
                continue

    @staticmethod
    def _add_a_number(list, number):
        if not number.isdigit():
            raise NotInt('Input is not an integer')
        list.append(int(number))

    @property
    def result_list(self):
        return self._created_list


a = CreateList()
print(a.result_list)
