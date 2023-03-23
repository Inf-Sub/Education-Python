# №5.2[33]. Хакер Василий получил доступ к классному журналу и хочет заменить
# все свои минимальные оценки на максимальные.
# Напишите функцию, которая заменяет оценки, переданные в виде списка, но
# наоборот: все максимальные – на минимальные.
# Функция должна возвращать новый список оценок
# Примечание: Обратите внимание на side effects функции.
# Примеры/Тесты:
#     <function_name>([1, 3, 3, 3, 4, 2, 5, 5, 2]) -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

# [*] Усложненение: Если ни одна оценка не была заменена, функция должна вернуть None
# Примеры/Тесты:
#     <function_name>([3, 3, 3, 3, 3, 3, 3, 3, 3]) -> None
# [**] Усложненение: Добавьте параметр в функцию, который определит как будут заменены оценки:
# Друзьям минимальные на максимальные, Врагам - наоборот.
# Примеры/Тесты:
#     grades = [1, 3, 3, 3, 4, 2, 5, 5, 2]
#     <function_name>(grades, "friend") -> [5, 3, 3, 3, 4, 2, 5, 5, 2]
#     <function_name>(grades, "enemy")  -> [1, 3, 3, 3, 4, 2, 1, 1, 2]

def change(grades: list, status: str = None) -> list:
    new_grades = []
    max_grade = max(grades)
    min_grade = min(grades)

    status_dict = {'friend': True, 'enemy': False}

    if min_grade == max_grade:
        return None


    for grade in grades:
        if status is None or not status_dict[status]:
            if grade == max_grade:
                grade = min_grade
        elif status_dict[status]:
            if grade == min_grade:
                grade = max_grade

        new_grades.append(grade)


    return new_grades



grades_list_1 = [1, 3, 3, 3, 4, 2, 5, 5, 2]
grades_list_2 = [3, 3, 3, 3, 3, 3, 3, 3, 3]
grades_list_3 = [1, 3, 3, 3, 4, 2, 5, 5, 2]

print(change(grades_list_1))
print(change(grades_list_2))
print(change(grades_list_3, "friend"))
print(change(grades_list_3, "enemy"))
