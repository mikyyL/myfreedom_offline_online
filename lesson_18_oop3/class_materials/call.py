class Counter:

    def __init__(self):
        self.__counter = 0

    def __call__(self, *args, **kwargs):
        print('__call__')
        self.__counter += 1
        return self.__counter


counter = Counter()
counter2 = Counter()
counter()
counter()
counter2()
counter()
result = counter()
counter2()
print(result)
result = counter2()
print(result)
