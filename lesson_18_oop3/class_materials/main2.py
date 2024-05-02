class Point:
    color = 'red'
    circle = 2

    def __init__(self, x, y):
        print('Вызов __init__')
        self.x = x
        self.y = y

    def __del__(self):
        print(f'удаление экземпляра {self}')

    def set_coords(self, x, y):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


point = Point(10, 15)
print(point.__dict__)
print(point.set_coords())