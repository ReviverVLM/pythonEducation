from User import User
from Video import Video


class UrTube:
    """
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:

     Атрибуты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

    - Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users
    с такими же логином и паролем. Если такой пользователь существует,
    то current_user меняется на найденного. Помните, что password передаётся в виде строки, а сравнивается по хэшу.

    - Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список,
    если пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname}
    уже существует". После регистрации, вход выполняется автоматически.

    - Метод log_out для сброса текущего пользователя на None.

    - Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
    названием видео ещё не существует. В противном случае ничего не происходит.

    - Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
    слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

    - Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
    то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
    После текущее время просмотра данного видео сбрасывается.
    """
    """
    Было принято волевое решение заменить список на словарь вида:
        ключ логин, значение объект, минус - без периодического вайпа могут закончиться места
    для регистрации. В системах такого вида ключом обычно является логин. Была мысль в значение залить массив с
    остальными атрибутами(в рамках данного задания это можно сделать), но в будущем будет проблематично получить доступ
    к объекту класса из-за того, что он фактически не будет использоваться
    
    """
    users = {}  # Ключ ник, значение объект
    videos = []
    current_user = None

    # class Singleton
    # Предотвращаем дубликаты класса
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not isinstance(cls._instance, cls):
            cls._instance = object.__new__(cls)
        return cls._instance

    def register(self, nickname, password, age):
        # Заготовка(надо довести до рабочего состояния), если потребуется массив users, а не словарь
        # for user in self.users:
        #     if user.nickname in self.users:
        #         print("Такой пользователь уже существует или если это вы выберите форму входа")
        #         break
        #     else:
        #         continue
        if nickname not in self.users:
            user = nickname  # Сохраняем значение ника во временную переменную
            nickname = User(user, password, age)  # Создаём класс, уникальность даёт ник, который проверяется выше
            self.users[user] = nickname  # Добавляем в словарь пару ключ ник, значение объект
            return self.log_in(user, password)
        else:
            print(f"Пользователь {nickname} уже существует, если это вы используйте другой метод")
            return None

    def log_in(self, user, password):
        if self.current_user != user:
            if user in self.users:
                if self.users[user].password == hash(password):
                    self.current_user = user
                    print("Добро пожаловать на самый лучший видеохостинг")
                else:
                    print("Неверный пароль. Попробуйте ещё раз")
            else:
                print("Такого пользователя не существует")
                if input("Если вы хотели зарегистрироваться введите '+': ") == '+':
                    self.register(user, password, input("Введите свой возраст: "))
                    self.log_in(user, password)
                else:
                    print("Галя, у нас отмена, усиливай защиту от ботов!!!")
        else:
            print("Не напрягайте и так слабую систему, вы уже залогинены. Идите лучше почините Ютаб или сделайте"
                  " адекватный аналог. Спасибо за понимание.")

    def log_out(self):
        if self.current_user is not None:
            self.current_user = None

    def add_videos(self, *videos):
        """Добавление видео. Проверки на авторизацию пользователя и премодерацию видео нетЪ"""
        for video in videos:
            if isinstance(video, Video):
                self.videos.append(video)

    def get_videos(self, search):
        searching_videos = []
        for movie in self.videos:
            if search.lower() in movie.title.lower():
                """Проверка на возраст вместо """
                if self.current_user is None or self.users[self.current_user].age <= 18:
                    if movie.adult_mode:
                        continue
                    else:
                        searching_videos.append(movie.title)
                else:
                    searching_videos.append(movie.title)

        return searching_videos

    def watch_video(self, video, current_video_time=0):
        if self.current_user is None:
            return print('Для просмотра требуется авторизация на сайте')

        import time
        for movie in self.videos:
            if video == movie.title:
                if movie.adult_mode and self.users[self.current_user].age <= 18:
                    return print('Ваш возраст не соответствует нормам санэпидемстанции, '
                                 'пожалуйста пройдите в комнату без интернета на сутки')
                movie.time_now = current_video_time
                while movie.time_now != movie.duration:
                    movie.time_now += 1
                    time.sleep(1)
                    print(movie.time_now)
                movie.time_now = 0
                return print("Поставьте лайк и подпишитесь на канал...а не то вам хуже будет(наверное)")


if __name__ == '__main__':
    ytube = UrTube()
    # ytube.register('vasya_pupkin', 'lolkekcheburek', 13)
    ytube.register('Miku', 'lolkekcheburek', 16)
    # ytube.register('vasya_pupkin', 'lolkekcheburek', 113)
    # ytube.register('Kaito', 'lolkekcheburek', 133)
    # ytube.register('Kaito', 'lolkekcheburek', 13)
    # ytube.log_in('vasya_pupkin', 'lolkekcheburek')
    # ytube.log_in('Miku', '3939')
    # ytube.log_in('vasya_pupkin', 'lolkek')
    # ytube.log_in('Kaito', 'lolkekcheburek')
    # ytube.log_in('Kaito', 'lolkekcheburek')
    v1 = Video('Лучший язык программирования 2024 года', 200)
    v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
    v3 = Video("RRes", 234, 60)
    obmanka = User('vasya_pupkin', 'lolkekcheburek', 13)
    ytube.add_videos(v1, v2, v3, obmanka)
    for vid in ytube.videos:
        print(vid)
    print(*ytube.get_videos("грам"))
    ytube.watch_video("Для чего девушкам парень программист?")
