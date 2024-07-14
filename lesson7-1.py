# list1 = [2, 0, 6, 'hello']


# def list_division(local_list: list):
#     l_result = list()
#     for one_element in local_list:
#         try:
#             l_result.append(one_element / 2)
#         except Exception as e:
#             print(e)
#         finally:
#             print(one_element)
#     return l_result


# print(list_division(list1))

def foo(element:int) -> list:
    local_list = []
    try:
        is_minus = element < 0
        for one_element in range(abs(element)):
            if not one_element % 2:
                local_list.append(one_element if not is_minus else one_element*(-1))
        return print(local_list)
    except Exception as e:
        print(e)

foo(-10)
# list2 = list1[::-2]
# print(list2)
def test1():
    assert foo(10) == [0, 2, 4, 6, 8], 'всё работает'
    assert foo(-10) == [0, -2, -4, -6, -8], ' vse works'

test1()