class Human:
    distance = int(input('Введите дистанцию для заплыва в метрах: '))
    # distance = 0

    def __init__(self, name : str, age: int):
        self.name = name
        self.age = age

    def walk(self, km):
        if km <= 5:

            return f'{self.name} может пройти {km} км'
        else:
            return f'Я не могу пройти {km} км'

    def swim(self):
        if self.distance <= 30:
            return f'Я могу проплыть {self.distance} метров'
        else:
            return f'Я не могу проплыть {self.distance} метров'
        

    # def swim_v_2(self, distance):
    #     if distance <= 30:
    #         return f'Я могу проплыть {distance} метров'
    #     else:
    #         return f'Я не могу проплыть {distance} метров'


my_human = Human('Artem', 18)
distance = 2
input_count_km = int(input('Введите количество км, которое должен пройти человек: '))
print(my_human.walk(input_count_km))
print(my_human.swim())
print(my_human.name)
print(my_human.age)
