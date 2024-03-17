# range()
# 1 - range(10) - от 0 до 10(не включая)
# 2 - range(2, 11) - от 2 до 11(не включая)
# 3 - range(10, 25, 5) - от 10 до 25(не включая с шагом 5)

# for i in range(10, 0, -1):
#     print(i)

# 1) Сгенерировать диапазон чисел от 25 до 99. Вывести результатом на экран значения
# кратные 7
x = []
for i in range(25, 99):
    if i % 7 == 0:
        x.append(i)
print(x)
# 2) Создать программу, которая просит ввести пользователя слово, а затем выводит каждую букву
# слова.

# 3) Пользователь вводит строку с клавиатуры. И также вводит символ, который входит в
# веденную нами строку. Программа должна вывести строку без того символа, который мы ввели.
# input_string = input('Введите строку: ')
# element_in_string = input('Введите символ строки: ')
# new_string = ''
# for i in input_string:
#     if i != element_in_string:
#         new_string += i
# print(new_string)

# for i in range(10):
#     if i == 6:
#         break
#     print(i)
#
# for i in range(10):
#     if i == 6:
#         continue
#     print(i)

list1 = [1, 2, 3, 4, 5]
sum_of_elements = 0
prod_of_elements = 1
for i in list1:
    sum_of_elements += i
    prod_of_elements *= i
print(f'сумма всех элементов {sum_of_elements}\nпроизведение всех элементов {prod_of_elements}')


