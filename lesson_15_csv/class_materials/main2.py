import csv
import pandas
# Запись в файл простых строк
# name_1 = 'Petya'
# name_2 = 'Miwa'
# with open('task.csv', 'w') as file:
#     writer = csv.writer(file, delimiter=';')
#     writer.writerow([name_1, name_2])

# Объединение данных изначально в список
# list1 = ["Petya", 'Miwa']
# with open('task.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(list1)


# записываем заголовки для таблиц
# with open('task2.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow(
#         ('login', 'password')
#     )
# # создаем список с логинами и паролями
# data = [
#     ['login1', 'password1'],
#     ['login2', 'password2'],
#     ['login3', 'password3']
# ]
# # for element in data:
# #     with open('task2.csv', 'a') as file:
# #         writer = csv.writer(file)
# #         writer.writerow(element)
# with open('task2.csv', 'a') as file:
#     writer = csv.writer(file)
#     writer.writerows(data)

data = [
    ('login', 'password'),
    ['login1', 'password1'],
    ['login2', 'password2'],
    ['login3', 'password3']
]
with open('task3.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerows(data)
#
# with open('task3.csv', 'r') as file:
#     reader = csv.reader(file)
#     for row in reader:
#         print(row)

# data = 'Петя'
# with open('task4.csv', 'w') as file:
#     writer = csv.writer(file)
#     writer.writerow([data])
#
# with open('task4.csv', 'r') as file:
#     reader = csv.reader(file)
#     print(list(reader))

# with open('task3.csv', 'r') as file:
#     reader = csv.DictReader(file)
#     for row in reader:
#         print(row)

result = pandas.read_csv('task3.csv')
print(result)