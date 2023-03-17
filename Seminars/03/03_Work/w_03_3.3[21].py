# №3.3[21]. Напишите программу для печати всех уникальных значений в списке словарей.
# Примечание: Список словарей задан изначально. Пользователь его не вводит
# Обратите внимание, что в словарях может быть один или несколько элементов
#     Примеры/Тесты:
#     Input:  [{"V": "S001", "X": "D009"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005", "XI": "D011"}, 
#               {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 ", "XII": "D001"}]
#     Output: {'S005', 'S002', 'S007', 'S001', 'S009'}
# [*]  Усложнение. Проверку уникальности строк сделайте без учета пробелов до и после значимой части строки
# [**] Усложнение. Запишите алгоритм в одну строку, используйте Comprehension


my_list = [
    {"V": "S001", "X": "D009"}, 
    {"V": "S002"}, 
    {"VI": "S001"}, 
    {"VI": "S005", "XI": "D011"}, 
    {"VII": " S005 "}, 
    {" V ":" S009 "}, 
    {" VIII ":" S007 ", "XII": "D001"}
    ]

# my_list = []
my_set1 = set()
my_set2 = set()

for elements in my_list:
    # print(elements)
    for element in elements.values():
        # print(element)
        # my_list.append(element)

        my_set1.add(element)
        my_set2.add(element.strip())

# print(set(my_list))
print(my_set1)
print('* Усложнение')
print(my_set2)

# print({element for element in my_list})
# print([elements for elements in my_list])
# print([element for elements in my_list for element in elements.values()])
print('** Усложнение')
print('Comprehension:')
print({element.strip() for elements in my_list for element in elements.values()})

print({element.strip() : element.strip() for elements in my_list for element in elements.values()})

print({element : element for elements in my_list for element in elements.items()})

print({element[0].strip() : element[1].strip() for elements in my_list for element in elements.items()})

print({key : value.strip() for elements in my_list for key, value in elements.items()})

print({key.strip() : value.strip() for elements in my_list for key, value in elements.items()})

