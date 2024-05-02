class Cat:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __repr__(self):
        return self.name + self.age

    def __str__(self):
        return self.name


cat = Cat('kitty', '2')
print(cat)
