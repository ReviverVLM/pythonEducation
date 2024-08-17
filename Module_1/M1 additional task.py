# Вам необходимо решить задачу из реальной жизни: "школьные учителя устали подсчитывать вручную
# средний балл каждого ученика, поэтому вам предстоит автоматизировать этот процесс":
# На вход даны следующие данные:
# Список: grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]
# Множество: students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}
#
# Список grades содержит списки оценок для каждого ученика в алфавитном порядке.
# Например: 'Aaron' - [5, 3, 3, 5, 4]
# Множество students содержит неупорядоченную последовательность имён всех учеников в классе.
#
# Напишите программу, которая составляет словарь, используя grades и students,
# где ключом будет имя ученика, а значением - его средний балл.

grades = [[5, 3, 3, 5, 4], [2, 2, 2, 3], [4, 5, 5, 2], [4, 4, 3], [5, 5, 5, 4, 5]]  # Входные значения
students = {'Johnny', 'Bilbo', 'Steve', 'Khendrik', 'Aaron'}



list_of_students = [students.pop(),
                    students.pop(),
                    students.pop(),
                    students.pop(),
                    students.pop()]
list_of_students.sort()


students_book_of_grades = {list_of_students[0]: sum(grades[0]) / len(grades[0]),
                           list_of_students[1]: sum(grades[1]) / len(grades[1]),
                           list_of_students[2]: sum(grades[2]) / len(grades[2]),
                           list_of_students[3]: sum(grades[3]) / len(grades[3]),
                           list_of_students[4]: sum(grades[4]) / len(grades[4])}

print(students_book_of_grades)
