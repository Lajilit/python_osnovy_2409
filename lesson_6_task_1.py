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
    _colors = ['red', 'yellow', 'green', 'yellow']
    _on_color = ''

    def running(self):
        for color in TrafficLight._colors:
            self._on_color = color
            self._change_colour(self._on_color)

    @staticmethod
    def _change_colour(color):
        colour_time_dict = {'red': 7, 'yellow': 2, 'green': 10}
        print(f'Change to color {color}')
        sleep(1)
        for time in range(colour_time_dict[color]):
            print(color)
            sleep(1)


if __name__ == '__main__':
    a = TrafficLight()
    a.running()
