"""
Напиши функцию get_multiplied_digits,
которая принимает аргумент целое число number и подсчитывает произведение цифр этого числа.
"""


def get_multiplied_digits(number):  # Незабываемая рекурсия
    result = number % 10
    if number < 10:
        return result
    elif result == 0:
        return get_multiplied_digits(number // 10)
    else:
        return result * get_multiplied_digits(number // 10)


print(get_multiplied_digits(21264))
"""
Можно решить данное задание и через строку с выдёргиванием последнего элемента,
но это долго, муторно и не совсем оптимально
"""
# def get_multiplied_digits_other_way(number):
#     str_number = str(number)
#     print(str_number.pop())