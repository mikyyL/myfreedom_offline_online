# __new__
# __new__ ---> объект класса ---> __init__

class Point:

    def __new__(cls, *args, **kwargs):
        print(f'Вызов __new__ для {cls}')
        return super().__new__(cls)

    def __init__(self, x, y):
        print(f'Вызов __init__ для {self}')
        self.x = x
        self.y = y


point = Point(1, 2)
print(point)