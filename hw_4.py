# Реализуйте базовый класс Car. У данного класса должны быть следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась,
# повернула (куда). Опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в базовый класс
# метод show_speed, который должен показывать текущую скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40 (WorkCar) должно выводиться сообщение о превышении
# скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.


class Car:
    def __init__(self, speed, color, name, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        print(f'{self.name} начал движение')

    def stop(self):
        print(f'{self.name} остановился')

    def turn(self, direction):
        print(f'{self.name} повернул {direction}')

    def show_speed(self):
        print(f'Скорость {self.name} составляет {self.speed}')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышена и составляет {self.speed}')
        else:
            print(f'Скорость {self.name} в пределах нормы и составляет {self.speed}')


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 40:
            print(f'Скорость {self.name} превышена и составляет {self.speed}')
        else:
            print(f'Скорость {self.name} в пределах нормы и составляет {self.speed}')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def police(self):
        if self.is_police:
            print(f'Автомобиль {self.name} является полицеским')
        else:
            print(f'Автомобиль {self.name} не является полицеским')


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)

    def show_speed(self):
        if self.speed > 60:
            print(f'Скорость {self.name} превышена и составляет {self.speed}')
        else:
            print(f'Скорость {self.name} в пределах нормы и составляет {self.speed}')


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)


bmw = SportCar(100, 'Красный', 'BMW', False)
kalina = TownCar(90, 'Желтый', 'Kalina', False)
kia = WorkCar(70, 'Серебристый', 'Ceed', False)
ford = PoliceCar(110, 'Черный', 'Ford', True)

bmw.turn('налево')
ford.police()
kalina.show_speed()
kia.go()
