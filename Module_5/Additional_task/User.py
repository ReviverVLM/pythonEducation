class User:
    """
    Каждый объект класса User должен обладать следующими атрибутами и методами:

    Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)
    """
    nickname = None
    password = None
    age = None

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age


if __name__ == '__main__':
    beta_user = User("Miku", "3939", 16)
    print(beta_user.age)

