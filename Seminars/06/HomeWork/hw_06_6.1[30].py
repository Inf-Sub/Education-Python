# #### 6.1[30]: Напишите программу, генерирующую элементы арифметической прогрессии
# Программа принимает от пользователя три числа :

# - Первый элемент прогрессии, Разность (шаг) и Количество элементов

# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.

# 	Напишите функцию

# 	- Аргументы: три указанных параметра
# 	- Возвращает: список элементов арифмитической прогрессии.

# 	Примеры/Тесты:

# 	Ввод: 7 2 5
# 	Вывод: [7 9 11 13 15]
# 	Ввод: 2 3 12
# 	Вывод: [2, 5, 8, 11, 14, 17, 20, 23, 26, 29, 32, 35]

# ```(*)``` **Усложнение.** Для формирования списка внутри функции используйте Comprehension


# ```(**)``` **Усложнение.** Присвоение значений переменным a1,d,n запишите, используя только один input,
# в одну строку, вам понадобится распаковка и Comprehension или map


def arithmetic_progression(first: int, diff: int, counts: int) -> list:
    # version 1
    # progress_list = [0] * counts
    # for i in range(counts):
    #     progress_list[i] = first
    #     first += diff

    # version 2 (with Comprehension)
    progress_list = [first] * counts
    progress_list = [value + key * diff  for key, value in enumerate(progress_list)]
    return progress_list


# input_params = '2 3 12'.split()
input_params = input('Введите 3 числа (Первый элемент прогрессии, Разность (шаг) и Количество элементов): ').split()
first_num, step, el_counts = list(map(int, input_params))

print(arithmetic_progression(first_num, step, el_counts))
