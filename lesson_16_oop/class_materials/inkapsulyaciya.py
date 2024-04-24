# public
# protected
# private

class Wrapper:
    # public
    x = 2

    def public_method(self):
        return 'Это публичный метод'

    # protected
    _y = 1

    def _protected_method(self):
        return 'Это частично защищенный метод'

    # private
    __c = 6

    def __private_method(self):
        return 'Это приватный метод'

    def check_private_attr(self):
        return f'Значение приватного атрибута в том классе где был создан {self.__c}'

class ChildWrapper(Wrapper):

    def check_protected_atr(self):
        return self._y

    def check_private_atr(self):
        return self.__c


child_wrapper = ChildWrapper()
print(child_wrapper.check_protected_atr())
# print(child_wrapper.check_private_atr())
# print(child_wrapper._Wrapper__c)
print(child_wrapper.check_private_attr())


print(1 and 6)

print(bool(1), bool(-1))

