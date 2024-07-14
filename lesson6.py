# 2. Создайте несколько классов - например: человек и т.д.

class Human:
    head: int
    hands: int
    age: int
    foots: int
    sex: int

    def __init__(self, v_name='Ivan'):
        self.name = v_name
        self.head = 1
        self.hands = 2
        self.age = 29
        self.foots = 2
        self.sex = 1


    def print_info(self):
        print(f'name = {str(self.name)}')
        print(f'hands = {str(self.hands)}')
        print(f'foots = {str(self.foots)}')
        print(f'head = {str(self.head)}')
        print(f'age = {str(self.age)}')
        print(f'sex = {str(self.sex)}')

#
# first_man = Human('Vasy')
# first_man.print_info()
# 3. От класса человек отнаследуйте класс "ребёнок"
#
# class Children(Human):
#
#     def __init__(self, v_name='maloy'):
#         super().__init__(v_name)
#         self.age = 10
#
# maloy = Children(v_name='maloy1')
# maloy.print_info()
# 4. Создайте класс "автобус".
# В автобусе должно содержаться несколько "детей" - например в list.
#
class Buss:
    color: str
    rolls: int
    dlina: int
    shirina: int
    hight: int
    mest: list


    def __init__(self, name_ob):
        self.name = name_ob
        self.color = 'white'
        self.rolls = 4
        self.dlina = 10
        self.shirina = 2.5
        self.hight = 2
        self.mest = []
        # self.cord_x = 1
        # self.cord_y = 1

    def zero_point(self):
        self.cord_x = 10
        self.cord_y = 10
    def print_info(self):
        print(f'name = {str(self.name)}')
        print(f'color = {str(self.color)}')
        print(f'rolls = {str(self.rolls)}')
        print(f'dlina = {str(self.dlina)}')
        print(f'shirina = {str(self.shirina)}')
        print(f'hight = {str(self.hight)}')
        print(f'mest = {str(self.mest)}')
        # print(f"cord_x = {str(self.cord_x)}")
        # print(f"cord_y = {str(self.cord_y)}")


    def add_baby(self, mest):
        self.mest.append(mest)



    def del_baby(self, mest):
        self.mest.remove(mest)




class baby_buss(Buss):  # Наследуем от класса Human
    def __init__(self, v_name='Glasha'):
        super().__init__(v_name)
        self.cord_x = 5
        self.cord_y = 5

    def print_info(self):
        super().print_info()
        print(f"cord_x = {str(self.cord_x)}")
        print(f"cord_y = {str(self.cord_y)}")




# new_bus = Buss('pety')
# new_bus.print_info()
new_baby_bus = Buss('baby_bus1')

new_baby_bus.add_baby('masha')
new_baby_bus.print_info()


# Для класса автобус напишите методы добавления ребёнка в автобус,
# удаления ребёнка из автобуса.
#
# 5. У каждого ребёнка сделайте хранение его текущего местоположения
# и методы для его изменения/отображения.
#
# У автобуса сделайте метод - при вызове которого будет
# меняться местоположение у всех детей, кто в нём находится на заданное
# (новое положение передавать в метод изменения положения)
#
# 5. Проявите смекалку - и создайте ещё несколько классов,
# которые будут содержать переменные других классов и делать что-нибудь забавное.