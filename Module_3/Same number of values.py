"""
Задача "Однокоренные":
Напишите функцию single_root_words, которая принимает одно обязательное слово в параметр root_word,
а далее неограниченную последовательность в параметр *other_words.
Функция должна составить новый список same_words только из тех слов списка other_words,
которые содержат root_word или наоборот root_word содержит одно из этих слов.
После вернуть список same_words в качестве результата своей работы.
"""


def single_root_words(root_word, *other_words):
    root_words = []
    for word in other_words:
        if word.lower() in root_word.lower() or root_word.lower() in word.lower():
            root_words.append(word)
        else:
            continue
    return root_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
result3 = single_root_words(input("Введите любое слово из словаря Даля: "), "Мику", "Микуська", "Микусёныш",
                            "Подмикунь", "Мика", "Мизантроп", *["милиция", "Miku", "мику", "лук-порей"])
print(result1)
print(result2)
print(result3)
