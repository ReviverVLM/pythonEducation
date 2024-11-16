"""
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции будет простым числом
и "Составное" в противном случае.
"""


def is_prime(func):
    def wrapper(a, b, c):
        result = func(a, b, c)
        if result == 1:
            print('Результат единица')
        elif result == 2 or result == 3 or result == 5 or result == 7:
            print('Простое')
            return result
        else:
            if result % 2 == 0 or result % 3 == 0 or result % 5 == 0 or result % 7 == 0:
                print('Составное')
                return result
            else:
                print('Простое')
                return result
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


print(sum_three(4, 5, 7))



