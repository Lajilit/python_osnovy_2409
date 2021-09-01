# 4. Реализуйте базовый класс Car. У данного класса должны быть
# следующие атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction), которые должны сообщать,
# что машина поехала, остановилась, повернула (куда). Опишите несколько
# дочерних классов: TownCar, SportCar, WorkCar, PoliceCar. Добавьте в
# базовый класс метод show_speed, который должен показывать текущую
# скорость автомобиля. Для классов TownCar и WorkCar переопределите
# метод show_speed. При значении скорости свыше 60 (TownCar) и 40
# (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов. Выполните
# доступ к атрибутам, выведите результат. Выполните вызов методов и
# также покажите результат.

class Car:
    speed = 0
    is_police = False

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def go(self, speed):
        print(f'{self.name} is moving')
        self.speed = speed

    def stop(self):
        print(f'{self.name} stopped')
        self.speed = 0

    def turn(self, direction):
        directions = ('left', 'right', 'back')
        if direction in directions:
            print(f'{self.name} turns {direction}')
        else:
            print('Wrong direction!')

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')


class TownCar(Car):
    def __init__(self, name, color, body='sedan'):
        super().__init__(name, color)
        self.body = body

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')
        if self.speed >= 60:
            print('Attention! Speeding!')


class WorkCar(Car):
    def __init__(self, name, color, model='work car'):
        super().__init__(name, color)
        self.model = model

    def show_speed(self):
        print(f'{self.name} speed is {self.speed}')
        if self.speed >= 40:
            print('Attention! Speeding!')

        
class SportCar(Car):
    def __init__(self, name, color, model='sport car'):
        super().__init__(name, color)
        self.model = model
        

class PoliceCar(Car):
    is_police = True
    
    def __init__(self, name, color, body='sedan'):
        super().__init__(name, color)
        self.body = body


car = Car('Star', 'blue')
print(car.__dict__)

town_car = TownCar('Tony', 'red')
print(town_car.__dict__)

worker = WorkCar('Greg', 'green', 'tractor')
print(worker.__dict__)

sport_car = SportCar('Train A', 'yellow', 'porsche')
print(sport_car.__dict__)

police_car = PoliceCar('Jonny', 'black')
print(police_car.__dict__)


car.go(60)
car.turn('right')

town_car.go(70)
town_car.stop()
town_car.show_speed()

worker.go(80)
worker.show_speed()

sport_car.go(90)
sport_car.show_speed()

police_car.go(100)
print(police_car.is_police)
