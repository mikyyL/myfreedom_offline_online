import random

list1 = [1, 2, 3, 4]
list2 = [5, 6, 7, 8]
list1.append(list2)
print(list1)
list1.extend(list2)
print(list1)
list1.insert(0, 10)
print(list1)
list1.pop(5)
print(list1)
list1.remove(10)
print(list1)
list2.clear()
print(list2)
list3 = list1.copy()
print(list3)
print(id(list1), id(list3))
count_of_number_one = list1.count(1)
print(count_of_number_one)
index_of_element_five = list1.index(5)
print(index_of_element_five)

x = [1, 2, 10, 4, 5, 6]
x.sort(reverse=True)
# x.sort(key=len)
# print(x)
# x.reverse()
print(x)

list_of_elements = [1, 2, 3, 4, 5, 'b', 'a', 'c']
# appends, extend, remove, pop, insert
# Отсортировать значения у списка так, чтобы числа были в порядке убывания,
# а строки по возрастанию, получив новый список
# применить reverse
# заменить первый элемент списка на строку 'hello world python'


numbers = [i for i in range(11) if i % 2 == 0]
print(numbers)

# number = []
# for i in range(7):
#     x = random.randint(10, 99)
#     number.append(x)
# print(number)
#
#
# number = [random.randint(10,99) for i in range(10)]
# print(number)

# 1 Дан произвольный список. Представить его в обратном порядке
x = [random.randint(10, 99) for i in range(10)]
print(x)
x.reverse()
print(x)

# 2 Дан список с числами и в нем есть цифра 20. Поменять 20 на 200.
list4 = [1, 2, 3, 20, 50, 20]
for i in list4:
    index = list4.index(i)
    if i == 20:
        list4[index] = 200
print(list4)

for i in range(len(list4)):
    if list4[i] == 20:
        list4[i] = 200
print(list4)

list5 = [i for i in range(10)]
print(list5[1::2])

# Сгенерируйте список, который должен составлять 10 элементов.
# Найдите сумму всех его четных элементов. (
# встроенную функцию для нахождения суммы использовать нельзя)
list6 = [random.randint(1, 10) for i in range(10)]
sum_of_elements = 0
for i in list6:
    if i % 2 == 0:
        sum_of_elements += i
print(sum_of_elements)

# Список из 7 цифр. Если чётных цифр в нём больше, то найти сумму всех цифр,
# если нечётных больше, то найти произведение 1, 3 и 6 элемента.
numbers = [random.randint(1, 15) for i in range(7)]
x_1 = 0
x_2 = 0
summ = 0
prod = 1
for i in numbers:
    if i % 2 == 0:
        x_1 += 1
    else:
        x_2 += 1
print(f'Количество четный значений {x_1}\nКоличество нечетных значений {x_2}')
if x_1 > x_2:
    for i in numbers:
        summ += i
    print(f'сумма {summ}')
else:
    prod = numbers[0] * numbers[2] * numbers[5]
    print(f'произведение {prod}')

# Найти совпадающие элементы двух списков. a = [5,[1,2],2,'r',4,'ee'] b = [4,'we','ee',3,[1,2]]
# Эти значения записать в новый список

a = [5, [1, 2], 2, 'r', 4, 'ee']
b = [4, 'we', 'ee', 3, [1, 2]]
c = []
for i in a:
    if i in b:
        c.append(i)
print(c)

# Напишите программу для удаления элементов с четными индексами из списка.
x = [i for i in range(10)]
print(x)
for i in x:
    index = x.index(i)
    if index % 2 == 0:
        x.pop(index)
print(x)

x = [random.randint(1, 10) for i in range(10) if i % 2 != 0]
print(x)

# Напишите программу для нахождения второго наименьшего элемента в списке.
x = [random.randint(1, 100) for i in range(10)]
print(x)
x.sort()
print(x[1])



