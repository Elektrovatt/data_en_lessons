class Human:
    _name: str
    __location: str

    def __init__(self, name='Ivan'):
        self._name = name
        self._location = 'Moscow'

    def get_name(self):
        return self._name

    def get_location(self):
        return self._name + ': ' + self._location

    def set_location(self, location):
        self._location = location

class Childern(Human):
    _age = 5
    def __init__(self, name='Ivan'):
        super().__init__(name)

    def set_age(self, age):
        self._age = age

    def get_age(self):
        return self._name + ': ' + str(self._age)


class Bus:
    childrens : list

    def __init__(self, childrens: list):
       self.childrens = childrens

    def add_childrens(self, childrens):
        self.childrens += childrens

    def remove_childrens(self, childrens):
        for one_child in childrens:
            if one_child in self.childrens:
                self.childrens.remove(one_child)

    def print_all_childrens_location(self):
        for one_child in self.childrens:
            print(one_child.get_location())

    def go_to_new_location(self, new_location):
        for one_child_location in self.childrens:
            one_child_location.set_location(new_location)

one_child = Childern('Vasya')
two_child = Childern('Gena')
three_child = Childern('Alex')

one_bus = Bus([one_child, two_child])
one_bus.print_all_childrens_location()
one_bus.go_to_new_location('Piter')
one_bus.print_all_childrens_location()
one_child.set_location('Smolensk')
one_bus.print_all_childrens_location()


