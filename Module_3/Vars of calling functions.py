# Часто при разработке и работе с рассылками писем(e-mail) они отправляются от одного и того же
# пользователя(администрации или службы поддержки). Тем не менее должна быть возможность сменить его в редких случаях.
# Попробуем реализовать функцию с подробной логикой.

# Создайте функцию send_email, которая принимает
# 2 обычных аргумента: сообщение и получатель
# и 1 обязательно именованный аргумент со значением по умолчанию - отправитель.

# Внутри функции реализовать следующую логику:
#   Проверка на корректность e-mail отправителя и получателя.
#   Проверка на отправку самому себе.
#   Проверка на отправителя по умолчанию.


def check_email(email):
    is_valid = False
    if "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net")):
        is_valid = True
    return is_valid


def send_email(message, receiver, *, sender="university.help@gmail.com"):
    # receiver = "hardssd@mail.ru"
    result = ""

    success = f"Письмо успешно отправлено со стандартного адреса {sender} на адрес {receiver}, сообщение: {message}"
    other_sender_success = (f"Нестандартный отправитель! Письмо отправлено с адреса {sender} на адрес {receiver}, "
                            f"сообщение: {message}")
    failure_email = f"Один или оба E-mail {sender} и {receiver} введены неправильно или не поддерживаются"
    failure_email_self = ("Внимание! Вы отправляете письмо самому себе. "
                          "Здесь отправка писем самому себе не поддерживается")

    if check_email(receiver) and check_email(sender):
        if receiver == sender:
            result = failure_email_self
        elif sender == "university.help@gmail.com":
            result = success
        else:
            result = other_sender_success
    else:
        result = failure_email
    return print(result)


# print(send_email("Banan", "hardssd@mail.ru"))
send_email("Banan", "hardssd@mail.ru")
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
