# Экземпляр класса инициализируется с аргументом name – именем котенка. Класс
# реализует методы:
# – to_answer() – ответить: котенок через один раз отвечает да или нет, начинает с да. Метод
# возвращает “moore-moore”, если да, “meow-meow”, если нет. Одновременно
# увеличивается количество соответствующих ответов;
# – number_yes() – количество ответов да;
# – number_no() – количество ответов нет.
# Пример 1
# Ввод:
# tk = Talking('Pussy')
# print(tk.to_answer())
# print(tk.to_answer())
# print(tk.to_answer())
# print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
# Вывод:
# moore-moore
# meow-meow
# moore-moore
# Pussy says "yes" 2 times, "no" 1 times
class Talking:
    def __init__(self, name):
        self.name = name
        self.yes_count = 0
        self.no_count = 0
        self.answer = True

    def to_answer(self):
        if self.answer:
            self.yes_count += 1
            self.answer = False
            return "moore-moore"
        else:
            self.no_count += 1
            self.answer = True
            return "meow-meow"

    def number_yes(self):
        return self.yes_count

    def number_no(self):
        return self.no_count

# Пример использования класса:
tk = Talking('Pussy')
print(tk.to_answer())
print(tk.to_answer())
print(tk.to_answer())
print(f'{tk.name} says "yes" {tk.number_yes()} times, "no" {tk.number_no()} times')
