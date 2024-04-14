# 1
print(4 ** 4 ** 4)  # True,
# 4^4^4 -> 4^256    (4^4)^4 -> 256^4
# 4

# В строке “Иван Иванов” поменяйте местами слова.
# Может быть предоставлена любая строка с именем и фамилией.
# например “Петр Иванов” => “Иванов Петр”
name = 'Иван Иванов'
list_name = name.split(' ')
print(list_name)
print(f'{list_name[-1]} {list_name[0]}')
# reverse_list_names = list(reversed(list_name))
# print(reverse_list_names)
# result = " ".join(reverse_list_names)
# print(result)

# 5 Создать список с числами от 1 до 50 используя генератор списков.
list_x = [i for i in range(1, 51)]
print(list_x)

# 6 Вам передан массив чисел. Известно, что каждое число
# в этом массиве имеет пару, кроме одного: [1, 5, 2, 9, 2, 9, 1] => 5
numbers = [1, 5, 2, 9, 2, 9, 1]
for i in numbers:
    if numbers.count(i) == 1:
        print(i)

# 7 Дан список [student1, student2, student3] с помощью цикла for добавить к
#     каждому элементу списка слово “_good”. Вывести на экран.

students = ['student1', 'student2', 'student3']
x = []
for i in students:
    i += '_good'
    x.append(i)
    print(i)
print(x)

# 8 Вывести на экран числа от 0 до 50, кроме 35.
for i in range(0, 50):
    if i == 35:
        continue
    print(i)
list1 = [i for i in range(0, 50) if i != 35]
print(list1)

# 9 Дана строка [“hello my friend”, “my name is”, “house”, “cat”, “dog”].
# В новый список добавить элементы, которые содержат пробел.
list2 = ['hello my friend', 'my name is', 'house', 'cat', 'dog']
new_list = [i for i in list2 if " " in i]
print(new_list)
# for element in list2:
#     if ' ' in element:
#         new_list.append(element)
# print(new_list)

# 10 В классе N школьников. На уроке физкультуры тренер говорит «на первый-второй
# рассчитайтесь». Выведите, что скажут ученики.
# Входные данные: Вводится одно целое число — количество человек в классе.
# Входные данные: Выведите последовательность чисел 1 и 2, в том порядке,
# как будут говорить школьники.
# n = int(input('Введите количетсво школьников: '))
# for i in range(1, n + 1):
#     if i % 2 != 0:
#         print(f'школьник под номером {i} сказал 1')
#     else:
#         print(f'школьник под номером {i} сказал 2')

# Дан список чисел, необходимо удалить все вхождения числа 20 из него.
list5 = [1, 2, 3, 20, 20, 30, 50, 20]
# for i in list5:
#     if i == 20:
#         list5.remove(i)
while 20 in list5:
    list5.remove(20)
print(list5)

# С клавиатуры вводится десятизначное число. Вывести на экран четные числа входящие в
# данное число. Например 1234567892  2 4 6 7 8 2
# number = int(input('Введите десятизначное число: '))
# if len(str(number)) != 10:
#     print('Вам необходимо ввести десятизначное число')
# else:
#     for i in str(number):
#         if int(i) % 2 == 0:
#             print(i, end=' ')

# Необходимо удалить пустые строки из списка строк. Пример списка:
# [‘1’, ‘2’,  ‘3’ , ‘4’ ,’hello’, ‘’, ‘good’ , ‘’, ‘’, ‘5’, ‘6’, ‘7’]

list6 = ['1', '2', '3', '4', 'hello', '', 'good', '', '', '5', '6', '7']
while '' in list6:
    list6.remove('')
print(list6)


# Напишите программу, которая принимает текст и выводит два слова:
# наиболее часто встречающееся и самое длинное.

string = input('Введите строку: ')
list_string = string.split(' ')
print(list_string)
max_len_element = max(list_string, key=len)
max_count_element = max(list_string, key=list_string.count)
print(max_len_element)
print(max_count_element)


#
# Дезоксирибонуклеиновая кислота (ДНК) представляет собой
# химическое вещество, находящееся в ядре клеток и несущее
# «инструкции» по развитию и функционированию живых организмов.
# В цепочках ДНК символы «А» и «Т» дополняют друг друга, как «С» и
# «G».Вам нужно вернуть другую дополнительную сторону. Нить
# ДНК никогда не бывает пустой или ДНК вообще не существует.
# Пример: (ввод --> вывод)
#
# “AТТGС" --> "ТААСG"
# “GТАТ" --> "САТА"
dna = input('Введите ДНК: ').upper()
new_dna = ''
for i in dna:
    if i == 'A':
        new_dna += 'T'
    elif i == 'T':
        new_dna += 'A'
    elif i == 'C':
        new_dna += 'G'
    elif i == 'G':
        new_dna += 'C'
print(new_dna)

