lst = [1, 2, 3]
lst2 = lst
print(lst is lst2)  # True,
print(lst == lst[:])  # True
print(id(lst), id(lst2))

#
# x = sum()
# print(x) # Hello world
#
# str = 'py'
# del str
# print(1.)
# count = 0
#
#
# def f():
#     count = 0
#     count += 1
#     return count
#
# f()
# print(count)

lst = [i if i > 0 else i ** 2 for i in range(-2, 2)]
print(f'{lst = }') # [4, 1, 0, 1]

import timeit
code_to_test = """
a = 'hello'
b = 'world'
c = f'{a}{b}'
"""

# print(dis.dis('{}{}'.format(a, b)))
print(timeit.timeit(code_to_test))




