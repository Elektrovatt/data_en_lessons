# # 1. Использовать условный оператор - сравнить несколько чисел и вывести что-нибудь в print
# # 2. Использовать условный оператор - и если число в переменной
# # положительное - умножить его на 10, а если отрицательное - разделить.
# # a = 1
# # b = -6
# # if a > 0 and b > 0:
# #     print('a = {}, b = {}' .format(a * 10, b * 10))
# # elif a < 0 and b > 0:
# #     print('a = {}, b = {}' .format(a / 10, b * 10))
# # elif a < 0 and b < 0:
# #     print('a = {}, b = {}'.format(a / 10, b / 10))
# # else:
# #     print('a = {}, b = {}' .format(a * 10, b / 10))
# # # 3. Если число кратно 2м - то разделить его на 2 и вывести - иначе - умножить на 3.
# # # Как детектировать кратность числа в питоне - погуглите.
# # a = 5
# #
# # if a % 2 == 0:
# #     print(a*10)
# # else:
# #     print(a*3)
# # 4. Сделать какой-нибудь if внутри if.
# # a = 6.6
# #
# # if a % 2 == 0:
# #     if int(a):
# #         print('a is int')
# #     elif float(a):
# #         print('a is float')
# #     print(a * 10)
# # else:
# #     print(a*3)
# # 5. взять 2 переменных. Если в каждой переменной лежит тип int - вывести их сумму.
# # a = 6
# # b = 8
# # print(type(a), type(b))
# # if isinstance(a, int)  and isinstance(b, int) :
# #     print(a+b)
# # else:
# #     print('a and b is float')
#
#
# # 6. использовать оператор if с типом list - проверить наличие значения в списке.
#
list_num = [1, 2, 3]
pois = 5
if len(list_num) < 1:
    print('not number in list')
elif pois in list_num:
    print('number is list')
else:
    print('number is not list')