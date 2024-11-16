"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
"""


def all_variants(text):
    def path_string(string, start, end):
        return string[start:end]
    for first in range(len(text)+1):
        for second in range(len(text)+1):
            if second > first:
                yield path_string(text, first, second)


# def sorted_all_variants(text):
#     def path_string(string, start, end):
#         return string[start:end]
#     for first in range(len(text)+1):
#         for second in range(len(text)+1):
#             if second > first:
#                 yield path_string(text, first, second)

# yield string


result = all_variants("abcd")
for char in result:
    print(char)
