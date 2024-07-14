import datetime

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
        try:
            for one in self.rota:
                print(one.print_all_in_rota())

        except Exception as e:
            print(e)