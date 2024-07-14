import pandas
import datetime

from Utils.utils1 import *

dt_time = datetime.datetime.now()
print(dt_time)
dttt = datetime.date(1990, 1, 25)
print(dttt.day)

class New_Human(Human):

    def __init__(self, name, date_b):
        self.name = name
        self.date_b = date_b

    def get_info_human(self):
        # year = self.date_b.day
        return self.name + ': ' + str(self.date_b)
        


one_person = New_Human('vasay', 1990)
one_person.get_name()
# two_person = Human('alex', 25)
# thee_person = Human('petya', 23)
one_rota = Rota([one_person])
# two_rota = Rota([two_person])
one_rota.print_all_in_rota()
print('------------------------------')
# two_rota.print_all_in_rota()
print('---------------------')
# one_polk = Polk([one_rota])
# one_polk.print_all_polk()
