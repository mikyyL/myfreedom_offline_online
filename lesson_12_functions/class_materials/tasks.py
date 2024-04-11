# 1) Написать функцию is_year_leap, принимающую 1 параметр —
# год, и возвращающую True, если год високосный, и False иначе.
import math


def is_year_leap(year):
    return year % 4 == 0 and year % 100 != 0 or year % 400 == 0


input_year = int(input('Введите год: '))
print(is_year_leap(input_year))


# Написать функцию square, принимающую 1 аргумент — сторону квадрата, и
# возвращающую 3 значения (с помощью кортежа): периметр квадрата, площадь
# квадрата и диагональ квадрата. Сторону квадрата вводить с клавиатуры.

# def square(side):
#     perim = 4 * side
#     area = side * side
#     diag = side * math.sqrt(2)
#     return perim, area, round(diag, 2)
#
#
# print(square(4))

# Написать функцию season, принимающую 1 аргумент — номер месяца (от 1 до 12),
# и возвращающую время года, которому этот месяц принадлежит (зима, весна, лето
# или осень). Номер месяца вводить с клавиатуры.

def season(number_of_mn):
    if number_of_mn in [12, 1, 2]:
        return 'Зима'
    elif number_of_mn in [3, 4, 5]:
        return 'Весна'
    elif number_of_mn in [6, 7, 8]:
        return "Лето"
    elif number_of_mn in [9, 10, 11]:
        return 'Осень'
    else:
        return 'Вы ввели число несуществующего месяца'


input_number_of_month = int(input('Введите число месяца: '))
print(season(input_number_of_month))