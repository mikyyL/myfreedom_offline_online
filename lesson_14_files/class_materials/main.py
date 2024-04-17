# 1 способ открытия файла
file = open('task1.txt', 'r')
# print(file)
# 1 способ чтения файла
# print(*file)
file.close()
# 2 способ открытия файла
# with open('task1.txt', 'r') as file:
#     # print(*file)
#     # print(file.read())
#     # print(file.readline(20))
#     # print(file.readline())
#     # print(file.readline())
#     print(file.readlines())
with open('task2.txt', 'w', encoding='utf-8') as file:
    # file.write('Привет мир')
    file.writelines(['привет1', 'привет2', 'привет3'])

# with open('task2.txt', 't') as file:
#     file.read()
    # print(line)
    # numbers = []
    # for i in line:
    #     if i.isdigit():
    #         numbers.append(int(i))
    # print(numbers)

with open(r'/Users/artemmikulich/Desktop/myfreedom_offline_online/lesson_10_try_except_podgotovka_exam_1/test_path.txt', 'r') as file:
    print(file.read())



