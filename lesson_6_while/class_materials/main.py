# lst = [2, 4]
# print(lst * (2/2))

# a = '13'
# b = '100'
# print(ord)
# print(a > b)
# print('a' > 'A')
# print(ord('a'), ord('A'))
# print(ord('3'), ord('0'))

# for i in range(3):
#     print(i)
#     i = 0 # 0 0 0; 0 1 2

#
# while True:
#     a = input('Введите строку: ')

# for i in range(10):
#     if i == 11:
#         break
# else:
#     print('Цикл не был принудительно остановлен')

# numbers = 23
# running = True
# while running:
#     input_number = int(input('Угадайте число: '))
#     if input_number == numbers:
#         print(f'Молодец, ты угадал, загаданное число было {numbers}')
#         running = False
#     elif input_number < numbers:
#         print(f'Твое число меньше загаданного')
#     else:
#         print('Твое число больше')
# else:
#     print('While завершил свою работу')

# 4
# num1 = int(input('Введите число: '))
# num2 = int(input('Введите число: '))
# if num1 < num2:
#     while num1 < num2:
#         num1 += 1
#         if num1 == 0:
#             break
#         print(num1)
# else:
#     while num2 < num1:
#         num2 += 1
#         if num2 == 0:
#             break
#         print(num2)


# Квадраты всех целых чисел от 1 до 10(включительно).
i = 1
while i <= 10:
    print(f'Квадратом числа {i} является число {i ** 2}')
    i += 1

# Перемножить все чётные значения в диапазоне от 0 до 125; результат вывести на экран.
i = 1
result = 1
while i <= 125:
    result *= i
    i += 1
print(result)

# Вывести числа от 1 до 15 в порядке убывания
i = 15
while i >= 1:
    print(i)
    i -= 1

# Необходимо, чтоб программа выводила на экран вот такую последовательность
# (не использовать готовый список):
# 7 14 21 28 35 42 49 56 63 70 77 84 91 98 Добавить в список и найти его длинну.
element = 7
numbers = []
while element <= 98:
    numbers.append(element)
    element += 7
print(f'Полученный список {numbers}\nДлина списка {len(numbers)}')



