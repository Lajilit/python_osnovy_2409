# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку
# конструктора класса (метод __init__()), который должен принимать
# данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода
# матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции
# сложения двух объектов класса Matrix (двух матриц). Результатом
# сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый
# элемент первой строки первой матрицы складываем с первым элементом
# первой строки второй матрицы и т.д.


class Matrix:
    def __init__(self, list_list):
        self._matrix = list_list
        self.length = len(self._matrix[0])
        self.height = len(self._matrix)

    def __len__(self):
        return self.length * self.height

    def __str__(self):
        result = ''
        for line in self._matrix:
            line = [str(i) for i in line]
            m_string = ' '.join(line)
            result += m_string + '\n'
        return result

    def __add__(self, other):
        if isinstance(other, Matrix):
            if self.length == other.length and self.height == other.height:
                result = []
                for index_line in range(self.height):
                    lst = []
                    for index_number in range(self.length):
                        lst.append(
                            self._matrix[index_line][index_number] + \
                            other._matrix[index_line][index_number]
                        )
                    result.append(lst)

                return Matrix(result)
            else:
                print('Matrix sizes must be the same')
        #  далее необязательная часть, которая, возможно, работает не так,
        #  как должно работать сложение числа с матрицей. Но я решила
        #  потренироваться, и получилось, что получилось. В данном коде
        #  прибавляется число к каждому элементу матрицы
        elif isinstance(other, int):
            result = []
            for line in self._matrix:
                lst = []
                for i in line:
                    lst.append(i + other)
                result.append(lst)
            return Matrix(result)
        else:
            print('The argument must be int or Matrix()')
# вместо print во всех случаях можно сделать генерацию исключений, но тогда
# нужно будет делать ещё и их обработку,а у меня на это уже нет сил


if __name__ == '__main__':
    a = Matrix([[1, 2, 3, 4], [5, 6, 7, 8]])
    b = Matrix([[9, 10, 11, 12], [13, 14, 15, 16]])

    print(a)
    print(b)
    print(a+b)
    print(a+3)
