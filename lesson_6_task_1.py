# 1. Создать класс TrafficLight (светофор) и определить у него один
# атрибут color (цвет) и метод running (запуск). Атрибут реализовать
# как приватный. В рамках метода реализовать переключение светофора в
# режимы: красный, желтый, зеленый. Продолжительность первого состояния
# (красный) составляет 7 секунд, второго (желтый) — 2 секунды, третьего
# (зеленый) — на ваше усмотрение. Переключение между режимами должно
# осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.

from time import sleep


class TrafficLight:
    __colour = ['red', 'yellow', 'green', 'yellow']

    def running(self):
        for colour in TrafficLight.__colour:
            self.__colour = colour
            self._change_colour(self.__colour)

    @staticmethod
    def _change_colour(colour):
        colour_time_dict = {'red': 7, 'yellow': 2, 'green': 10}
        print(f'Change to color {colour}')
        sleep(1)
        for time in range(colour_time_dict[colour]):
            print(colour)
            sleep(1)


if __name__ == '__main__':
    a = TrafficLight()
    a.running()
