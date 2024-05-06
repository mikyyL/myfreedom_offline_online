# Класс Bus содержит свойства:
# – speed (скорость),
# –capacity (максимальное количество пассажиров),
# – maxSpeed (максимальная скорость),
# – passengers (список имен пассажиров),
# – hasEmptySeats (наличие свободных мест),
# – seats (словарь мест в автобусе);
# методы:
# – посадка и высадка одного или нескольких пассажиров,
# – увеличение и уменьшение скорости на заданное значение.
# – операции "in", "+=" и "−=" (посадка и высадка пассажира(ов) с заданной фамилией)
class Bus:
    def __init__(self, speed, capacity, max_speed):
        self.speed = speed
        self.capacity = capacity
        self.max_speed = max_speed
        self.passengers = []
        self.seats = {i: None for i in range(1, capacity + 1)}

    def embark(self, *names):
        for name in names:
            if len(self.passengers) < self.capacity:
                self.passengers.append(name)
                empty_seat = next(seat for seat, occupant in self.seats.items() if occupant is None)
                self.seats[empty_seat] = name
                print(f"{name} сел в автобус на место {empty_seat}")
            else:
                print("Автобус полон!")

    def disembark(self, *names):
        for name in names:
            if name in self.passengers:
                self.passengers.remove(name)
                seat = next(seat for seat, occupant in self.seats.items() if occupant == name)
                self.seats[seat] = None
                print(f"{name} вышел из автобуса с места {seat}")
            else:
                print(f"{name} не находится в автобусе!")

    def increase_speed(self, value):
        if self.speed + value <= self.max_speed:
            self.speed += value
            print(f"Скорость увеличена на {value} км/ч и составляет теперь {self.speed} км/ч")
        else:
            print("Превышена максимальная скорость!")

    def decrease_speed(self, value):
        if self.speed - value >= 0:
            self.speed -= value
            print(f"Скорость уменьшена на {value} км/ч и составляет теперь {self.speed} км/ч")
        else:
            print("Скорость не может быть отрицательной!")

    def __contains__(self, name):
        return name in self.passengers

    def __iadd__(self, name):
        self.embark(name)
        return self

    def __isub__(self, name):
        self.disembark(name)
        return self


bus = Bus(speed=0, capacity=50, max_speed=60)
bus += "Иван"
bus += "Мария"
bus += "Петр"
print("Пассажиры в автобусе:", bus.passengers)
print("Свободные места в автобусе:", [seat for seat, occupant in bus.seats.items() if occupant is None])
bus -= "Иван"
print("Пассажиры в автобусе:", bus.passengers)
print("Свободные места в автобусе:", [seat for seat, occupant in bus.seats.items() if occupant is None])
bus.increase_speed(40)
bus.decrease_speed(20)
