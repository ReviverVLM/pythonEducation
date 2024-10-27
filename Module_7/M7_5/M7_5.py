"""
Освоить работу с файловой системой в Python, используя модуль os.
Научиться применять методы
os.walk, os.path.join, os.path.getmtime, os.path.dirname, os.path.getsize
и использование модуля time для корректного отображения времени.

Задание:

Создайте новый проект или продолжите работу в текущем проекте.
Используйте os.walk для обхода каталога, путь к которому указывает переменная directory.
Примените os.path.join для формирования полного пути к файлам.
Используйте os.path.getmtime и модуль time для получения и отображения времени последнего изменения файла.
Используйте os.path.getsize для получения размера файла.
Используйте os.path.dirname для получения родительской директории файла.
"""
import os
import time

directory = "."

for root, dirs, files in os.walk(directory):
    print(root)
    print(dirs)
    print(files)
    count = 0
    if count == 0:
        print(os.path.join(*dirs, "hihi.webp"))
        count += 1

hihi = os.path.abspath("hihi.webp")
print(hihi)
secs_time = os.path.getmtime("hi.webp")
print(secs_time)
print(time.ctime(secs_time))
print(os.path.getsize("hi.webp"))
print(os.path.dirname(hihi))
for root in os.walk(directory):
    print(root)

