# set1 = {1, 2, 3, 4, 5}
# set2 = {6, 4, 7, 9, 8}
# set1.difference_update(set2)
# print(set1)
# set4 = {10, 7}
# print(type(None))
# # set3 = set1.union('set3')
# # print(set3)
# #
# # x = set1.update('set3')
# # print(set1)
import random

# 1

person = {
    'name': 'Artem',
    'age': 18,
    'city': 'Minsk'
}
print(person['age'])

# 2

cars = {
    'BMW': ['x3', 'x5', 'x6'],
    'TESLA': ['Modal 3', 'Modal x', 'Modal s']
}
for key in cars:
    print(f'{cars[key][0]}, {cars[key][-1]}')

# 4
numbers = {
    key: key ** 2 for key in range(1, 10)
}
x = 1
for value in numbers.values():
    x *= value
print(x)

# 5
list1 = [random.randint(1, 10) for i in range(10)]
list2 = [random.randint(1, 10) for i in range(10)]
new_dict = dict(zip(list1, list2))
print(new_dict)

# 6
string = 'pythonist'
dct = {key: string.count(key) for key in string}
print(dct)

# 7
# alfa = {
#     'cat': 'кот',
#     'dog': 'собака'
# }
# input_eng_word = input('Введите слово на английском языке: ')
# if input_eng_word in alfa:
#     print(f'{alfa[input_eng_word]}')

# x = {1, 2, 3, 4, [1]}
# print(x)
y = {[1, 2, 3]: 3}
print(y)
