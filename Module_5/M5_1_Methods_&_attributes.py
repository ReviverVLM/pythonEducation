"""
Реализуйте класс House, объекты которого будут создаваться следующим образом:
House('ЖК Эльбрус', 30)
Объект этого класса должен обладать следующими атрибутами:
self.name - имя, self.number_of_floors - кол-во этажей
Также должен обладать методом go_to(new_floor), где new_floor - номер этажа(int), на который нужно приехать.
Метод go_to выводит на экран(в консоль) значения от 1 до new_floor(включительно).
Если же new_floor больше чем self.number_of_floors или меньше 1, то вывести строку "Такого этажа не существует".
"""
import time


class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor == 1:
            print("Вы уже на этом этаже")
        elif self.number_of_floors >= new_floor > 1:
            time.sleep(new_floor)
            print(f"Вы приехали на {new_floor} этаж")
        else:
            print("Такого этажа не существует или введены некоректные данные, попробуйте ещё раз")


village = House("Дача", 3)
urban = House("Городская многоэтажка", 10)

print(village.name, village.number_of_floors)
print(urban.name, urban.number_of_floors)

want_on_floor = 10
village.go_to(want_on_floor)
urban.go_to(want_on_floor)
village.go_to(want_on_floor)
