#### 3.2[18]: Требуется найти в списке целых чисел самый близкий по величине элемент к заданному числу X. 
# Пользователь вводит это число с клавиатуры, список можно считать заданным. Введенное число не обязательно 
# содержится в списке.

    # Примеры/Тесты:
    # Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 0
    # Output: 2
    # Input: [10, 5, 7, 3, 3, 2, 5, 7, 3, 8], X = 9
    # Output: 10


number = int(input(f'Введите число: '))
# number = 14

default_list = [10, 5, 7, 3, 3, 2, 5, 7, 3, 8]
# default_list = [1, 2, 195, 4, 5, 6, 8, 12, 76, 15, 17, 18, 3, 21, 30, 51, 9, 127]

line = f'\n{"=" * 60}\n'
DEBUG = False

'''
Вариант 1: 
через преобразование в множество (для удаления лишних элементов списка) и обратно, и возможности 
обратиться к элементу по номеру в сортированном списке. При увеличении разницы, выход из цикла.
'''
print(f'Вариант 1: через преобразование в множество и обратно в список:')
default_set = set(default_list)

default_list = sorted(list(default_set))
if number < default_list[0]:
    nearest = default_list[0]

elif number > default_list[-1]:
    nearest = default_list[-1]

else:
    full_len = len(default_list)
    half_len = full_len//2
    last_difference = None

    if number < default_list[half_len]:
        if DEBUG: 
            print(f'{number} < {default_list[half_len]}')
        range_start = 0
        range_end = half_len

    elif number >= default_list[half_len]:
        if DEBUG: 
            print(f'{number} >= {default_list[half_len]}')
        range_start = half_len
        range_end = full_len

    for i in range(range_start, range_end):
        difference = abs(default_list[i] - number)
        if DEBUG: 
            print(f'{difference} = {abs(default_list[i] - number)} ({default_list[i]} - {number})')
        if last_difference is None:
            last_difference = difference

        if difference <= last_difference:
            last_difference = difference
            nearest = default_list[i]
        else:
            break

        if DEBUG: 
            print(f'i: {i}; nearest: {nearest}; last_difference: {last_difference}')

print(f'Введено число: {number}\nБлижайшее число: {nearest}{line}')


'''
Вариант 2: 
через преобразование в множество (для удаления лишних элементов списка).
'''
print(f'Вариант 2: через преобразование в множество:')
default_set = set(default_list)
last_difference = None

for number_in_set in default_set:
        difference = abs(number_in_set - number)
        if DEBUG: 
            print(f'{difference} = {abs(number_in_set - number)} ({number_in_set} - {number})')
        if last_difference is None:
            last_difference = difference

        if difference <= last_difference:
            last_difference = difference
            nearest = number_in_set

print(f'Введено число: {number}\nБлижайшее число: {nearest}{line}')


'''
Вариант 2: 
через преобразование в множество (для удаления лишних элементов списка) и поиск всех ближайших 
равнозначных элементов.
'''
print(f'Вариант 3: через преобразование в множество (вывод двух ближайших):')
default_set = set(default_list)
nearest = set()
last_difference = None

for number_in_set in default_set:
        difference = abs(number_in_set - number)
        if DEBUG: 
            print(f'{difference} = {abs(number_in_set - number)} ({number_in_set} - {number})')
        if last_difference is None:
            last_difference = difference

        if difference <= last_difference:
            if difference < last_difference:
                nearest.clear()
            last_difference = difference
            nearest.add(number_in_set)

print(f'Введено число: {number}\nБлижайшее число: {nearest}{line}')