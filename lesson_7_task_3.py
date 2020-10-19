# 3. Реализовать программу работы с органическими клетками. Необходимо
# создать класс Клетка. В его конструкторе инициализировать параметр,
# соответствующий количеству клеток (целое число). В классе должны быть
# реализованы методы перегрузки арифметических операторов: сложение
# (__add__()), вычитание (__sub__()), умножение (__mul__()), деление
# (__truediv__()).Данные методы должны применяться только к клеткам и
# выполнять увеличение, уменьшение, умножение и обычное
# (не целочисленное) деление клеток, соответственно. В методе деления
# должно осуществляться округление значения до целого числа.
# Сложение. Объединение двух клеток. При этом число ячеек общей клетки
# должно равняться сумме ячеек исходных двух клеток.
# Вычитание. Участвуют две клетки. Операцию необходимо выполнять только
# если разность количества ячеек двух клеток больше нуля, иначе выводить
# соответствующее сообщение.
# Умножение. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как произведение количества ячеек этих двух клеток.
# Деление. Создается общая клетка из двух. Число ячеек общей клетки
# определяется как целочисленное деление количества ячеек этих двух
# клеток.
# В классе необходимо реализовать метод make_order(), принимающий
# экземпляр класса и количество ячеек в ряду. Данный метод позволяет
# организовать ячейки по рядам.
# Метод должен возвращать строку вида *****\n*****\n*****..., где
# количество ячеек между \n равно переданному аргументу. Если ячеек на
# формирование ряда не хватает, то в последний ряд записываются все
# оставшиеся.
# Например, количество ячеек клетки равняется 12, количество ячеек в
# ряду — 5. Тогда метод make_order() вернет строку: *****\n*****\n**.
# Или, количество ячеек клетки равняется 15, количество ячеек в ряду — 5.
# Тогда метод make_order() вернет строку: *****\n*****\n*****.

class Cell:
    def __init__(self, nucleus_count):
        if isinstance(nucleus_count, int):
            self.nucleus_count = nucleus_count
        else:
            raise TypeError(f'Invalid argument: must be int')

    def __str__(self):
        return f'Cell({len(self)})'

    def __len__(self):
        return self.nucleus_count

    def __add__(self, other):
        if isinstance(other, Cell):
            return Cell(len(self) + len(other))
        else:
            raise TypeError(f'Invalid argument: must be Cell')

    def __sub__(self, other):
        if isinstance(other, Cell):
            if len(self) != len(other):
                return Cell(abs(len(self) - len(other)))
            else:
                print('Cells are the same')
        else:
            raise TypeError(f'Invalid argument: must be Cell')

    def __mul__(self, other):
        if isinstance(other, Cell):
            return Cell(len(self) * len(other))
        else:
            raise TypeError(f'Invalid argument: must be Cell')

    def __truediv__(self, other):
        if isinstance(other, Cell):
            result = max(len(self), len(other)) / \
                     min(len(self), len(other))
            return Cell(round(result))
        else:
            raise TypeError(f'Invalid argument: must be Cell')

    def make_order(self, row_length):
        result = ''
        for i in range(len(self)):
            result += '*\n' if (i + 1) % row_length == 0 else '*'
        return result


a = Cell(3)
b = Cell(4)
c = Cell(5)
d = Cell(6)
new = a * c

print(a * b)
print(c + d)
print(b - c)
print(d / a)
print(new)
print(new.make_order(3))
print(a.make_order(3))


