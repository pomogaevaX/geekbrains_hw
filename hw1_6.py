# 1. Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running (запуск).
# Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы: красный, желтый,
# зеленый. Продолжительность первого состояния (красный) составляет 7 секунд, второго (желтый) — 2 секунды,
# третьего (зеленый) — на ваше усмотрение. Переключение между режимами должно осуществляться только в указанном
# порядке (красный, желтый, зеленый). Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
# сообщение и завершать скрипт.

import time
import sys

class TrafficLight:

    __colorSleep = {'red': 7, 'yellow': 2, 'green': 7}
    __colorOrder = {'red': ['yellow'], 'yellow': ['green', 'red'], 'green': ['yellow']}

    def __init__(self, firstColor):
        if self.__colorSleep.get(firstColor, -1) > 0:
            self.__color = firstColor
        else:
            print('Неверное значение')


    def running(self, newColor):
        if newColor in self.__colorOrder.get(self.__color):
            sleepTime = self.__colorSleep.get(newColor, -1)
            if sleepTime > 0:
                print(f'Поступила команда включить {newColor}')
                self.__color = newColor
                time.sleep(sleepTime)
                print(f'Свет включен {newColor}')
            else:
                print('Неверное значение')
                sys.exit()
        else:
            print('Неверная последовательность')
            sys.exit()


a = TrafficLight('red')
a.running('yellow')
a.running('green')
a.running('yellow')
a.running('green')
a.running('red')



