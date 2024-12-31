"""
Необходимо создать функцию, которая принимает объект (любого типа) в качестве аргумента
и проводит интроспекцию этого объекта, чтобы определить его тип, атрибуты, методы, модуль, и другие свойства.

1. Создайте функцию introspection_info(obj), которая принимает объект obj.
2. Используйте встроенные функции и методы интроспекции Python для получения информации о переданном объекте.
3. Верните словарь или строки с данными об объекте, включающий следующую информацию:
  - Тип объекта.
  - Атрибуты объекта.
  - Методы объекта.
  - Модуль, к которому объект принадлежит.
"""
import inspect
from Module_6.M6_2 import Vehicle

car = Vehicle("Miku", "Toyota", "голубой", 3939)


def introspection_info(obj):
    # Получаем и выводим тип объекта
    obj_type = type(obj)
    print(f"Тип объекта: {obj_type}")

    # Получаем и выводим все атрибуты и методы объекта
    obj_dir = dir(obj)
    print("\nАтрибуты и методы объекта:")
    for item in obj_dir:
        print(item)

    # Получаем и выводим все члены объекта
    obj_members = inspect.getmembers(obj)
    print("\nЧлены объекта:")
    for name, value in obj_members:
        print(f"{name}: {value}")

    # Получаем и выводим модуль, к которому принадлежит объект
    obj_module = inspect.getmodule(obj)
    print(f"\nМодуль: {obj_module.__name__ if obj_module else 'Неизвестный модуль'}")


if __name__ == '__main__':
    introspection_info(car)

