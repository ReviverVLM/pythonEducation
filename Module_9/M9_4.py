"""
Даны 2 строки
лямбда функция для:
list(map(?, first, second))
Результат - совпадение букв на той же позиции

Написать функцию get_advanced_writer(file_name)
Принимает название файла
Внутри функция write_everything(*data_set)
которая добавляет данные в файл file_name
get_advanced_writer возвращает write_everything

Создать класс MysticBall c атрибутом words
Определить метод __call__ который рандомит слово из words
"""
import random

first = 'Мама мыла раму'
second = 'Рамена мало было'

lambda_list = list(map(lambda first_char, second_char: first_char == second_char, first, second))
print(lambda_list)

"""+++"""


def get_advanced_writer(file_name):
    def write_everything(*data_set):
        with open(file_name, 'w', encoding="UTF-8") as file:
            for data in data_set:
                file.write(f'{data}\n')
    return write_everything


super_write = get_advanced_writer('text.txt')
res = [0, 'Enter', "Alou", 9, 'u']
super_write(lambda_list, res)

"""+++"""


class MysticBall:
    words = []

    def __init__(self, words):
        self.words = words

    def __call__(self):
        return random.choice(self.words)


data = ["Да", "Yes", "Конечно", "Точно", "U Best"]
mystic_rand = MysticBall(data)
print(mystic_rand(), end=' ')
print(mystic_rand(), end=' ')
print(mystic_rand(), end=' ')

