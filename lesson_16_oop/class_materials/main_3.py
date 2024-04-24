class Fruit:

    def __init__(self, name, color):
        self.name = name
        self.color = color

    def cut(self):
        return f'{self.name} был порезан'


class Apple(Fruit):

    def clear(self):
        return f'{self.name} был очищен'


apple = Apple('Яблоко', 'Красный')
print(apple.name)
print(apple.color)
print(apple.cut())
print(apple.clear())
