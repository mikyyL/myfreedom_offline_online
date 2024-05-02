class Pet:
    def __init__(self):
        self.__name = str
        self.__animal_type = str
        self.__age = int

    def set_name(self, name):
        self.__name = name

    def set_animal_type(self, animal_type):
        self.__animal_type = animal_type

    def set_age(self, age):
        self.__age = age

    def get_name(self):
        return self.__name


pet = Pet()
pet.set_name('Kitty')
print(pet.get_name())
