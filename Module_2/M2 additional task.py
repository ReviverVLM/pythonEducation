# Вы отправились в путешествие на необитаемый остров и конечно же в очередной вылазке в джунгли
# вы попали в ловушку местному племени (да-да, классика "Индиана Джонса").
# К вашему удивлению, в племени были неплохие математики и по совместительству фантазёры.
# Вы поняли это, когда после долгих блужданий перед вами появились ворота (выход из ловушки)
# с двумя каменными вставками для чисел.
# В первом поле камни с числом менялись постоянно (от 3 до 20) случайным образом, а второе было всегда пустым.
#
#
# Во вторую вставку нужно было написать те пары чисел друг за другом,
# чтобы число из первой вставки было кратно(делилось без остатка) сумме их значений.
#
# Пример кратности(деления без остатка):
# 1 + 2 = 3 (сумма пары)
# 9 / 3 = 3 (ровно 3 без остатка)
# 9 кратно 3 (9 делится на 3 без остатка)
#
#
# Пример 1:
# 9 - число из первой вставки
# 1218273645 - нужный пароль (1 и 2, 1 и 8, 2 и 7, 3 и 6, 4 и 5 - пары; число 9 кратно сумме каждой пары)
#
# Пример 2:
# 11 - число из первой вставки
# 11029384756 - нужный пароль (1 и 10, 2 и 9, 3 и 8, 4 и 7, 5 и 6 - пары; число 11 кратно сумме каждой пары)
#
#
# Составьте алгоритм, используя циклы, чтобы в независимости от введённого числа n (от 3 до 20)
# программа выдавала нужный пароль result, для одного введённого числа.

def generate_list_of_numbers(max_value):
    list_of_numbers = []
    for i in range(max_value):
        list_of_numbers.append(i+1)
    return list_of_numbers


def check_dublet(list_of_values, value):             # Функция проверки на дубликат пары
    result = False                                   # Изначально считаем, что дубля нет
    for i in range(list_of_values.__len__()):        # if set_result == set_check:
        if set(list_of_values[i]) == set(value):     # Условие для отсеивания дублирующей пары
            result = True                            # Если нашли дубль, говорим, что он есть
            break                                    # Ломаем(завершаем) цикл(дальнейший прогон не нужен)
    return result                                    # Возвращаем результат поисков(Да? Да Нет? Нет)


def pass_gen(n, max_value):
    result = []
    my_list = generate_list_of_numbers(max_value)
    # i, j = 1, 1
    # while i < n/2: <-- не использовать, идея провальная, работает наполовину(возможна доработка)
    for i in range(my_list.__len__()):
        if i > n:
            break
        for j in range(my_list.__len__()):
            number_main_cycle = my_list[i]
            number_insider_cycle = my_list[j]
            if number_main_cycle == number_insider_cycle:
                continue
            if n % (number_main_cycle + number_insider_cycle) == 0:
                pair = [number_main_cycle, number_insider_cycle]
                if result.__len__() == 0:
                    result.append([number_main_cycle, number_insider_cycle])
                    continue
                if check_dublet(result, pair):
                    continue
                else:
                    result.append([number_main_cycle, number_insider_cycle])
    return result    # result


print(*(pass_gen(15, 20)))
