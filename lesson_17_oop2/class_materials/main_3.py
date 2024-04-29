from abc import ABC, abstractmethod


class Book(ABC):

    def __init__(self, name, auther):
        self.name = name
        self.auther = auther

    @abstractmethod
    def get_info_of_book(self):
        pass
    @abstractmethod
    def get_name_auther(self):
        pass


class Detective(Book):

    def get_info_of_book(self):
        return f'Это книга жанра детектив, название {self.name}, автор {self.auther}'


class Fantasy(Book):

    def get_info_of_book(self):
        return f'Книга в стиле фэнтази, ее назвние {self.name}, автор книги был {self.auther}'


detect = Detective('Шерлок Хоумс', 'Доил')
print(detect.get_info_of_book())
fant = Fantasy('Ведьмак', 'Сапковский')
print(fant.get_info_of_book())

