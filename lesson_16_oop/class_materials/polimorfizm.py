class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Котика зовут {self.name}, его возраст {self.age}'

    def make_sound(self):
        return 'Мяу'


class Dog:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_info(self):
        return f'Собачку зовут {self.name}, его возраст {self.age}'

    def make_sound(self):
        return 'Гаф'


cat = Cat('Kitty', 3)
dog = Dog('Baks', 4)
for animal in (cat, dog):
    print(animal.get_info())
    print(animal.make_sound())
