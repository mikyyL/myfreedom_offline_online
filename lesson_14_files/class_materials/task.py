with open('task.txt', 'r') as file:
    result = file.read()
print(result)
sum_elements = 0
new_result = result.replace('_', ' ')
list1 = new_result.split(' ')
print(list1)
for i in list1:
    if i.isdigit():
        sum_elements += int(i)
print(sum_elements)