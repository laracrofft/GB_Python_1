# Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также класс «Оргтехника»,
# который будет базовым для классов-наследников. Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.

# Продолжить работу над первым заданием. Разработать методы, отвечающие за приём оргтехники на склад и передачу в
# определенное подразделение компании. Для хранения данных о наименовании и количестве единиц оргтехники,
# а также других данных, можно использовать любую подходящую структуру, например словарь.

# Продолжить работу над вторым заданием. Реализуйте механизм валидации вводимых пользователем данных.
# Например, для указания количества принтеров, отправленных на склад, нельзя использовать строковый тип данных.

class YearError(Exception):
    txt = 'Товар устарел'

    def __str__(self):
        return self.txt


class Warehouse:
    def __init__(self):
        self._dict = {}
        self._out = {}

    def add_to(self, equipment):
        self._dict.setdefault(equipment.group_name(), []).append(equipment)

    def extract(self, name):
        if self._dict[name]:
            self._dict.setdefault(name).pop(0)


class Tech:
    def __init__(self, name, make, year):
        self.name = name
        self.make = make
        self.year = year
        self.group = self.__class__.__name__

    def group_name(self):
        return f'{self.group}'

    def __repr__(self):
        try:
            if self.year <= 2000:
                raise YearError
            else:
                return f'{self.name} {self.make} {self.year}'
        except YearError as e:
            print(e)


class Printer(Tech):
    def __init__(self, series, name, make, year):
        super().__init__(name, make, year)
        self.series = series

    def action(self):
        return 'Печатает'


class Scanner(Tech):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Сканирует'


class Copier(Tech):
    def __init__(self, name, make, year):
        super().__init__(name, make, year)

    def action(self):
        return 'Копирует'


warehouse = Warehouse()
scanner = Scanner('hp', '321', 2020)
warehouse.add_to(scanner)
scanner = Scanner('canon', '311', 2014)
warehouse.add_to(scanner)
scanner = Scanner('epson', '330', 2020)
warehouse.add_to(scanner)
printer = Printer('e-320', 'sony', 126, 2018)
warehouse.add_to(printer)
copier = Copier('xerox', '201', 2018)
warehouse.add_to(copier)
print(f'На склад поступили: {warehouse._dict}')
warehouse.extract('Scanner')
print(f'Остаток на складе: {warehouse._dict}')
