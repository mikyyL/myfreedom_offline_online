# dict1 = {}
# dict2 = dict()
# print(dict1, dict2)
# new_dict = {'cat1': 'кот', 'dog1': 'собака'}
# x= {'cat2':'2', 'dog2': 'собака2'}
# # y = new_dict * 2
# # print(y)
# y = {**new_dict, **x}
# print(y)
# c = {1:'2', 1:'b'}
# print(c)
# v = x | y
# print(v)

new_dict = {'cat': 'кот', 'dog': 'собака'}
value_cate = new_dict.get('cat')  # получение значения по ключу
print(value_cate)
object_keys_and_values = new_dict.items()
print(object_keys_and_values)
x = list(object_keys_and_values)
print(x.pop(1))
print(x)
object_keys = new_dict.keys()
print(object_keys)
object_values = new_dict.values()
print(object_values)
new_dict.pop('cat')
print(new_dict)
new_dict1 = {'bird': 'птица'}
new_dict.update(new_dict1)
print(new_dict)
new_dict['zebra'] = 'Зебра'
print(new_dict)
new_dict.popitem()
print(new_dict)
print(new_dict.setdefault('dogg'))
print(new_dict)
print(new_dict.get('dog'))
x = [1, 2, 3]
y = [4, 5, 6]
c = dict(zip(x, y))
print(c)
# for i in c:
#     print(i)
    # print(f'значения {c[i]}')
# for key in c.keys():
#     print(key)
#
# for value in c.values():
#     print('Значения', value)

for key, value in c.items():
    print(f'Ключ словаря {key}\nЗначение словаря {value}')

print(4 in c)
