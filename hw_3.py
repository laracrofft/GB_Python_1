# Реализовать базовый класс Worker (работник), в котором определить атрибуты:
# name, surname, position (должность), income (доход). Последний атрибут должен быть защищенным и ссылаться на словарь,
# содержащий элементы: оклад и премия, например, {"wage": wage, "bonus": bonus}.
# Создать класс Position (должность) на базе класса Worker. В классе Position реализовать методы получения
# полного имени сотрудника (get_full_name) и дохода с учетом премии (get_total_income).
# Проверить работу примера на реальных данных (создать экземпляры класса Position, передать данные,
# проверить значения атрибутов, вызвать методы экземпляров).


class Worker:
    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"Оклад": wage, "Премия": bonus}


class Position(Worker):
    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)
        self.__income = {"Оклад": wage, "Премия": bonus}

    def get_full_name(self):
        print(f'{self.position} {self.name} {self.surname}')

    def get_total_income(self):
        print(f'Доход с учетом премии составляет: {sum(self.__income.values())}')


developer = Position('Рик', 'Санчез', 'Младший разработчик', 100000, 20000)
developer.get_full_name()
developer.get_total_income()

