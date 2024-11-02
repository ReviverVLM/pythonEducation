"""
Напишите функцию apply_all_func(int_list, *functions), которая принимает параметры:

int_list - список из чисел (int, float)
*functions - неограниченное кол-во функций (которые применимы к спискам, состоящим из чисел)

Эта функция должна:
-Вызвать каждую функцию к переданному списку int_list
-Возвращать словарь, где ключом будет название вызванной функции, а значением - её результат работы со списком int_list.
"""


def apply_all_func(int_list, *functions):
    result_dict = {}
    for function in functions:
        result_dict.update({function.__name__: function(int_list)})
    return result_dict


print(apply_all_func([6, 20, 15, 9], max, min))
print(apply_all_func([6, 20, 15, 9], len, sum, sorted))
