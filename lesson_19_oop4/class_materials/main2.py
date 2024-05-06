# Экземпляру класса при инициализации передается аргумент – список тем для
# разговора.
# Класс реализует методы:
# – add_theme(value) – добавить тему в конец;
# – shift_one() – сдвинуть темы на одну вправо (последняя становится первой, остальные
# сдвигаются);
# – reverse_order() – поменять порядок тем на обратный;
# – get_themes() – возвращает список тем;
# – get_first() – возвращает первую тему.
# Пример 1
# Ввод:
# tl = Themes(['weather', 'rain'])
# tl.add_theme('warm')
# print(tl.get_themes())
# tl.shift_one()
# print(tl.get_first())
# Вывод:
# ('weather', 'rain', 'warm')
# warm
class Themes:
    def __init__(self, themes):
        self.themes = themes

    def add_theme(self, value):
        self.themes.append(value)

    def shift_one(self):
        if self.themes:
            last_theme = self.themes.pop()
            self.themes.insert(0, last_theme)

    def reverse_order(self):
        self.themes.reverse()

    def get_themes(self):
        return tuple(self.themes)

    def get_first(self):
        if self.themes:
            return self.themes[0]
        else:
            return None

# Пример использования класса:
tl = Themes(['weather', 'rain'])
tl.add_theme('warm')
print(tl.get_themes())
tl.shift_one()
print(tl.get_first())


