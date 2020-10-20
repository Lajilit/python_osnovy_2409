# 4. Начните работу над проектом «Склад оргтехники». Создайте класс,
# описывающий склад. А также класс «Оргтехника», который будет базовым
# для классов-наследников. Эти классы — конкретные типы оргтехники
# (принтер, сканер, ксерокс). В базовом классе определить параметры,
# общие для приведенных типов. В классах-наследниках реализовать
# параметры, уникальные для каждого типа оргтехники.

# 5. Продолжить работу над первым заданием. Разработать методы,
# отвечающие за приём оргтехники на склад и передачу в определенное
# подразделение компании. Для хранения данных о наименовании и
# количестве единиц оргтехники, а также других данных, можно
# использовать любую подходящую структуру, например словарь.

# 6. Продолжить работу над вторым заданием. Реализуйте механизм
# валидации вводимых пользователем данных. Например, для указания
# количества принтеров, отправленных на склад, нельзя использовать
# строковый тип данных.
# Подсказка: постарайтесь по возможности реализовать в проекте «Склад
# оргтехники» максимум возможностей, изученных на уроках по ООП.

class CapacityError(Exception):
    def __init__(self, text):
        self.text = text


class Storage:

    def __init__(self, capacity):
        if not isinstance(capacity, (int, float)):
            raise TypeError('Invalid data type. Capacity must be a number')
        elif capacity <= 0:
            raise ValueError('Capacity must > 0')
        self.capacity = capacity  # вместимость склада
        self.storage_content = {}

    def __str__(self):
        info_string = ''
        if self.storage_content:
            for k, v in self.storage_content.items():
                info_string += f' {k} ({v})\n'
            info_string = info_string.strip('\n')
            return f'Storage:\n{info_string}.\nCapacity is {self.capacity}'
        else:
            return f'The storage is empty. Capacity is {self.capacity}'

    @property
    def content(self):
        return self.__str__()

    def add_product(self, product):
        if self.capacity > 0:
            if not isinstance(product, OfficeEquipment):
                raise TypeError('Invalid data type. Product must be '
                                'OfficeEquipment')
            if product not in self.storage_content:
                self.storage_content[product] = 0
            if self.capacity < product.size:
                raise CapacityError(f'Too big to this storage. Capacity is'
                                    f' {self.capacity}')
            self.storage_content[product] += 1
            self.capacity -= product.size
            print(f'Added {product}')
            if self.capacity == 0:
                print('The storage is full')
        else:
            print('The storage is full')

    def remove_product(self, product):
        if not isinstance(product, OfficeEquipment):
            raise TypeError('Invalid data type. Product must be '
                            'OfficeEquipment')
        if product not in self.storage_content:
            print('There is no such product in storage')
        elif self.storage_content[product] == 0:
            print('There is no such product in storage')
            del self.storage_content[product]
        else:
            self.storage_content[product] -= 1
            self.capacity += product.size
            print(f'Removed {product}')


class OfficeEquipment:
    def __init__(self, model, size):
        model, size = self.validate_info(model, size)
        self.model = model
        self.size = size

    @staticmethod
    def validate_info(model, size):
        if not isinstance(model, str):
            raise TypeError('Invalid data type. Model must be a string')
        if not isinstance(size, (int, float)):
            raise TypeError('Invalid data type. Size must be a number')
        return model, size

    def __str__(self):
        return f'OfficeEquipment {self.model}'


class Printer(OfficeEquipment):
    name = 'Printer'

    def __init__(self, model, size, printer_type):
        super().__init__(model, size)
        if printer_type not in ('multicolor', 'black/white'):
            raise TypeError('''Invalid data type. Print_type must be 
                            'multicolor' or 'black/white'.''')
        self.type = printer_type

    def __str__(self):
        return f'Printer {self.model}'


class Scanner(OfficeEquipment):
    name = 'Scanner'

    def __init__(self, model, size, scanner_type):
        super().__init__(model, size)
        if scanner_type not in ('multicolor', 'black/white'):
            raise TypeError('''Invalid data type. Type must be 
                            'multicolor' or 'black/white'.''')
        self.type = scanner_type

    def __str__(self):
        return f'Scanner {self.model}'


class Computer(OfficeEquipment):
    name = 'Computer'

    def __init__(self, model, size, computer_type):
        super().__init__(model, size)
        if computer_type not in ('PC', 'laptop', 'monoblock'):
            raise TypeError('''Invalid data type. Type must be 
                            'PC', 'laptop' or 'monoblock'.''')
        self.type = computer_type

    def __str__(self):
        return f'Computer {self.model}'


a = OfficeEquipment('abc-08', 3)
print(a)
b = Printer('abc-09', 5, 'black/white')
print(b)
c = Scanner('asd123', 1, 'multicolor')
print(c)
d = Computer('123', 2, 'laptop')
print(d)

e = Storage(1000)
print(e.content)
print('_' * 10)
e.add_product(a)
print('_' * 10)
print(e.content)
print('_' * 10)
e.add_product(b)
print('_' * 10)
print(e.content)
print('_' * 10)
e.add_product(c)
print('_' * 10)
print(e.content)
print('_' * 10)
e.add_product(d)
e.add_product(d)
e.add_product(d)
print('_' * 10)
print(e.content)
print('_' * 10)
print('_' * 10)
e.remove_product(d)
print(e.content)
print('_' * 10)
e.remove_product(d)
e.remove_product(d)
e.remove_product(d)
print(e.content)
