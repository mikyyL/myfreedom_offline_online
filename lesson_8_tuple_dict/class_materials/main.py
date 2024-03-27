tuple1 = tuple()
print(type(tuple1))
tuple2 = ()
print(type(tuple2))

new_tuple = (1,)
print(new_tuple)

tuple3 = (1, 2, 3, 4, 5, 6, 7)
print(tuple3)

# базовые операции
x_1 = new_tuple + tuple3
print(x_1)
x_2 = x_1 * 3
print(x_2)

element_pos = x_2.index(4)
print(element_pos)
count_element = x_2.count(1)
print(count_element)

# abc = (1, 2, 3, [1, 2, 3], 6, 7, 8)
# list1 = abc[3]
# list1.append(4)
#
#
# print(abc)
x = (1, -22, 33, 44, 5)
# x_list = list(x)
# x_list.sort()
# print(f'Минимальное значение списка {x_list[0]}\nМаксимальное значение {x_list[-1]}')
max_element = x[0]
min_element = x[0]
for i in x:
    if max_element < i:
        max_element = i
    elif min_element > i:
        min_element = i
print(f'Минимальное значение списка {min_element}\nМаксимальное значение {max_element}')

print(f'Минимальное значение списка {min(x)}\nМаксимальное значение {max(x)}')
