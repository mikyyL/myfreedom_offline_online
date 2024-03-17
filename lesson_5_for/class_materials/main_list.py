# способы создания списка
list1 = []
list2 = list()

animals_names = ['cat', 'dog', 'panda']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

# x = 1
# y = list(x)
# print(y)
name = 'Artem'
list3 = list(name)
print(list3)

# Индексы
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[0])
print(numbers[-1])

# методы
new_list = [1, 2, 3, 4]
new_list.append(5)  # добавление в конец списка
print(new_list)
new_list.insert(0, 10)  # добавление на указанную позицию элемент
print(new_list)
new_list.remove(10)  # удаление по имени элемента
print(new_list)
del_value = new_list.pop(-1)  # удаление по индексу + возвращает удаленный элемент
print(new_list, f'Удаленное значение из списка {del_value}')
print(new_list.count(6))

# Изменить элемент в списке
x = [1, 2, 3, 4]
x[0] = 'hello'
print(x)

# Разница между изменяемы и неизменяемые???
x_list1 = [1, 2, 3, 4]
y_list1 = x_list1
x_list1.append(5)
print(f"Список x_list1 = {x_list1}")  # 1, 2, 3, 4, 5
print(f'Список y_list1 = {y_list1}')  # 1, 2, 3, 4

x = 2
y = x
y += 2
print(y)
print(x)
