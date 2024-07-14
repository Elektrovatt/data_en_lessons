# # 1. Написать функцию без параметров.
# #
# def first_func():
#     print('first func')
#
#
# # 2. Написать функцию с 1 параметром.
# #
# list_elements = ['1', '2', '3']
# def two_func(a: list):
#     print(a)
#
# # 3. Написать функцию с 3 параметрами.
# #
# def func_3(a, b, c):
#     print(a, b, c)
#
#
# # func_3(1,2,3)
# # 4. Написать функцию с 3 параметрами - и последнему параметру задать значение по умолчанию.
# #
# def func_4(a, b, c=5):
#     print(a, b, c)
#
#
# # func_4(1, 2)
# # 5. Функцию с 1 параметром вызвать внутри цикла.
# #
# # def func_5(a):
# #     print(a)
# #
# #
# # list = [1, 2, 0]
# # for i in list:
# #     func_5(i)
#
# # 6. Написать функцию с 1 параметром - и в этот параметр передать переменную типа list.
# # Функция должна возвращать сумму всех элементов list, который в неё передали.
# # Возвращать через return - а не просто через print выводить.
# #
#
# def func_6(a:list):
#     summa = 0
#
#     for i in a:
#         summa += int(i)
#
#     return print(summa)
#     # print(summa)

# list_ele6 = [1, 3, 4]
# func_6(list_ele6)

# def func_6(a, b):
#     sum1 = a + b
#     print(sum1)
#     return sum1
#
# func_6(1,2)
# 7. Вызвать одну функцию внутри другой.
#
# def func_1(i):
#     print(f'hello {i}')
#
# def func_2(b):
#     func_1('lexa')
#     print(b)
#
# func_2('vadim')
# 8. Прочитать в интернете, что такое сортировка пузырьком.
# Написать себе на листке алгоритм, после чего написать функцию,
# которая на вход получает список (list),
# сортирует его пузырьком, после чего возвращает отсортированный список.
#
#
from random import randint
def b_sort(a:list):

    length = len(a)
    for i in range(length):
        for j in range(0, length-i-1):
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
    print(a)

b_sort([1, 9, 4, 2, 8])