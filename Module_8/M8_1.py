"""
Пора разрушать шаблоны привычного нам Python!
Вот вас раздражает, что мы не можем сложить число(int) и строку(str)? Давайте исправим это недоразумение!

Реализуйте следующую функцию:
add_everything_up, будет складывать числа(int, float) и строки(str)

Описание функции:
add_everything_up(a, b) принимает a и b, которые могут быть как числами(int, float), так и строками(str).
TypeError - когда a и b окажутся разными типами (числом и строкой),
то возвращать строковое представление этих двух данных вместе (в том же порядке).
Во всех остальных случаях выполнять стандартные действия.
"""


def add_everything_up(*params):
    sum_params = str()
    try:
        sum_params = round(sum(params), 5)
        # return sum_params
    except TypeError:
        for param in params:
            sum_params += str(param)
    except Exception as exp:
        return f"Нам ломают прогу ошибкой {exp}"
    else:
        print("Всё идёт по плану...хммм")
    finally:
        return sum_params


print(add_everything_up())
