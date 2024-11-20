"""
Задача "За честь и отвагу!":
Создайте класс Knight, наследованный от Thread, объекты которого будут обладать следующими свойствами:
Атрибут name - имя рыцаря. (str)
Атрибут power - сила рыцаря. (int)

А также метод run, в котором рыцарь будет сражаться с врагами:
При запуске потока должна выводится надпись "<Имя рыцаря>, на нас напали!".
Рыцарь сражается до тех пор, пока не повергнет всех врагов (у всех потоков их 100).
В процессе сражения количество врагов уменьшается на power текущего рыцаря.

По прошествию 1 дня сражения (1 секунды) выводится строка
"<Имя рыцаря> сражается <кол-во дней>..., осталось <кол-во воинов> воинов."

После победы над всеми врагами выводится надпись "<Имя рыцаря> одержал победу спустя <кол-во дней> дней(дня)!"
"""
import threading
import time


class Knight(threading.Thread):
    def __init__(self, name, power):
        super().__init__()
        self.name = name
        self.power = power

    def run(self):
        print(f'{self.name}, на нас напали!')
        enemy = 100
        days = 0
        while enemy:
            time.sleep(1)
            days += 1
            enemy -= self.power
            print(f'{self.name} сражается {days} дней. Осталось {enemy} воинов сопротивления ')
        print(f'{self.name} одержал победу спустя {days} дней(дня)')


first_knight = Knight('Sir Lancelot', 10)
second_knight = Knight("Sir Galahad", 20)

defenders = [first_knight, second_knight]

for knight in defenders:
    knight.start()

for knight in defenders:
    knight.join()


