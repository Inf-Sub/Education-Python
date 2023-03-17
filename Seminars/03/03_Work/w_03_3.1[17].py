# №3.1[17]. Дан список чисел. Определите, сколько в нем встречается различных чисел.
# Примечание: Пользователь может вводить значения списка или список задан изначально.
#     Примеры/Тесты:
#     [1, 1, 2, 0, -1, 3, 4, 4] -> 6
#     [1, 1, 2, 0, 1, 2, 1, 2]  -> 3


elements = [1, 1, 2, 0, -1, 3, 4, 4]
print(len(set(elements)))

elements = [1, 1, 2, 0, 1, 2, 1, 2]
print(len(set(elements)))



# len_elements = len(elements)
# result = []
# print(len_elements)

# for i in range(len_elements - 1):
#     print(elements[i])

# for element in elements:
#     print(elements[i])
#     for index in range(len_elements):
#         if element == elements[index]:
#             continue
#         else:
#             pass
