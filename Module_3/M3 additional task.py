"""
Задание "Раз, два, три, четыре, пять .... Это не всё?"

Что должно быть подсчитано:
Все числа (не важно, являются они ключами или значениям или ещё чем-то).
Все строки (не важно, являются они ключами или значениям или ещё чем-то)

Для примера, указанного выше, расчёт вёлся следующим образом:
1 + 2 + 3 + len('a') + 4 + len('b') + 5 + 6 + len('cube') + 7 + .... + 35 = 99

Входные данные (применение функции):
data_structure = [
[1, 2, 3],
{'a': 4, 'b': 5},
(6, {'cube': 7, 'drum': 8}),
"Hello",
((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)


Выходные данные (консоль):
99
"""

# def dict_to_list(argument):
#     dict_list = []
#     for key in argument:
#         dict_list.append(key)
#         dict_list.append(argument[key])
#     return dict_list
#
#
# print(dict_to_list({'cube': 7, 'drum': 8}))
"""Оптимизировано до *argument.items(). Без распаковки не работает. 

Пояснение нейросетки: 
 Проблема заключается в том, что argument.items() возвращает объект dict_items, который не может быть непосредственно
 распакован в sum_of_computer_types. Это приведет к ошибке, так как функция ожидает, что 
 аргументы будут переданы в виде отдельных элементов, а не в виде итератора.
 
 Вкратце isinstance(argument.items(), object) == True. Это итерируемый объект
 
 Дополнение: ошибка не выдаётся, но пропускается
"""


def sum_of_computer_types(*args):
    result = 0
    for argument in args:
        if isinstance(argument, (tuple, list, set)):
            result += sum_of_computer_types(*argument)
        elif isinstance(argument, dict):
            result += sum_of_computer_types(*argument.items())
        elif isinstance(argument, int):
            result += argument
        elif isinstance(argument, str):
            result += len(argument)
    return result


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]
# print(sum_of_computer_types([1, 2, 2], [2, 3]))
print(sum_of_computer_types(*data_structure))
