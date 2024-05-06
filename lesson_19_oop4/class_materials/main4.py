# Класс Publication описывает публикацию от пользователя в сети:
# – никнейм пользователя,
# – время публикации,
# – количество лайков,
# – текст сообщения,
# – список комментариев.
# Конструктор класса получает автора, устанавливает время, зануляет количество
# ругательств, а для комментариев создает списочный массив.
# Добавить метод, позволяющий поставить лайк сообщению

import datetime


class Publication:
    def __init__(self, nickname, text):
        self.nickname = nickname
        self.time = datetime.datetime.now()
        self.likes = 0
        self.text = text
        self.comments = []

    def add_like(self):
        self.likes += 1

    def get_time(self):
        self.time = datetime.datetime.now()
        return self.time


# Пример использования класса:
publication = Publication("JohnDoe", "Hello, world!")
print(f"Original Likes: {publication.likes}")
publication.add_like()
print(f"Updated Likes: {publication.likes}")
# print(publication.time)
