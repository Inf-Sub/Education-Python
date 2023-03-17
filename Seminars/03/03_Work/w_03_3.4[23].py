# №3.4[23]. Дан список, состоящий из целых чисел. Напишите программу, которая сформирует список из тех элементов, 
# которые больше предыдущего (элемента с предыдущим номером) 
# Примечание: Пользователь может вводить значения списка или список задан изначально.
#     Примеры/Тесты:
#     Input: [0, -1, 5, 2, 1]
#     Output: [5]

#     Input: [-2, -1, 5, 2, 3]
#     Output: [-1, 5, 3]
# [*] Усложнение: Запишите алгоритм в одну строку, используйте Comprehension


# elements = [-2, -1, 5, 2, 3]
# elements = [0, -1, 5, 2, 1]
# for index in range(len(elements)):
#     # print(index)
#     # if index > 0:
#         if elements[index] > elements[index - 1]:
#             print(elements[index], end = ', ')


elements = [0, -1, 2, 2, 1, 11, 5, 7, 10, 0, 36]
print([elements[index] for index in range(len(elements))])
print([elements[index] for index in range(len(elements)) if elements[index] > elements[index - 1]])
print(tuple([elements[index] for index in range(len(elements)) if elements[index] > elements[index - 1]]))
print([elements[index] if elements[index] < 5 else 'NoN' for index in range(len(elements)) if elements[index] > elements[index - 1]])
print(['a' for index in range(len(elements)) if elements[index] > elements[index - 1]])
print([str(index) for index in range(len(elements)) if elements[index] > elements[index - 1]])

