"""
Напишите функцию-генератор all_variants(text), которая принимает строку text и возвращает объект-генератор,
при каждой итерации которого будет возвращаться подпоследовательности переданной строки.
"""


def all_variants(text):
    start = 0
    end = 1
    counter = 1
    while counter <= len(text):
        if start < end:
            yield text[start:end]
            start, end = start + 1, end + 1
        if len(text) < end:
            start = 0
            counter += 1
            end = counter


result = all_variants("abcd")
for char in result:
    print(char)
