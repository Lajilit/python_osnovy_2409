# 7. Реализовать проект «Операции с комплексными числами». Создайте
# класс «Комплексное число», реализуйте перегрузку методов сложения и
# умножения комплексных чисел. Проверьте работу проекта, создав
# экземпляры класса (комплексные числа) и выполнив сложение и умножение
# созданных экземпляров. Проверьте корректность полученного результата.

class MyComplex:
    def __init__(self, real_part, imaginary_part):
        self.check_numbers(real_part, imaginary_part)
        self.real = real_part
        self.imaginary = imaginary_part

    def __str__(self):
        if self.imaginary > 0:
            return f'{self.real}+{self.imaginary}i'
        elif self.imaginary == 0:
            return f'{self.real}'
        elif self.imaginary < 0:
            return f'{self.real}-{abs(self.imaginary)}i'

    def __add__(self, other):
        if isinstance(other, MyComplex):
            result_real = self.real + other.real
            result_imaginary = self.imaginary + other.imaginary
            return MyComplex(result_real, result_imaginary)
        elif isinstance(other, (int, float)):
            result_real = self.real + other
            return MyComplex(result_real, self.imaginary)
        else:
            raise TypeError(f'unsupported operand type(s)'
                            f' +: "MyComplex" and "{type(other)}"')

    def __mul__(self, other):
        if isinstance(other, MyComplex):
            result_real = self.real * other.real - \
                          self.imaginary * other.imaginary
            result_imaginary = self.real * other.imaginary + \
                               self.imaginary * other.real
            return MyComplex(result_real, result_imaginary)
        elif isinstance(other, (int, float)):
            result_real = self.real * other
            result_imaginary = self.imaginary * other
            return MyComplex(result_real, result_imaginary)
        else:
            raise TypeError(f'unsupported operation'
                            f' +: "{type(self)}" and "{type(other)}"')

    @staticmethod
    def check_numbers(real_part, imaginary_part):
        if not isinstance(real_part, (int, float)):
            raise ValueError('Real part must be int or float')
        if not isinstance(imaginary_part, (int, float)):
            raise ValueError('Imaginary part must be int or float')
        return real_part, imaginary_part


if __name__ == '__main__':
    a = MyComplex(3, 4)
    print(a)
    b = MyComplex(2, 5)
    print(b)
    print('*' * 10)
    c = a + b
    d = a + 3
    print(c)
    print(d)
    print('*' * 10)
    e = c * d
    f = d * 3
    print(e)
    print(f)
