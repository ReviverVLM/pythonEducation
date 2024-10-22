"""
Задача "Найдёт везде":

Напишите класс WordsFinder, объекты которого создаются следующим образом:
WordsFinder('file1.txt, file2.txt', 'file3.txt', ...).
Объект этого класса должен принимать при создании неограниченного количество названий файлов
и записывать их в атрибут file_names в виде списка или кортежа.

Также объект класса WordsFinder должен обладать следующими методами:

get_all_words - подготовительный метод, который возвращает словарь следующего вида:
{'file1.txt': ['word1', 'word2'], 'file2.txt': ['word3', 'word4'], 'file3.txt': ['word5', 'word6', 'word7']}
Где:
'file1.txt', 'file2.txt', ''file3.txt'' - названия файлов.
['word1', 'word2'], ['word3', 'word4'], ['word5', 'word6', 'word7'] - слова содержащиеся в этом файле.

Алгоритм получения словаря такого вида в методе get_all_words:
Создайте пустой словарь all_words.
Переберите названия файлов и открывайте каждый из них, используя оператор with.
Для каждого файла считывайте единые строки, переводя их в нижний регистр (метод lower()).
Избавьтесь от пунктуации [',', '.', '=', '!', '?', ';', ':', ' - '] в строке.
(тире обособлено пробелами, это не дефис в слове).
Разбейте эту строку на элементы списка методом split(). (разбивается по умолчанию по пробелу)
В словарь all_words запишите полученные данные, ключ - название файла, значение - список из слов этого файла.

find(self, word) - метод, где word - искомое слово.
Возвращает словарь, где ключ - название файла, значение - позиция первого такого слова в списке слов этого файла.
count(self, word) - метод, где word - искомое слово.
Возвращает словарь, где ключ - название файла, значение - количество слова word в списке слов этого файла.
В методах find и count пользуйтесь ранее написанным методом get_all_words для получения названия файла и списка его слов.
Для удобного перебора одновременно ключа(названия) и значения(списка слов) можно воспользоваться методом словаря - item().

for name, words in get_all_words().items():
  # Логика методов find или count
"""


class WordsFinder:
    __file_names = []

    def __init__(self, *files):
        self.__file_names = list(files)

    def get_file_names(self):
        return self.__file_names

    def get_all_words(self):
        all_words = {}
        for file in self.__file_names:
            with open(file, encoding="utf-8") as text:
                file_words = []
                for line in text:
                    clear_line = line.casefold()
                    clear_line = clear_line.replace(' - ', " ")
                    clear_line = clear_line.replace('...', " ")
                    chars = {',', '.', '=', '!', '?', ';', ':'}
                    clear_line = ''.join(filter(lambda x: x not in chars, clear_line))
                    clear_line = clear_line.strip()
                    clear_line = clear_line.split()
                    for word in clear_line:
                        file_words.append(word)
                all_words.update({file: file_words})
        return all_words

    def find(self, word):
        word_location = {}
        for filename, words in self.get_all_words().items():
            if word in words:
                print(f"слово {word} имеет {words.index(word)} индекс, находится {words.index(word) + 1} в списке")
                word_location.update({filename: words.index(word) + 1})
                return word_location
        if len(word_location) == 0:
            return "Слово не найдено"

    def count(self, word):
        word_location = {}
        count_words = 0
        for filename, words in self.get_all_words().items():
            if word in words:
                count_words += 1
                word_location.update({filename: count_words})
        return word_location


c = WordsFinder("t1.txt", "t2.txt")
print(c.count("все"))
