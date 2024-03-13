name = "Petya"
age = 28
people_in_the_class = 10

string_template = "My names is: {}. I'm: {} years old. There are {} people in the class"
print("Simple format method without order:") #Простой метод форматирования без порядка
print(string_template.format("Artem", 20, 19))
print(string_template.format(name, age, people_in_the_class))
####################################################################

string_template = "My names is: {}. I'm: {} years old. There are {} people in the class"
print("\nSimple format method without order with more parameters:") # Простой метод форматирования без порядка с большим количеством параметров
print(string_template.format("Artem", 20, 19, 100, "abc", 777))
print(string_template.format(name, age, people_in_the_class))
####################################################################

print("\nSimple format method with sequence order:")    # Простой метод форматирования с порядком следования
string_template = "My names is: {0}. I'm: {1} years old. There are {2} people in the class"
print(string_template.format(name, age, people_in_the_class))
####################################################################

print("\nSimple format method with random order:") # Простой метод форматирования со случайным порядком
string_template = "My names is: {1}. I'm: {2} years old. There are {0} people in the class"
print(string_template.format(name, age, people_in_the_class))
####################################################################

print("\nSimple format method with duplicate index:") # Простой метод форматирования с повторяющимся индексом
string_template = "My names is: {1}. I'm: {2} years old. There are {2} people in the class"
print(string_template.format(name, age, people_in_the_class))
####################################################################

print("\nFormat with array as parameter:") # Формат с массивом в качестве параметра
string_template = "My names is: {info[0]}. I'm: {info[1]} years old. There are {info[2]} people in the class"
print(string_template.format(info=[name, age, people_in_the_class]))
####################################################################
my_string = f"My names is: {name}. I'm: {age} years old. There are {people_in_the_class} people in the class"
print(my_string)
# print('my name is: ', name, '')