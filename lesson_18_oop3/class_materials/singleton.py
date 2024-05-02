class Data:
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __del__(self):
        Data.__instance = None

    def __init__(self, user, password):
        self.user = user
        self.password = password

    def connect(self):
        print(f'соединение с базой данных {self.user}, {self.password}')


data1 = Data('user1', '1234')
data2 = Data('user2', '1234567')
print(id(data1), id(data2))
data1.connect()
data2.connect()
