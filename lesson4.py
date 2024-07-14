# 1. Написать цикл по листу.
# list_num = [1, 2, 3, 4, 5]
# for one_element in list_num:
#     print(one_element)
# 2. Написать цикл по листу со строками.
# Выводить значения, если длина строки элемента > 5 символов.
# list_element = [1, 2, 'list', 3, 4, 'elements']
# for one_element in list_element:
#     if isinstance(one_element, str) and len(one_element) > 5:
#         print(one_element)
# list_element1 = ['list','eleme12121nts']
# for one_element in list_element1:
#     if len(one_element) > 5:
#         print(one_element)
# 3. Написать цикл по листу с листами.
# Внутри цикла по внешнему листу - сделать цикл по внутренним листикам. Просто выводить элементы.

# list_root = [["list1", "list1.1"], ["list2", "list2.2"]]
# print(list_root)
# for i in list_root:
#     for a in i:
#         print(a)

# 4. Написать цикл по словарю (по ключам словаря).
# Выводить ключи и выводить значения.
# d1 = {
#     1: '1slovo',
#     2: '2slovo',
#     3: '3slovo'
# }
# for i in d1.keys():
#     print(i, d1.get(i))

# 5. Вывести цифры от 1 до 10000 используя цикл while и break.
# a = 1000
# i = 0
# while i < a:
#     print(i)
#     i+= 1
#     if i == 90:
#         break
# 6. Создайте 2 словаря с различными ключами.
# Сделайте 3й словарь - чтобы там были значения и из 1го словаря и из второго -
# используя цикл по второму словарю.

# d1 = {
#     1: '1slovo',
#     2: '2slovo',
#     3: '3slovo'}
# d2 = {
#     21: '21slovo',
#     22: '22slovo',
#     23: '23slovo'}
# # d3 = {}
# #
# # d3 = {**d1, **d2}
# # for i in d3:
# #     print(i, d3.get(i))
# # print(d3)
# for i in d2.keys():
#     d1[i]=d2.get(i)
# print(d1)

list_key = [1, 2, 3, 3,  4, 4]

def func_del(one_par):
    list_key.remove(one_par)

func_del(4)
print(list_key)
