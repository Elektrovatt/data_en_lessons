import pandas
import datetime

from Utils.utils1 import *

dt_time = datetime.datetime.now()
print(dt_time)

one_person = Human('vasay', 19)
two_person = Human('alex', 25)
thee_person = Human('petya', 23)
one_rota = Rota([one_person, thee_person])
two_rota = Rota([two_person])
# one_rota.print_all_in_rota()
print('------------------------------')
# two_rota.print_all_in_rota()
print('---------------------')
one_polk = Polk([one_rota, two_rota])
one_polk.print_all_polk()
