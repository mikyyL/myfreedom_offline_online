# def print_text():
#     return 'hello world'
#
#
# x = print_text()
# print(x)
#
#
# def sum_of_numbers(num1, num2, num3):
#     result = num1 + num2 + num3
#     return result
#
#
# num1 = int(input('Введите первое число: '))
# num2 = int(input('Введите второе число: '))
# num3 = int(input('Введите третье число: '))
#
# print(sum_of_numbers(1, 2, 3))

# x = 50  # Глобальная переменная
#
#
# def func1(x):
#     print(f'Значие x->{x}')
#     x = 2  # Локальная переменная
#     print(f'Локальное значение x->{x}')
#     return x
#
#
# func1(x)
# print(f'Финальное значение x->{x}')

x = 50


#
# def func2():
#     global x
#     print(f'значение x->{x}')
#     x = 2
#     print(f'Замена на глобальное значение x->{x}')
#
#
# func2()
# print(f'Значение x в глобальной области видимости {x}')

# def values(*args, **kwargs):
#     print(args)
#     print(kwargs)
#
#
# values(1, 2, 3, 4, 5, a=5, b=6, c=7, d=8)

# def greet(*args):
#     """Эта функция выводит приветствие для всех
#     людей, перечисленных в кортеже names."""
#
#     # names — кортеж с именами
#     for name in args:
#         print("Привет, ", name)
#
#
# greet("Катя", "Андрей", "Борис", "Маша")


def greet_me(**kwargs):
    for key, value in kwargs.items():
        # print("{0} = {1}".format(key, value))
        print(f'{key} - {value}')


greet_me(name="yasoob")


def greet(name, msg='Доброе утро'):
    """
    Эта функция выводит
    для человека с именем name
    сообщение msg.

    Если текст сообщения не передан,
    по умолчанию используется "Доброе
    утро!"
    """

    print("Привет, ", name + '. ' + msg)


# 2 именованных аргумента
greet(name="Борис", msg="Как дела?")

# 2 именованных аргумента (идут не по порядку)
greet("Как дела?", "Борис")

# 1 позиционный, 1 именованный аргумент
greet("Борис", msg='Как дела?')



