# def call_with_five(function):
#     return function(5)
#
#
# def add_one(x):
#     return x + 1
#
#
# print(call_with_five(add_one))

# def multiply(num1):
#     def inner(num2):
#         return num1 * num2
#
#     return inner
#
# x = multiply(1)
# print(x(4))

def uppercase_decorator(function):
    def wrapper():
        print('Программа запустилась')
        print(function())
        # make_uppercase = func.upper()
        print('Программа закончила работу')

    return wrapper


@uppercase_decorator
def say_hi():
    return 'всем привет'


# print(uppercase_decorator(say_hi)())
say_hi()

double = lambda x: x * 2
print(double(5))


# 10


def factorial(n):
    if n <= 0:
        return 1
    return n * factorial(n - 1)


print(factorial(5))
