# try:
#     x = 1
#     y = 0
#     result = x / y
# except (ZeroDivisionError, AttributeError):
#     print('Словили исключение деления на 0')
# else:
#     print(result)
# finally:
#     print('Конец программы')

x = 2
if x == 2:
    raise Exception('Принудительный вызов исключения')
