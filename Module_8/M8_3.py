"""
Задача "Некорректность":

Создайте 3 класса (2 из которых будут исключениями):

Класс Car должен обладать следующими свойствами:
Атрибут объекта model - название автомобиля (строка).
Атрибут объекта __vin - vin номер автомобиля (целое число). Уровень доступа private.
Атрибут __numbers - номера автомобиля (строка).

Метод __is_valid_vin(vin_number) - принимает vin_number и проверяет его на корректность.
Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.
Метод __is_valid_numbers(numbers) - принимает numbers и проверяет его на корректность.
Возвращает True, если корректный, в других случаях выбрасывает исключение. Уровень доступа private.

Классы исключений IncorrectVinNumber и IncorrectCarNumbers -
объекты, обладающие атрибутом message - сообщение, которое будет выводиться при выбрасывании исключения.

Работа методов __is_valid_vin и __is_valid_numbers:

__is_valid_vin
Выбрасывает исключение IncorrectVinNumber с сообщением
'Некорректный тип vin номер', если передано не целое число. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectVinNumber с сообщением 'Неверный диапазон для vin номера'
если переданное число находится не в диапазоне от 1000000 до 9999999 включительно.
Возвращает True, если исключения не были выброшены.

__is_valid_numbers
Выбрасывает исключение IncorrectCarNumbers с сообщением
'Некорректный тип данных для номеров', если передана не строка. (тип данных можно проверить функцией isinstance).
Выбрасывает исключение IncorrectCarNumbers с сообщением
'Неверная длина номера', переданная строка должна состоять ровно из 6 символов.
Возвращает True, если исключения не были выброшены.
"""


class IncorrectVinNumberError(Exception):
    # message1 = "Некорректный тип данных vin номера"
    # message2 = "Неверный диапазон для vin номера. Номер должен быть семизначным числом"
    def __init__(self, message):
        self.message = message


class IncorrectCarNumbersError(Exception):
    def __init__(self, message):
        self.message = message


class Car:
    # model = ""
    # __vin = 0
    # __number = "n039ya"

    def __init__(self, model, vin, number):
        self.model = model
        if self.__is_valid_vin(vin):
            self.__vin = vin
        if self.__is_valid_number(number):
            self.__number = number

    @property
    def vin(self):
        return self.__vin

    @vin.setter
    def vin(self, vin):
        if self.__is_valid_vin(vin):
            self.__vin = vin

    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number):
        if self.__is_valid_number(number):
            self.__number = number

    @staticmethod
    def __is_valid_vin(vin):
        if not isinstance(vin, int):
            raise IncorrectVinNumberError("Некорректный тип данных vin номера")
        elif len(str(vin)) != 7:
            raise IncorrectVinNumberError("Неверный диапазон для vin номера. Номер должен быть семизначным числом")
        return True

    @staticmethod
    def __is_valid_number(number):
        if not isinstance(number, str):
            raise IncorrectCarNumbersError("Некорректный тип данных номера машины")
        elif len(number) != 6:
            raise IncorrectCarNumbersError("Неверная длина номера")
        return True

# class InvalidInputError(Exception):
#     """Исключение для неверного ввода."""
#     pass
#
#
# def process_input(value):
#     if not isinstance(value, int):
#         raise InvalidInputError("Ожидается целое число!")
#     return print(value)
#
#
# try:
#     process_input("пп")
# except InvalidInputError as e:
#     print(e)
try:
  first = Car('Model1', 1000000, 'f123dj')
except IncorrectVinNumberError as exc:
  print(exc.message)
except IncorrectCarNumbersError as exc:
  print(exc.message)
else:
  print(f'{first.model} успешно создан')

try:
  second = Car('Model2', 300, 'т001тр')
except IncorrectVinNumberError as exc:
  print(exc.message)
except IncorrectCarNumbersError as exc:
  print(exc.message)
else:
  print(f'{second.model} успешно создан')

try:
  third = Car('Model3', 2020202, 'нет номера')
except IncorrectVinNumberError as exc:
  print(exc.message)
except IncorrectCarNumbersError as exc:
  print(exc.message)
else:
  print(f'{third.model} успешно создан')