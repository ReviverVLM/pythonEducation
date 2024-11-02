"""
Напишите 2 функции:

Функция personal_sum(numbers):
-Принимает коллекцию numbers
-Считает сумму чисел numbers перебором и увеличивает переменную result
-Если при переборе всречается не числовой тип, обработать исключение TypeError и увеличить счётчик
incorrect_data на 1
-Функция возвращает кортеж из двух значений - result сумма чисел
incorrect_data количество неверных данных

Функция calculate_average:
-Принимает коллекцию numbers
-возвращает среднее арифметическое
-Учесть нулевую коллекцию и обработать ZeroDivisionError, вернуть 0
-Учесть, что может быть передан неверный тип данных, обработать Type Error
"""


def personal_sum(numbers):
    result = 0
    incorrect_data = 0
    for number in numbers:
        try:
            result += number
        except TypeError:
            incorrect_data += 1
    return result, incorrect_data


def calculate_average(numbers):
    result = 0
    try:
        result = personal_sum(numbers)[0]/(len(numbers)-personal_sum(numbers)[1])
    except TypeError as exp:
        print(f"Принят неверный тип данных {exp}")
    except ZeroDivisionError:
        print("Коллекция пустая")
        return 0
    return result


data = (1, 3, 5, 7, 24, "Miku", "zzz", 20)
print(calculate_average(data))
print(personal_sum(data))
