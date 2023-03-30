# №6.1[39]. Даны два списка чисел. Требуется вывести те элементы первого списка ,
# которых нет во втором списке.
# Создайте функцию.
#     Аргументы: два списка целых чисел
#     Возвращает: список элементов (смотри условие)

# Примеры/Тесты:
#     <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [2, 3, 12]
#     <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3,4]

# [*] Усложнение. Элементы необходимо возвращать в том порядке, в котором они находятся в первом списке, с учетом повторений
# Примеры/Тесты:
#     <function_name>([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1] ) -> [3, 3, 2, 12]
#     <function_name>([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5] ) -> [3, 4, 3, 4]

from time import perf_counter
from random import randint

def set_diferecne(list_a, list_b):
    t1 = perf_counter()
    result = list(set(list_a).difference(set(list_b)))
    t2 = perf_counter()
    return result, t2 - t1

print(set_diferecne([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
print(set_diferecne([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))

def list_diferecne(list_a, list_b):
    t1 = perf_counter()
    new_list = []
    for i in list_a:
        if not (i in list_b or i in new_list):
            new_list.append(i)
    t2 = perf_counter()

    return new_list,  t2 - t1

print(list_diferecne([3, 1, 3, 4, 2, 4, 12], [4, 15, 43, 1, 15, 1]))
print(list_diferecne([3, 4, 1, 5, 1, 3, 10, 4, 9, 5], [9, 6, 6, 5, 10, 1, 10, 9, 1, 5]))

n = 10000
lst1 = [randint(0, int(n)) for _ in range(n)]
lst2 = [randint(0, int(n)) for _ in range(n)]

print(set_diferecne(lst1, lst2)[1])
print(list_diferecne(lst1, lst2)[1])
