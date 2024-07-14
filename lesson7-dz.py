# Создать классы: человек, рота, полк.
# В роте могут содержаться несколько человек, в полку - несколько рот.
# Написать методы:
# - добавления человека в роту, добавления роты в полк.
# - удаления человека из роты или из полка (в этом случае, человек удалиться из роты).
# Метод на вход должен получать list с несколькими переменными типа Human - как я с автобусом делал.
# - выводить информацию об одном человеке: имя, возраст.
# - выводить информацию об всех людях в роте.
# - выводить информацию об всех людях в полку.
# 4. Для всех методов из п.3 использовать обработку исключений.
# Можно не обрабатывать отдельные исключения - достаточно общего через просто Except.

class Human():
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_info_human(self):
        return self.name + ': ' + str(self.age)


class Rota():
    human: list

    def __init__(self, human: list):
        self.human = human

    def add_human_rota(self, human):
        self.human += human

    def remove_person(self, human):
        for one_person in human:
            if one_person in self.human:
                self.human.remove(one_person)

    def print_all_in_rota(self):
        for one in self.human:
            print(one.get_info_human())

    def get_name_rota(self):
        return self.human

class Polk():
    rota: list

    def __init__(self, rota: list):
        self.rota = rota

    def add_rota(self, rota):
        self.rota += rota

    def print_all_polk(self):
        for one in self.rota:
            print(one.print_all_in_rota())



one_person = Human('vasay', 19)
two_person = Human('alex', 25)
thee_person = Human('petya', 23)
one_rota = Rota([one_person, thee_person])
two_rota = Rota([two_person])


one_polk = Polk([one_rota, two_rota])
one_polk.print_all_polk()

