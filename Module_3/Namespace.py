# Порой необходимо отслеживать, сколько раз вызывалась та или иная функция.
# К сожалению, в Python не предусмотрен подсчёт вызовов автоматически.
# Давайте реализуем данную фишку самостоятельно!
#
# Вам необходимо написать 3 функции:
# Функция count_calls подсчитывающая вызовы остальных функций.
# Функция string_info принимает аргумент - строку и возвращает кортеж из:
# длины этой строки, строку в верхнем регистре, строку в нижнем регистре.
# Функция is_contains принимает два аргумента: строку и список, и возвращает True, если строка находится в этом списке,
# False - если отсутствует. Регистром строки при проверке пренебречь: UrbaN ~ URBAN.
# Пункты задачи:
# Создать переменную calls = 0 вне функций.
# Создать функцию count_calls и изменять в ней значение переменной calls.
# Эта функция должна вызываться в остальных двух функциях.
# Создать функцию string_info с параметром string и реализовать логику работы по описанию.
# Создать функцию is_contains с двумя параметрами string и list_to_search, реализовать логику работы по описанию.
# Вызвать соответствующие функции string_info и is_contains произвольное кол-во раз с произвольными данными.
# Вывести значение переменной calls на экран(в консоль).

functions_calls = 0


def count_calls():
    global functions_calls
    functions_calls += 1


def string_info(string=''):
    count_calls()
    mod_string = (string.lower(), string.upper(), string.__len__())
    return mod_string


def is_contains(string, verifying_list):
    count_calls()
    contain = False
    for checking_string in verifying_list:
        if checking_string.lower() == string.lower():
            contain = True
            break
    return contain


print(string_info('Miku'))
print(string_info('Kaito'))
print(string_info('Meiko'))
print(string_info("Роса"))
print(string_info("初音ミク"))
print(is_contains('Miku', ['MikU', 'Micke', 'Maik']))
print(is_contains('Meiko', ['MikU', 'Micke', 'MeiKo']))
print(functions_calls)
