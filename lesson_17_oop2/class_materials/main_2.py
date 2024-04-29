# # class Human:
# #     @classmethod
# #     def class_method_human(cls):
# #         return 'Это метод класса'
# #
# #     @staticmethod
# #     def func_in_class():
# #         return 'Это функция внутри класса'
# #
# #
# # human = Human()
# # print(Human.class_method_human())
# # print(Human.func_in_class())
# # print(human)
#
#
# class Base:
#
#     def price(self):
#         return 10
#
#
# class InterFoo(Base):
#
#     def price(self):
#         return super().price() * 1.1
#
#
# class NewClass(InterFoo):
#
#     def price(self):
#         return super().price() * 0.8
#
#
# x = InterFoo()
# print(x.price())
# y = NewClass()
# print(y.price())

class Class1:

    def __init__(self, atr1, atr2):
        self.atr1 = atr1
        self.atr2 = atr2


class Class2(Class1):

    def __init__(self, atr1, atr2, atr3, atr4):
        super().__init__(atr1, atr2)
        self.atr3 = atr3
        self.atr4 = atr4


val1 = Class1(1, 2)
val2 = Class2(1, 2, 3, 4)
print(val1.atr1, val2.atr2)
print(val2.atr1, val2.atr2, val2.atr3, val2.atr4)
