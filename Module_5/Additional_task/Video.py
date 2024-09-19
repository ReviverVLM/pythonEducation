class Video:
    """
    Каждый объект класса Video должен обладать следующими атрибутами и методами:

    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту, bool (False по умолчанию))
    """
    title = None
    duration = None
    time_now = 0
    adult_mode = False

    def __init__(self, title, duration, time_now=time_now, adult_mode=adult_mode):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode


if __name__ == '__main__':
    beta_user = Video("Miku", 3939, adult_mode=True)
    print(beta_user.adult_mode)
